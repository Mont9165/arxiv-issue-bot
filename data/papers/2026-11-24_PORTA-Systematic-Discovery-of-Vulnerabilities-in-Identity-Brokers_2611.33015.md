# PORTA: Systematic Discovery of Vulnerabilities in Identity Brokers

- arXiv ID: `2611.33015v1`
- Authors: Zixu Zhou, Xiangyu Guo, Ilya Grishchenko, David Lie
- Published: 2026-11-24
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.33015v1) | [pdf](https://arxiv.org/pdf/2611.33015v1)

## Abstract

Identity brokers such as Keycloak, Vault, and Dex translate authentication proofs from an upstream identity provider into sessions for downstream services. Due to their central role in authentication and trust mediation, a single vulnerability in a broker compromises every downstream service behind it. In fact, recent incidents have demonstrated that even widely adopted platforms are not immune to such issues, highlighting the critical need for systematic analysis. To build such an analysis, this work first defines invariants for broker operation. These invariants are not completely covered by existing authentication specifications, primarily because brokers are unique in their duality, i.e., acting simultaneously as a relying party and an identity provider. The invariants capture the properties that identity brokers must uphold throughout their workflows, as all 60 previous CVEs we consider violate at least one invariant. Within these workflows, we further define high-level action categories. Equipped with this information, our automated tool PORTA leverages a large language model (LLM) to generate API invocation sequences corresponding to the high-level action categories, and oracle assertions aligned with the specified invariants. PORTA identifies 33 previously unreported security vulnerabilities in seven popular open-source brokers. We study these novel vulnerabilities and trace them to eight recurring patterns. We responsibly disclosed all discovered vulnerabilities: 29 have been confirmed, 14 patched, and 19 assigned CVE numbers, with 10 CVEs rated as critical.
