# ARACDE: Retrofitting Databases with ABAC using External Authorization Engines

- arXiv ID: `2610.18660v1`
- Authors: Karthikeya S M Yelisetty, Shamik Sural, Santosh Nagarakatte
- Published: 2026-10-13
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.18660v1) | [pdf](https://arxiv.org/pdf/2610.18660v1)

## Abstract

This paper proposes a methodology for decoupling the authorization logic of a relational database from its core data management engine, enabling specification of advanced access control policies with minimal changes to the code base. Our decoupled authorization architecture, which we call ARCADE, externalizes access request resolution to a formally verifiable policy engine (e.g., Cedar), while the database itself enforces those decisions. We showcase the capabilities of ARCADE on two widely popular open-source databases, namely MySQL and PostgreSQL. Purpose built lightweight plugins add an Attribute-based Access Control (ABAC) layer that augments the native discretionary and role-based access control capabilities of these databases. ARCADE supports highly expressive policies using attributes of subjects, objects, and the environment, and the use of Cedar enables easy auditing and verification of the specified policies. It follows a design principle that mitigates potential risks in segregating authorization from the database core through low footprint, network isolation, and a policy composition methodology that does not negate any native authorization. Experiments on TPC-C, TPC-B, and a custom workload show that ARCADE incurs negligible performance overhead, for instance, less than 3.9% throughput penalty for MySQL (1.3% for PostgreSQL) on industry standard TPC-C benchmark.
