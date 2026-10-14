# Stage-Supervised Latent Reasoning for Single-Shot JavaScript Deobfuscation

- arXiv ID: `2609.27058v1`
- Authors: Rong Feng, Suman Saha
- Published: 2026-09-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.27058v1) | [pdf](https://arxiv.org/pdf/2609.27058v1)

## Abstract

JavaScript obfuscation is widely used to protect code, but it also makes program analysis and security review substantially harder. Existing LLM-based deobfuscation methods usually treat the task as one-step translation, ignoring the staged structure of practical deobfuscation pipelines. This WIP paper proposes a stage-aware latent reasoning framework that converts intermediate outputs from a deterministic deobfuscation tool into supervision for Coconut-based training. The model learns from multi-stage rewrites during training but generates the final cleaned program in a single shot at inference time. Preliminary results on JsDeObsBench show that the Coconut-based model improves syntactic validity to 50%, compared with 15% for direct fine-tuning and 25% for a zero-shot baseline, and reaches 80% semantic correctness among valid outputs, indicating better semantic faithfulness than either comparison model in deobfuscation.
