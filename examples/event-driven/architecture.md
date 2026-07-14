# Event Driven Architecture

```mermaid
flowchart LR

A[CRM]

A --> B[Event Producer]

B --> C[Message Broker]

C --> D[ERP]

C --> E[Analytics]

C --> F[Notification Service]
```

---

## Components

| Component | Responsibility |
|-|-|
| Producer | Generates events |
| Broker | Routes messages |
| Consumer | Processes events |

---

## Consultant Perspective

When designing event-driven integrations, evaluate:

- Business requirements
- Processing latency
- Data consistency
- Failure handling
- Monitoring requirements