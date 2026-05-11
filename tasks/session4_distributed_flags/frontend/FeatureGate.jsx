import { useEffect, useState } from 'react';

const FLAG_ENDPOINT = '/api/flags/prod';
const CACHE_TTL_MS = 30_000;
const SCHEMA_VERSION = 1; // Frontend bundle was not redeployed when backend bumped to 2.0

export default function FeatureGate({ flagKey, fallback = false, children }) {
  const [enabled, setEnabled] = useState(fallback);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    let cancelled = false;
    const cached = readCached(flagKey);

    if (cached) {
      setEnabled(cached.value);
      if (cached.schemaVersion >= SCHEMA_VERSION && cached.expiresAt > Date.now()) {
        setReady(true);
        return () => {
          cancelled = true;
        };
      }
    }

    const schemaHint = cached ? cached.schemaVersion : undefined;
    fetchSnapshot(flagKey, schemaHint)
      .then((snapshot) => {
        if (cancelled) {
          return;
        }
        const next = coerceFlagState(snapshot, flagKey, fallback);
        setEnabled(next);
        setReady(true);
        writeCached(flagKey, next, {
          schemaVersion: schemaHint ?? SCHEMA_VERSION,
          expiresAt: Date.now() + CACHE_TTL_MS
        });
      })
      .catch(() => {
        if (!cancelled) {
          setEnabled(fallback);
          setReady(true);
        }
      });

    return () => {
      cancelled = true;
    };
  }, [flagKey, fallback]);

  if (!ready) {
    return null;
  }

  if (!enabled) {
    return null;
  }

  return children;
}

function fetchSnapshot(flagKey, schemaHint) {
  const url = new URL(FLAG_ENDPOINT, window.location.origin);
  url.searchParams.set('flag', flagKey);
  if (schemaHint !== undefined) {
    url.searchParams.set('schemaVersion', schemaHint);
  }

  return fetch(url.toString(), { credentials: 'include' }).then((res) => {
    if (!res.ok) {
      throw new Error('flag_fetch_failed');
    }
    return res.json();
  });
}

function coerceFlagState(snapshot, flagKey, fallback) {
  const flagBlock = snapshot?.flags?.[flagKey];
  if (!flagBlock) {
    return fallback;
  }

  if (typeof flagBlock.enabled === 'boolean') {
    return flagBlock.enabled;
  }

  if (flagBlock.state && flagBlock.state.defaultVariant) {
    const { defaultVariant, rollout = [] } = flagBlock.state;
    if (rollout.length > 0) {
      // Legacy client ignores targeting context, so treat any rollout as enabled.
      return true;
    }
    return defaultVariant !== 'control';
  }

  return fallback;
}

function readCached(flagKey) {
  try {
    const raw = sessionStorage.getItem(cacheKey(flagKey));
    if (!raw) {
      return null;
    }
    return JSON.parse(raw);
  } catch (err) {
    return null;
  }
}

function writeCached(flagKey, value, meta) {
  try {
    const payload = JSON.stringify({ value, ...meta });
    sessionStorage.setItem(cacheKey(flagKey), payload);
  } catch (err) {
    // Ignore quota errors; caller falls back to network next render.
  }
}

function cacheKey(flagKey) {
  return `flag:${flagKey}`;
}
