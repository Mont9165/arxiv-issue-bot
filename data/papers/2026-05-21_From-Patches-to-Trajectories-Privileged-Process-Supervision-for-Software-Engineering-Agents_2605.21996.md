# From Patches to Trajectories: Privileged Process Supervision for Software-Engineering Agents

- arXiv ID: `2605.21996v1`
- Authors: Murong Ma, Tianyu Chen, Yun Lin, Shuai Lu, Qinglin Zhu, Yeyun Gong, Zhiyong Huang, Peng Cheng, Yan Lu, Jin Song Dong
- Published: 2026-05-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.21996v1) | [pdf](https://arxiv.org/pdf/2605.21996v1)

## Abstract

Supervised fine-tuning (SFT) on long teacher trajectories is the dominant way to instill investigation and reasoning in open software-engineering (SWE) agents. Since every retained response becomes an imitation target, the student inherits the final outcome and intermediate flaws, including ungrounded leaps and redundant loops. High-quality training data must be effective(each step is grounded and narrows the agent's epistemic gap to the correct fix) and efficient(each step is information-bearing rather than redundant or looping). Existing recipes filter or relabel teacher rollouts using only a binary terminal verifier, which does not directly target these axes and provides no supervision on instances where the teacher fails.
  Most real issue includes a developer-authored reference patch, $p^\star$, revealing the file paths, runtime behaviors, and coding conventions presupposed by the correct fix, yet standard pipelines discard it. We propose Patches-to-Trajectories (P2T), which uses $p^\star$ as privileged information during curation and formulates trajectory construction as bi-objective optimization over per-step effectiveness and trajectory length. A reverse phase distills $p^\star$ into a latent process graph, $G^\star$, of contextual facts and solution milestones. A forward phase curates trajectories from blinded teacher continuations by scoring per-step progress against $G^\star$ under a leakage-blocking groundedness check and retaining the shortest effective segments.
  Using only 1.8k curated SWE-Gym instances, P2T improves effectiveness and efficiency over outcome-filtered SFT and its tool-error-masking variant. On SWE-bench Verified, it raises Pass@1 by up to 10.8 points while reducing per-instance inference cost by ~15%, with consistent gains on SWE-bench Lite. Size-matched ablations and qualitative analysis further isolate trajectory quality from data scale.
