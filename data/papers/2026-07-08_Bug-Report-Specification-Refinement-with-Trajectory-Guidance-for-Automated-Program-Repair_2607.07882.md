# Bug Report Specification Refinement with Trajectory Guidance for Automated Program Repair

- arXiv ID: `2607.07882v1`
- Authors: S M Farah Al Fahim, Md Nakhla Rafi, Md Ahasanuzzaman, Zeyang Ma, Dong Jae Kim, Shaowei Wang,  Tse-Hsun,  Chen
- Published: 2026-07-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.07882v1) | [pdf](https://arxiv.org/pdf/2607.07882v1)

## Abstract

Bug reports serve as task specifications for repository-level automated program repair (APR) agents, but they often describe only the observed failure and omit repair-relevant information such as the failure-inducing behavior, behavioral requirement, and implementation scope. As a result, a repair agent may inspect irrelevant code, infer an incorrect requirement, or generate a patch that addresses the reported symptom without restoring the intended repository behavior. We present TrajSpec, a trajectory-guided approach for repository-supported bug report specification refinement. Given an original report and a pre-fix repository, TrajSpec runs a trajectory-collection agent and uses the resulting unverified trajectory as a source of trajectory-derived specification evidence. It organizes this evidence into a three-level representation consisting of a high-level interpretation of the issue, diagnostic findings supporting that interpretation, and concrete repository observations. TrajSpec then generates a draft refined report and applies repository-based review to remove unsupported claims, revise uncertain claims, and add repository-supported details. We evaluate TrajSpec on all 300 SWE-Bench Lite instances using Mini-SWE-Agent V2. TrajSpec's refined reports improve Pass@1 from 41.00% to 59.67% with GPT-5-mini and from 54.67% to 64.33% with MiniMax M2.5. On a stratified sample of 100 instances, TrajSpec's refined reports also improve Pass@1 from 41.00% to 71.00% with Agentless and from 47.00% to 72.00% with AutoCodeRover. Ablation results show that removing repository-based review or the hierarchical evidence representation reduces Pass@1 from 59.67% to 48.00% and 47.67%, respectively. Overall, TrajSpec provides actionable repository-supported context that consistently improves repair performance.
