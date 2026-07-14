# OAuth 2.0 - Client Credentials Flow

## Business Scenario

A backend application needs to securely access another system without user interaction.

Example:

ERP → CRM

or

Middleware → External API

---

## Flow

Application

↓

Authorization Server

↓

Access Token

↓

Protected API

---

## Required Information

- Client ID
- Client Secret
- Token Endpoint
- Scope

---

## Typical Request

POST /oauth/token

grant_type=client_credentials

client_id=...

client_secret=...

---

## Result

The application receives an Access Token that is used for subsequent API calls.