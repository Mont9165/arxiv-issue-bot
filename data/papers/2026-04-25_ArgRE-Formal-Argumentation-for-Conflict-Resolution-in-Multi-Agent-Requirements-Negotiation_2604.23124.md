# ArgRE: Formal Argumentation for Conflict Resolution in Multi-Agent Requirements Negotiation

- arXiv ID: `2604.23124v1`
- Authors: Haowei Cheng, Milhan Kim, Chong Liu, Teeradaj Racharak, Truong Vinh Truong Duy, Phan Thi Huyen Thanh, Jialong Li, Naoyasu Ubayashi, Hironori Washizaki
- Published: 2026-04-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.23124v1) | [pdf](https://arxiv.org/pdf/2604.23124v1)

## Abstract

As software systems grow in complexity, they must satisfy an increasing number of competing quality attributes, making it essential to balance them in a principled manner -- for example, a safety requirement for sensor-fusion verification may conflict with a tight planning-cycle budget. Multi-agent large language model frameworks support this balancing process by assigning specialized agents to different objectives. However, their conflict resolution is typically heuristic. Requirements are aggregated implicitly without explicit acceptance or rejection, limiting auditability in regulated domains. We present ArgRE, a multi-agent requirements negotiation system that embeds Dung-style abstract argumentation into the negotiation stage. Each proposal, critique, and refinement is modeled as an argument, conflicts are represented as directed attack relations, and the accepted set of arguments is computed under grounded and preferred semantics. The pipeline further integrates KAOS goal modeling, multi-layer verification, and standards-oriented artifact generation. Evaluation across five case studies spanning safety-critical, financial, and information-system domains shows that ArgRE provides argument-level traceability absent from existing frameworks. Independent evaluators rated its decision justifications significantly higher than those of heuristic synthesis (4.32 vs. 3.07, p < 0.001), indicating improved auditability, while semantic intent preservation remains comparable (94.9% BERTScore F1) and compliance coverage reaches 84.7% versus 47.6%--47.8% for baselines. Structural analysis further confirms that the default pairwise protocol yields acyclic graphs in which grounded and preferred semantics coincide, whereas cross-pair arbitration introduces controlled cyclicity, leading to predictable divergence between the two semantics.
