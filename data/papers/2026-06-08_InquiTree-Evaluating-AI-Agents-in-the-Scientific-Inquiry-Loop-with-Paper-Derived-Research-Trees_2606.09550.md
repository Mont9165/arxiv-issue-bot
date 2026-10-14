# InquiTree: Evaluating AI Agents in the Scientific Inquiry Loop with Paper-Derived Research Trees

- arXiv ID: `2606.09550v1`
- Authors: Shaoyang Cui
- Published: 2026-06-08
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.09550v1) | [pdf](https://arxiv.org/pdf/2606.09550v1)

## Abstract

While LLM-based agents are increasingly used in scientific workflows, it remains unclear whether they are truly qualified for the dynamic and uncertain process of discovery. Existing static evaluations often conflate genuine reasoning with rote memorization. We introduce InquiTree, a diagnostic environment that formalizes scientific inquiry as interactive Research Trees: directed acyclic graphs capturing the logical dependencies among hypothesis formulation, study design, result interpretation, and belief updating. Evaluating agents on a 30-paper test pool and releasing the open-access InquidTree-18(IT-18) subset, we identify two key limitations. First, agents exhibit an "Erosion of Marginal Capabilities": during long-horizon interactions, they develop "cognitive tunneling," where critical judgment and anomaly detection degrade relative to their intrinsic baselines. Second, performance drops on papers published after model training cutoffs, revealing a boundary between interpolation and extrapolation and suggesting that apparent competence is partly driven by parametric memory. These findings indicate that scaling context alone is insufficient for reliable AI scientists; stronger architectures or human oversight may be required to preserve critical evaluation and generalization.
