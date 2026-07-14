# Common HTTP Errors

| Status | Meaning | Typical Cause | Suggested Action |
|---------|----------|---------------|------------------|
| 400 | Bad Request | Invalid payload | Validate request body |
| 401 | Unauthorized | Missing or expired token | Verify authentication |
| 403 | Forbidden | Insufficient permissions | Check user roles |
| 404 | Not Found | Wrong endpoint | Verify API URL |
| 409 | Conflict | Duplicate resource | Review business logic |
| 429 | Too Many Requests | Rate limit exceeded | Retry with backoff |
| 500 | Internal Server Error | Server issue | Check server logs |
| 503 | Service Unavailable | Temporary outage | Retry later |