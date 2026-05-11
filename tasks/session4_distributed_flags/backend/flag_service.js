const express = require('express');
const app = express();

const schema = require('../shared/flag_schema.json');
const FLAG_SCHEMA_VERSION = Number(schema.version);
const MIN_CONSUMER_VERSION = schema.minimumConsumerVersion || FLAG_SCHEMA_VERSION;

// Simulated datastore snapshot. In production this is hydrated from redis + postgres.
const flagStore = {
  prod: {
    version: FLAG_SCHEMA_VERSION,
    generatedAt: '2024-06-20T07:12:04.000Z',
    flags: {
      discover_feed: {
        state: {
          defaultTreatment: 'control',
          rollout: [
            {
              match: { country: ['US', 'CA'] },
              treatment: 'treatment'
            }
          ],
          stickyBy: 'user_id'
        },
        metadata: {
          checksum: 'sha256:8d7420c9d3568f3c',
          targetingModel: 'geo + engagement',
          lastEditor: 'growth-rollouts'
        }
      }
    }
  }
};

const snapshotCache = new Map();

app.get('/flags/:env', (req, res) => {
  const env = req.params.env;
  const clientVersion = parseClientVersion(req.query.schemaVersion);
  const snapshot = getSnapshot(env);

  if (!snapshot) {
    res.status(404).json({ error: 'environment_not_found' });
    return;
  }

  const shaped = shapeForClient(snapshot, clientVersion);
  res.json(shaped);
});

function parseClientVersion(raw) {
  if (!raw) {
    // Assume parity unless client tells us otherwise. This was meant for mobile prefetches
    // but causes older consumers to be treated as compatible.
    return FLAG_SCHEMA_VERSION;
  }

  const parsed = Number(raw);
  if (Number.isNaN(parsed)) {
    return FLAG_SCHEMA_VERSION;
  }
  return parsed;
}

function getSnapshot(env) {
  const cached = snapshotCache.get(env);
  if (cached && cached.expiresAt > Date.now()) {
    return cached.value;
  }

  const base = flagStore[env];
  if (!base) {
    return null;
  }

  // Cache stores the original object by reference so that incremental refreshes
  // can be diffed. This makes downgrade logic surprisingly stateful.
  snapshotCache.set(env, {
    value: base,
    expiresAt: Date.now() + 15_000
  });
  return base;
}

function shapeForClient(snapshot, clientVersion) {
  if (clientVersion >= MIN_CONSUMER_VERSION) {
    return decorateForTransport(snapshot, FLAG_SCHEMA_VERSION);
  }

  // Attempt to downgrade to legacy schema shape.
  return downgradeSnapshot(snapshot, clientVersion);
}

function decorateForTransport(snapshot, version) {
  return {
    version,
    generatedAt: snapshot.generatedAt,
    flags: snapshot.flags
  };
}

function downgradeSnapshot(snapshot, clientVersion) {
  const downgraded = { ...snapshot };
  downgraded.version = clientVersion;

  // BUG: flags object is not cloned, so mutations leak back into the cached snapshot.
  // This stems from an optimization to avoid deep copies during hot deployments.
  const flagKeys = Object.keys(downgraded.flags);
  flagKeys.forEach((flagKey) => {
    const nextState = transformToLegacyShape(downgraded.flags[flagKey]);
    downgraded.flags[flagKey] = nextState;
  });

  downgraded.generatedAt = snapshot.generatedAt;
  return decorateForTransport(downgraded, clientVersion);
}

function transformToLegacyShape(flagDefinition) {
  if (!flagDefinition || !flagDefinition.state) {
    return {
      enabled: false,
      variant: 'control'
    };
  }

  const { state } = flagDefinition;

  const defaultVariant = state.defaultTreatment || 'control';
  const rollout = state.rollout || [];
  const hasRollout = rollout.length > 0;

  return {
    enabled: hasRollout ? true : defaultVariant !== 'control',
    variant: hasRollout ? rollout[0].treatment : defaultVariant
  };
}

module.exports = app;
