# From Benchmarks to Production: A Text-to-SQL System for Complex Financial Data

- arXiv ID: `2610.03524v1`
- Authors: Arijit Sehanobish, Bruno Gomes Coelho, Guillaume Michel, Sophia Zhi, Valerie Faucon-Morin, Kristen Howell
- Published: 2026-10-02
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2610.03524v1) | [pdf](https://arxiv.org/pdf/2610.03524v1)

## Abstract

General-purpose Text-to-SQL systems achieve strong performance on academic benchmarks like Spider and BIRD, where schemas are relatively shallow and column values are often human readable. In production financial databases, where concepts are stored as opaque integer keys rather than human-readable strings, these methods fall below 50%, as even simple queries require multiple joins and filter predicates reference opaque IDs. We present Financial LINking Text-to-SQL (FLINT), a domain-specialized Text-to-SQL system that closes this gap through three key components: (1) a lookup agent that dynamically resolves natural-language concepts to question-specific reference table constraints, (2) embedding-based retrieval of structurally similar query templates from a compact, expert-authored bank, and (3) schema linking that prunes a large table schema to the relevant subset by traversing foreign-key chains, rather than relying on name similarity alone. We evaluate on two datasets totaling 359 questions over production financial schemas. FLINT outperforms various state-of-the-art baselines using the same LLM. The system is deployed in production as part of a financial data retrieval service.
