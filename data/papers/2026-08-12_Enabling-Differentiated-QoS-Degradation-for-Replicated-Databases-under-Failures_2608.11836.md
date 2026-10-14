# Enabling Differentiated QoS Degradation for Replicated Databases under Failures

- arXiv ID: `2608.11836v1`
- Authors: Belkis Djeffal, Pierre Bourhis, Romain Rouvoy
- Published: 2026-08-12
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2608.11836v1) | [pdf](https://arxiv.org/pdf/2608.11836v1)

## Abstract

Elasticity is commonly presented as the default response to capacity loss after failures, since replacement replicas can compensate for failed nodes and restore pre-incident service levels. Replacement capacity entails both delay and additional resource commitment, as replicas must be provisioned and synchronized before they can serve traffic. Under fixed budgets or constrained operating conditions, capacity restoration cannot be treated as the immediate recovery path. Failure handling must instead define how the service continues while capacity remains reduced. When the service exposes differentiated service levels, capacity loss cannot be handled uniformly. Degradation becomes part of the service behavior, requiring explicit control over how reduced capacity affects each class without erasing the intended differentiation.  We study differentiated QoS degradation in replicated database services with service-class-aware sessions. We present a repair-to-target policy, implemented in PLB, a PostgreSQL JDBC middleware load balancer for service-class-aware routing. When fail-stop failures remove part of the available capacity, PLB updates the role assignment of healthy replicas into Premium, Mixed, and Freemium roles. This keeps the replica pool shared while ensuring that new session assignments continue to reflect the service class. We evaluate PLB under single and cascading replica failures across two deployment strategies: isolated perclass replica pools and shared, priority-agnostic routing. The results show that PLB improves median Premium goodput retention by 26-28 percentage points under a Premium-side fault, achieves more than 2x higher Premium goodput in the most severe cascading-failure phase, and reduces Premium p95 latency by 18.2% relative to shared round-robin.
