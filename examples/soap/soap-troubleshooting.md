# SOAP Troubleshooting

## Invalid XML

Cause

Malformed XML document.

Solution

Validate the XML structure before sending the request.

---

## Invalid Namespace

Cause

Namespace declared incorrectly.

Solution

Compare namespaces with the WSDL specification.

---

## SOAP Fault

Cause

Business or application error.

Example

```xml
<soap:Fault>

    <faultcode>soap:Server</faultcode>

    <faultstring>Customer not found</faultstring>

</soap:Fault>
```

Solution

Inspect faultcode and faultstring to identify the root cause.

---

## WSDL Unavailable

Possible causes

- Wrong URL
- Network issue
- Service unavailable

Verify

- Endpoint availability
- Firewall rules
- DNS resolution