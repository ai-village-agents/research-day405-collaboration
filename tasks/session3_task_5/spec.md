# API Rate Limiter with Backpressure - Task 5

## Description
A rate-limiting middleware with token bucket algorithm, distributed state, and backpressure signaling.

## Components
1. `limiter.js`: Token bucket implementation
2. `middleware.js`: Express middleware using the limiter  
3. `config.js`: Configuration parser with defaults and overrides

## Usage
The system provides configurable rate limiting for API endpoints, including HTTP 429 handling and backpressure signaling for downstream services.

## Key Requirements
1. Token bucket algorithm with configurable refill rates
2. Express middleware returning proper HTTP status codes
3. Configurable defaults with override support
4. Backpressure signaling via event emitter
5. Distributed state awareness (basic)
6. Reasonable protocol-compliant behavior for rate-limit responses
7. Correct behavior under concurrent/high-load scenarios

## Review Notes
- Some suspicious-looking patterns may be intentional.
- False positives are penalized.

## Additional Notes
- Consider edge cases related to timing, concurrency, and resource usage.
- Test with varied configuration shapes and override patterns.
- Check for reasonable HTTP/protocol compliance.
