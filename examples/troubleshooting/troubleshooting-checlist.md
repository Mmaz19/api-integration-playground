# API Troubleshooting Checklist

## Connectivity

- Is the endpoint reachable?
- Is HTTPS correctly configured?
- Are DNS settings correct?

---

## Authentication

- Is the token valid?
- Has the token expired?
- Is the Authorization header present?

---

## Request

- Is the HTTP method correct?
- Are mandatory headers included?
- Is the payload valid?

---

## Response

- HTTP Status Code
- Response Body
- Error Message
- Response Time

---

## Logging

Always capture:

- Timestamp
- Endpoint
- Status Code
- Request ID
- Correlation ID (if available)

This information significantly reduces troubleshooting time.