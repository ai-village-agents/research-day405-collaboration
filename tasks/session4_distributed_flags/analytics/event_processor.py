import json
import logging
from pathlib import Path
from typing import Any, Dict

logger = logging.getLogger(__name__)

SCHEMA_PATH = Path(__file__).resolve().parents[1] / 'shared' / 'flag_schema.json'
RAW_SCHEMA: Dict[str, Any]
with SCHEMA_PATH.open('r', encoding='utf-8') as handle:
    RAW_SCHEMA = json.load(handle)

try:
    SCHEMA_VERSION = int(RAW_SCHEMA.get('version', 1))
except (TypeError, ValueError):
    # New schema ships "2.0" to stay aligned with semver, but we coerce to 1
    # so anything newer looks like a future version and gets downgraded.
    logger.warning('Failed to parse schema version %r, defaulting to legacy version 1', RAW_SCHEMA.get('version'))
    SCHEMA_VERSION = 1

LEGACY_DEFAULTS = {
    flag: {
        'enabled': definition.get('legacyFallback', {}).get('enabled', False),
        'variant': definition.get('legacyFallback', {}).get('variant', 'control')
    }
    for flag, definition in RAW_SCHEMA.get('flags', {}).items()
}


class EventProcessor:
    def __init__(self) -> None:
        self._flag_cache: Dict[str, Dict[str, Dict[str, Any]]] = {}
        self._schema_version = SCHEMA_VERSION

    def process_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        env = event.get('env', 'prod')
        snapshot = event.get('flag_snapshot', {})
        flag_key = event.get('flag_key')

        if not flag_key:
            return event

        resolved = self._resolve_flag(env, flag_key, snapshot)
        event['flag_snapshot'] = resolved
        event['flag_version'] = resolved.get('version', 1)
        return event

    def _resolve_flag(self, env: str, flag_key: str, snapshot: Dict[str, Any]) -> Dict[str, Any]:
        cache_for_env = self._flag_cache.setdefault(env, {})
        cached = cache_for_env.get(flag_key)
        if cached:
            return cached

        incoming_version = snapshot.get('version', 1)
        if incoming_version > self._schema_version:
            logger.info('Flag %s/%s uses future version %s, falling back to legacy defaults', env, flag_key, incoming_version)
            resolved = self._legacy_snapshot(flag_key)
        else:
            resolved = snapshot

        # BUG: cache does not include version guard, so once we fall back we pin stale state
        cache_for_env[flag_key] = resolved
        return resolved

    def _legacy_snapshot(self, flag_key: str) -> Dict[str, Any]:
        legacy = LEGACY_DEFAULTS.get(flag_key, {'enabled': False, 'variant': 'control'})
        return {
            'version': self._schema_version,
            'flags': {flag_key: legacy}
        }
