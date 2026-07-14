# SOAP Integration

## Overview

Although REST APIs have become the standard for many modern applications, SOAP services are still widely used in enterprise environments, especially in industries such as banking, insurance, healthcare, and public administration.

Understanding how to interact with SOAP services remains an important skill for Integration Specialists and Technical Consultants.

---

## What is SOAP?

SOAP (Simple Object Access Protocol) is an XML-based messaging protocol used to exchange structured information between systems.

Unlike REST, SOAP relies on a formal contract defined through a WSDL (Web Services Description Language).

---

## Typical Enterprise Scenario

A CRM system needs to retrieve customer information from a legacy ERP exposing SOAP services.

```
CRM
 │
 │ SOAP Request
 ▼
ERP Web Service
 │
 │ SOAP Response
 ▼
CRM
```

---

## Repository Contents

- Example SOAP Request
- Example SOAP Response
- REST-to-SOAP mapping
- Troubleshooting guide