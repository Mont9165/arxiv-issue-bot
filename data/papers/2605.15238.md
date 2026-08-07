# Hydra: Efficient, Correct Code Generation via Checkpoint-and-Rollback Support

- arXiv ID: `2605.15238v1`
- Authors: Alexander Du, Jianjun Ou, Danyang Zhuo, Matthew Lentz
- Published: 2026-05-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2605.15238v1) | [pdf](https://arxiv.org/pdf/2605.15238v1)

## Abstract

Large language models are increasingly used for code generation, but many generated programs fail to compile, a prerequisite for further correctness checks such as unit tests. Existing solutions for repairing static errors are costly in both latency and token consumption. Post-hoc repair delays error detection until generation completes and commonly regenerates large regions of previously valid code. Constrained semantic decoding checks after each token, incurring per-token overhead while limiting repair to the current token even when the root cause lies earlier.
  We present Hydra, a system for efficient recovery from static errors during code generation. Hydra allows checking to proceed asynchronously with generation, avoiding checker overhead when the generated code is semantically correct. In addition, it provides checkpoint-and-rollback support for targeted repair, avoiding regeneration and rechecking of valid prefixes. We retrofit the Clang C/C++ compiler to support Hydra with modest modifications. Paired with a token-efficient repair strategy, Hydra reduces latency by up to 71% and token consumption by up to 70% relative to post-hoc repair on C/C++ code generation tasks that encounter static errors.
