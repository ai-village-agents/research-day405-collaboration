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
  const merged = Object.assign({}, defaultConfig, overrides);

  return merged;
}

module.exports = {
  loadConfig,
  defaultConfig,
};
