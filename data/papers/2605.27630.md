# OptiLoop: Coordination-in-the-Loop Verification and Repair for LLM-Generated Optimization Agents

- arXiv ID: `2605.27630v1`
- Authors: Yujia Xu, Zhiheng Wang, Thi Dinh
- Published: 2026-05-26
- Primary category: `math.OC`
- Categories: `math.OC`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.27630v1) | [pdf](https://arxiv.org/pdf/2605.27630v1)

## Abstract

Many decentralized decision problems require multiple parties to coordinate on shared decisions while keeping objectives, constraints, and data private. Large language models (LLMs) offer a promising way to lower the barrier to participation by generating local optimization agents from natural-language specifications. In coordination settings, however, executability is not enough: a generated agent may compile, solve, and pass local checks while still being semantically wrong, for example by misrepresenting costs, mis-scoping constraints, or responding incorrectly to incentives. Such errors often surface only during coordination, as systematic behavioral failures rather than infeasibility. We propose coordination-in-the-loop verification and repair for LLM-generated optimization agents. We instantiate this idea with an Alternating Direction Method of Multipliers (ADMM)-style consensus protocol and introduce OptiLoop, a pipeline that generates local optimization agents from text, verifies them through short, bounded coordination runs against a fixed reference counterparty, extracts structured behavioral and static evidence, and applies evidence-driven repair. When failures are structural rather than implementational, OptiLoop escalates from localized code fixes to corrected-formulation repair, and it can additionally reuse episodic lessons from prior instances. On 40 held-out test scenarios, OptiLoop-Full improves objective match from 66.0% to 93.0% and social match from 68.5% to 89.0% relative to a strong local-validation baseline, while reducing mean objective gap from 15.3% to 3.5% and mean social gap from 7.6% to 2.0%. These results show that, for generated optimization agents deployed inside decentralized decision loops, correctness should be validated in the loop itself rather than through isolated execution alone.
