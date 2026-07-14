# Event-Driven Integration

## Overview

Not all integrations require a synchronous request-response model.

Event-driven architectures allow systems to communicate asynchronously by publishing and consuming events.

This approach improves scalability, resilience, and decoupling between applications.

---

## Business Scenario

A customer places an order in an e-commerce platform.

Multiple systems need to react:

- Inventory management
- Payment processing
- Customer notification
- Analytics platform

Instead of calling each system directly, the platform publishes an event.

---

## Traditional Approach

```mermaid
flowchart LR

A[Order System]
--> B[Payment System]

A --> C[Inventory System]

A --> D[Notification System]
```

The order system is tightly coupled with multiple dependencies.

---

## Event-Driven Approach

```mermaid
flowchart LR

A[Order System]

A --> B[Order Created Event]

B --> C[Message Broker]

C --> D[Payment Service]

C --> E[Inventory Service]

C --> F[Notification Service]
```

---

## Topics Covered

- Webhooks
- Events
- Message brokers
- Retry strategies
- Idempotency
- Asynchronous communication