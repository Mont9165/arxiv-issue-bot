# Proof-of-Retention: A Framework for Auditable Cross-Organization Data Sharing

- arXiv ID: `2609.26654v1`
- Authors: Kyle MacMillan, Sanjay Krishnan
- Published: 2026-09-22
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.26654v1) | [pdf](https://arxiv.org/pdf/2609.26654v1)

## Abstract

The rapid adoption of AI across industries for (e.g.) fine-tuning and analytics has accelerated the need for high-quality data. To satisfy this demand, public and private entities will buy and sell data with other organizations. But such data sharing can and does violate privacy norms and laws. EU and American lawmakers have endeavored to control data sharing, restricting what data may be shared with whom, and under what circumstances. Unfortunately, accurately assessing compliance with new regulatory regimes remains a challenge, as data provenance, that is, metadata about data sharing, is rarely preserved. And even when provenance information is retained, unilateral changes to one party's database can render the provenance stale.
  To fill this gap, we present Proof-of-Retention a novel framework and interactive protocol that enforces auditable data sharing. Our framework requires each party involved in data sharing to retain a subset of information associated with each data exchange, and provides a mechanism for auditors to verify that the parties have indeed retained that information. Our approach combines techniques from database systems, including query witness generation, with cryptographic proof-of-possession protocols to provide retention guarantees. The framework enables efficient auditing that does not require full data replication or intrusive monitoring, thereby preserving privacy and remaining practical. We formalize the protocol, analyze its security and performance properties, and provide a reference implementation built on AWS infrastructure.
