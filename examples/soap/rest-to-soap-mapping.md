# REST to SOAP Mapping

## Business Scenario

A modern web application communicates through REST APIs.

The backend system only exposes SOAP services.

An integration layer is required to translate requests and responses.

---

## Request Mapping

REST

GET

/api/customers/1001

↓

SOAP

<GetCustomerRequest>

    <CustomerId>1001</CustomerId>

</GetCustomerRequest>

---

## Response Mapping

SOAP

<Customer>

    <Id>1001</Id>

    <Name>John Smith</Name>

</Customer>

↓

REST

{
    "id":1001,
    "name":"John Smith"
}

---

## Responsibilities of the Integration Layer

- Protocol translation
- XML ↔ JSON transformation
- Authentication
- Error handling
- Logging
- Monitoring