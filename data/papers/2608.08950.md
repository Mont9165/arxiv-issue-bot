# Independent Patch Verification for Coding Agents with a Bidirectional Reconstruct-and-Verify Framework

- arXiv ID: `2608.08950v1`
- Authors: Chenglin Li, Yisen Xu, Zehao Wang, Shin Hwei Tan,  Tse-Hsun,  Chen
- Published: 2026-08-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.08950v1) | [pdf](https://arxiv.org/pdf/2608.08950v1)

## Abstract

Autonomous coding agents powered by large language models can now generate code patches directly from bug reports, but a fundamental gap remains: once a patch is produced, no mechanism independently verifies whether it truly resolves the reported problem. Prior work has sought to address this through iterative self-refinement and inference-time scaling, but these approaches either review the patch under the same interpretation that produced it or broaden candidate generation without verifying individual patches, and neither provides an explicit verification signal for assessing patch correctness. We propose RETRACE, a training-free post-generation verification framework that derives such a signal through bidirectional reconstruction and reconciliation. When a coding agent generates a candidate patch for an issue, RETRACE performs forward reconstruction to build an explicit repair rationale from the issue and the agent's trajectory; backward reconstruction then independently infers, from the patch and its trajectory alone and without access to the original issue, a description of the problem the patch appears to address, and compares this reconstruction against the original issue to produce an alignment verdict; a reconciliation stage then checks the consistency between the forward rationale and the patch, diagnoses the source of any misalignment, and either submits the patch or produces targeted revision guidance. Evaluated on SWE-bench Verified with two backbones (GPT-5-mini and MiniMax-2.5), RETRACE lifts Pass@1 by 7.0% and 3.6% respectively on the mini-SWE-agent scaffold, and delivers comparable gains on OpenHands without modification. Ablation experiments show that both the forward and backward stages contribute to the overall improvement and that adding reconciliation yields further gains.
