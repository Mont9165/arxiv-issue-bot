# DPC: Training-Free Text-to-SQL Candidate Selection via Dual-Paradigm Consistency

- arXiv ID: `2604.15163v2`
- Authors: Boyan Li, Ou Ocean Kun Hei, Yue Yu, Yuyu Luo
- Published: 2026-04-16
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2604.15163v2) | [pdf](https://arxiv.org/pdf/2604.15163v2)

## Abstract

While Large Language Models (LLMs) demonstrate impressive proficiency in generating SQL queries, they fundamentally lack the capability to self-evaluate correctness without an execution oracle. This limitation creates a stark Generation-Selection Gap, where high potential accuracy (Pass@K) fails to translate into execution accuracy (Pass@1). Although supervised verifiers offer mitigation, they incur prohibitive annotation costs and suffer from domain fragility. Consequently, recent research has pivoted to the training-free setting. However, existing methods--such as Self-Consistency or LLM-as-a-Judge--remain hampered by systematic bias (consensus on hallucinations) and symbolic blindness (inability to simulate execution states). We introduce DPC (Dual-Paradigm Consistency), a multi-agent framework that reformulates SQL selection from a probabilistic guessing task on hidden data into a deterministic verification task on visible data. Specifically, DPC employs a SLICER and a TESTER agent to collaboratively construct a Minimal Distinguishing Database (MDD)--an adversarial, fully observable micro-environment engineered to expose logical discrepancies between candidates. To break the self-correction bias, a SOLVER agent then verifies the SQL candidates by cross-referencing their execution against a parallel Python/Pandas solution. By validating execution consistency between declarative (SQL) and imperative (Python) paradigms, DPC robustly discriminates correct logic from systematic hallucinations. Experiments on BIRD and Spider across multiple LLMs demonstrate that our method consistently outperforms existing selection baselines, achieving absolute accuracy improvements of up to 2.2% over strong competitors like Self-Consistency.
