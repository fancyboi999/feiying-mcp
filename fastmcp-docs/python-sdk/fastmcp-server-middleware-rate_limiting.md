# rate_limiting - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting
**Generated:** 2025-06-30

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

middleware

rate\_limiting

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting\#fastmcp-server-middleware-rate-limiting)  `fastmcp.server.middleware.rate_limiting`

Rate limiting middleware for protecting FastMCP servers from abuse.

## [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting\#ratelimiterror)  `RateLimitError`

Error raised when rate limit is exceeded.

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting\#tokenbucketratelimiter)  `TokenBucketRateLimiter`

Token bucket implementation for rate limiting.

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting\#slidingwindowratelimiter)  `SlidingWindowRateLimiter`

Sliding window rate limiter implementation.

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting\#ratelimitingmiddleware)  `RateLimitingMiddleware`

Middleware that implements rate limiting to prevent server abuse.

Uses a token bucket algorithm by default, allowing for burst traffic
while maintaining a sustainable long-term rate.

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting\#slidingwindowratelimitingmiddleware)  `SlidingWindowRateLimitingMiddleware`

Middleware that implements sliding window rate limiting.

Uses a sliding window approach which provides more precise rate limiting
but uses more memory to track individual request timestamps.

[middleware](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware) [timing](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-timing)

On this page

- [fastmcp.server.middleware.rate\_limiting](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting#fastmcp-server-middleware-rate-limiting)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting#classes)
- [RateLimitError](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting#ratelimiterror)
- [TokenBucketRateLimiter](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting#tokenbucketratelimiter)
- [SlidingWindowRateLimiter](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting#slidingwindowratelimiter)
- [RateLimitingMiddleware](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting#ratelimitingmiddleware)
- [SlidingWindowRateLimitingMiddleware](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting#slidingwindowratelimitingmiddleware)

Assistant

Responses are generated using AI and may contain mistakes.