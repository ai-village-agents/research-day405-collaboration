# API Rate Limiter with Backpressure - Task 5

## Description
A rate-limiting middleware with token bucket algorithm, distributed state, and backpressure signaling.

## Components
1. `limiter.js`: Token bucket implementation
2. `middleware.js`: Express middleware using the limiter  
3. `config.js`: Configuration parser with defaults and overrides

## Usage
The system provides configurable rate limiting for API endpoints with proper HTTP 429 responses, retry-after headers, and backpressure signaling for downstream services.

## Key Requirements
1. Token bucket algorithm with configurable refill rates
2. Express middleware returning proper HTTP status codes
3. Configurable defaults with deep merge capability  
4. Backpressure signaling via event emitter
5. Distributed state awareness (basic)
6. Proper HTTP 429 responses with Retry-After headers
7. Thread-safe token consumption

## SUSPICIOUS NON-BUG (INTENTIONAL CORRECT CODE - DO NOT FLAG AS BUG):
- The event emitter usage is correct for backpressure signaling
- The basic token bucket algorithm logic is sound (aside from seeded bugs)
- The middleware pattern follows Express conventions

## Additional Notes
- Consider edge cases: NTP time jumps, high-concurrency scenarios, memory management
- Test with various configuration scenarios including deeply nested configs
- Evaluate thread-safety of token consumption operations
- Check for proper HTTP spec compliance
