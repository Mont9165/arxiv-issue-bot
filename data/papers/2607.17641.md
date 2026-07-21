# Verify, Repair, Repeat, or Stop? Robust Stopping for Noisy Verify-Repair Loops in LLM Agents

- arXiv ID: `2607.17641v1`
- Authors: Yitao Wu, Si Shen, Rui Yang, Hong Peng, Bin Hu
- Published: 2026-07-20
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.17641v1) | [pdf](https://arxiv.org/pdf/2607.17641v1)

## Abstract

Verify-repair loops are a standard means for large language model (LLM) agents to correct faulty plans in code generation, mathematical reasoning, and tool use. When both the verifier and the repairer are noisy, repair can damage already-correct plans, and reported acceptance keeps rising while true validity falls, so existing methods lack a principled basis for deciding when repair should stop. We propose VRR-Stop, a robust stopping framework for noisy verify-repair-repeat (VRR) loops. A four-parameter noise model separates verifier false acceptance and false rejection from the repair and damage behavior of the repairer. Belief filtering turns repeated verification votes into an estimate of committed validity, and the loop commits or repairs according to the sign of the true marginal gain, which requires only sign identifiability rather than accurate recovery of all parameters. When verifier discrimination approaches zero, calibration itself fails and estimation error can flip the stopping sign, so we pair VRR-Stop with VRR-Guard, an estimation-free fallback that replaces the incumbent candidate only under a sufficient verification margin. On a GSM8K stress setting, VRR-Stop improves final true validity by 60.6 percentage points over fixed five-round repair at an average cost of 0.72 repair rounds. Across settings, stopping reliability is governed jointly by verifier discrimination and the decision margin rather than by the absolute size of estimation error.
