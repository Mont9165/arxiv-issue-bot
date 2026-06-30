# Agent Security Meets Regulatory Reality -- A Practitioner Systematization of Autonomous-Agent Threats and Controls in Regulated Financial Systems

- arXiv ID: `2606.29142v1`
- Authors: Krishna Mohan, Guda Nagavenkata Srinivasa
- Published: 2026-06-28
- Primary category: `cs.CY`
- Categories: `cs.CY`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.29142v1) | [pdf](https://arxiv.org/pdf/2606.29142v1)

## Abstract

Large language model agents are entering regulated financial systems, yet the security literature characterizing their attack surface is almost entirely laboratory-based, and the practitioner guidance on regulated deployment is neither peer-reviewed nor connected to a formal threat model. We bridge the two from production experience. We map six established agentic threat categories namely prompt injection, identity and authorization, action auditability, tool abuse, data residency, and boundary policy enforcement onto the specific control obligations imposed by the US and the EU financial regulation (ECOA and Regulation B, the EU AI Act, GDPR Article 22, and FINRA's 2026 agent guidance), showing how legal accountability amplifies each threat relative to an unregulated deployment. We then document four architectural patterns from a production Know Your Customer deployment for a consumer credit product (A2A compliance choreography, grounded-RAG-for-audit, case-ID propagation, and an inference-boundary redaction proxy) that moved a multi-day manual process to same-day automated resolution for roughly four in five cases. Finally, we report three negative results, including two control failures surfaced only by internal audit and a population of legitimate applicants the automated pipeline cannot serve. Securing agents under regulation, we conclude, is less about novel attack classes than about making auditability, least-privilege authorization, and boundary policy enforcement real at production scale -- requirements current agent frameworks leave to the deploying engineer.
