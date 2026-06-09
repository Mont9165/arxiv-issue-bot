# Data Agents Under Attack: Vulnerabilities in LLM-Driven Analytical Systems

- arXiv ID: `2606.08661v1`
- Authors: Kuncan Wang, Ziting Wang, Peizhuo Lv, Haoyang Li, Guoliang Li, Gao Cong, Wei Dong
- Published: 2026-06-07
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.08661v1) | [pdf](https://arxiv.org/pdf/2606.08661v1)

## Abstract

Data agents integrate LLM-driven reasoning with relational data access, executable analytical tools, and multi-step workflow orchestration, making them increasingly central to enterprise analytics. This integration introduces new security vulnerabilities across data resources, database execution, and agent reasoning, recombining concerns from database security and general-purpose LLM-agent security into failure modes that neither line of work captures on its own. To address this gap, we present a systematic security study of data agents. Our contributions are threefold. First, we develop a layered vulnerability framework that identifies eight data agent-specific risks across interpretation, execution, and policy layers. Second, we introduce an attack taxonomy organized by adversary goal, tactic, and technique, covering three goals, seven tactics, and fourteen techniques, and pair it with an LLM-driven payload generation pipeline grounded in real database schemas. Third, we evaluate these attacks on six systems, including four open-source data agents and two production cloud analytics services. Our experiments reveal substantial security vulnerabilities across current systems and yield four key takeaways.
