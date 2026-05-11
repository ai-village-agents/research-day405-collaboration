// Configuration loader with defaults and overrides

const defaultConfig = {
  apiKey: '',
  server: {
    host: 'localhost',
    port: 3000,
  },
  features: {
    caching: true,
    retries: 3,
  },
};

function loadConfig(overrides = {}) {
  // BUG: Uses shallow Object.assign which drops nested override properties.
  const merged = Object.assign({}, defaultConfig, overrides);

  // BUG: Missing validation for required fields like apiKey or server.host.
  // (No checks performed here.)

  // BUG: Null/undefined overrides are accepted and wipe out defaults silently.
  // e.g., overrides.server = null will erase server settings without fallback.

  // SUSPICIOUS NON-BUG: Basic configuration loading pattern is correct; merging overrides into defaults is intentional.
  return merged;
}

module.exports = {
  loadConfig,
  defaultConfig,
};
