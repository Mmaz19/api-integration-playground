# Event Driven Patterns

## Publish / Subscribe

Multiple consumers can react to the same event.

```mermaid
flowchart LR

A[Producer]

A --> B[Event Broker]

B --> C[Consumer A]

B --> D[Consumer B]

B --> E[Consumer C]
```

---

## Benefits

- Loose coupling
- Scalability
- Independent systems
- Easier evolution

---

## Challenges

- Event ordering
- Duplicate messages
- Monitoring complexity
- Data consistency