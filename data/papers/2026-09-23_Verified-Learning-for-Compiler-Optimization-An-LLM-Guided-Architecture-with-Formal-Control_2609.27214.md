# Verified Learning for Compiler Optimization: An LLM-Guided Architecture with Formal Control

- arXiv ID: `2609.27214v1`
- Authors: Dev Pratap Singh, Rong Feng, Suman Saha
- Published: 2026-09-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.27214v1) | [pdf](https://arxiv.org/pdf/2609.27214v1)

## Abstract

Compiler optimizations traditionally rely on handcrafted heuristics that often fail to generalize across programs and architectures. We investigate whether large language models can participate in compiler optimization through a verification-centered systems architecture that couples generative rewriting with formal equivalence checking. Using lazification in LLVM IR as a case study, we fine-tune a code-centric LLM on transformations produced by Wyvern and embed Alive2 into a feedback loop that enforces semantic preservation for every generated rewrite. Correctness is enforced externally as a runtime control layer rather than learned implicitly.
  During inference, candidate transformations are symbolically validated and regenerated when necessary, ensuring accepted rewrites satisfy formal constraints. On the LLVM test suite, the fine-tuned model reproduces core optimization behaviors while applying fewer transformations overall. Although Wyvern remains faster on most benchmarks, 9.8% achieve comparable or improved runtime under the learned system, with no semantic violations observed. Verification overhead remains bounded and convergence stable. These results demonstrate that generative AI components can be safely integrated into compiler pipelines through deterministic validation and structured feedback, offering a scalable architectural pattern for trustworthy AI-driven software infrastructure.
