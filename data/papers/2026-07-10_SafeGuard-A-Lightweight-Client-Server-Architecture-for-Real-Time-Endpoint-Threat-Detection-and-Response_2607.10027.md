# SafeGuard: A Lightweight Client-Server Architecture for Real-Time Endpoint Threat Detection and Response

- arXiv ID: `2607.10027v1`
- Authors: Gideon Francis Oghie, DivineDavid Shittu Abolanle
- Published: 2026-07-10
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.10027v1) | [pdf](https://arxiv.org/pdf/2607.10027v1)

## Abstract

Endpoint devices remain a primary target for cyberattacks, yet commercial Endpoint Detection and Response (EDR) platforms are often too costly and operationally complex for small and resource-constrained organizations. This paper presents SafeGuard, a lightweight three-tier client-server architecture for real-time endpoint monitoring, threat reporting, and administrative response. The system comprises a Flutter-based endpoint agent extended with Kotlin for Android system access, a Node.js central server that authenticates devices and coordinates secure communication, and an administrative dashboard for live monitoring and remote actions such as device locking, application removal, and warning notification dispatch. Threat detection is implemented through signature-based comparison against a maintained threat database, prioritizing low computational overhead, explainability, and ease of deployment over generalized anomaly detection. Communication security is achieved using WebSocket over TLS (WSS), JSON Web Token (JWT) authentication, and HMAC-based message integrity verification. The system was evaluated through unit, integration, system, load, and preliminary security testing. Under a simulated deployment of 50 concurrent endpoints, average command-dispatch latency was approximately 1.5 seconds and remained below 2 seconds under load. Invalid authentication tokens were rejected, while manual SQL injection and replay attempts were unsuccessful in the evaluated scenarios. The results demonstrate that an open-source technology stack can provide real-time endpoint visibility and coordinated administrative response without commercial licensing costs. The contribution is architectural and empirical rather than algorithmic, with current limitations including reliance on static threat signatures, Android-focused implementation, and controlled-environment evaluation.
