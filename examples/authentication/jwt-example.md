# JWT Authentication

## What is a JWT?

A JSON Web Token (JWT) is a compact token used to securely transmit information between systems.

Typical structure:

> Header.Payload.Signature

Example:

xxxxx.yyyyy.zzzzz

---

## Typical Flow

Client

↓

Authentication Service

↓

JWT Token

↓

Protected API

---

## Authorization Header

```http
Authorization: Bearer <token>
```

---

## Common Troubleshooting

### 401 Unauthorized

Possible causes:

- Missing token
- Expired token
- Invalid signature

### 403 Forbidden

Authentication succeeded but the user lacks the required permissions.