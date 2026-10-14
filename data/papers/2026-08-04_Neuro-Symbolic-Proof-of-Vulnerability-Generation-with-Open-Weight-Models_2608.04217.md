# Neuro-Symbolic Proof-of-Vulnerability Generation with Open-Weight Models

- arXiv ID: `2608.04217v1`
- Authors: Yu Nong, Haipeng Cai
- Published: 2026-08-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.04217v1) | [pdf](https://arxiv.org/pdf/2608.04217v1)

## Abstract

Software vulnerabilities are persistent, but validating them remains difficult: a Proof-of-Vulnerability (PoV) requires a concrete input that triggers the vulnerable behavior, yet public triggering inputs are often unavailable for disclosed vulnerabilities. Existing techniques make different tradeoffs in effectiveness, scalability, cost, and controllability, leaving room for complementary designs. To complement them, we present POVGEN, a low-cost neuro-symbolic framework that makes PoV generation cost-effective via semantic focusing and LLM-guided constraint reasoning using open-weight models. POVGEN first localizes vulnerability-relevant regions (utilizing patch information if available), then performs path-sensitive reachability analysis, and finally generates PoVs by extracting and solving constraints with LLM-guided reasoning backed by an SMT solver. POVGEN successfully generates PoVs for 78.98% of vulnerabilities in a recent benchmark, outperforming fuzzing (up to 50.20%) and symbolic execution (2.45%). On 250 real-world CVEs without public PoVs, it generates valid PoVs for 74.80% of cases and reproduces 65.1% when without patch information. The fine-tuned open-weight models match frontier commercial LLMs on key sub-tasks (i.e., the core constraint-reasoning steps) while running locally at no per-sample API cost. Applying the generated PoVs revealed six flawed patches in disclosed CVEs (all subsequently fixed) and five previously unreported vulnerabilities (of which four have been confirmed and fixed by the developers).
