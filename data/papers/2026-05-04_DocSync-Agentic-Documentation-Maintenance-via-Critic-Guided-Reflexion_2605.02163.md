# DocSync: Agentic Documentation Maintenance via Critic-Guided Reflexion

- arXiv ID: `2605.02163v1`
- Authors: Sidhesh Badrinarayan, Adithya Parthasarathy
- Published: 2026-05-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.02163v1) | [pdf](https://arxiv.org/pdf/2605.02163v1)

## Abstract

Software documentation frequently drifts from executable logic as codebases evolve, creating technical debt that degrades maintainability and causes downstream API misuse. While static analysis tools can detect the absence of documentation, they cannot evaluate its semantic consistency. Conversely, standard Large Language Models (LLMs) offer generative flexibility but frequently hallucinate when updating documentation without deep structural awareness of the underlying code. To address this gap, we propose DocSync, an agentic workflow that frames documentation maintenance as a structurally grounded, iterative generation task. DocSync bridges syntactic changes and natural language descriptions by fusing Abstract Syntax Tree (AST) representations and Retrieval-Augmented Generation (RAG) to provide dependency-aware context. Furthermore, to ensure factual consistency, we incorporate a critic-guided refinement loop based on the Reflexion paradigm, allowing the model to self-correct candidate updates against the source code. We empirically evaluate a resource-constrained implementation of DocSync-using a LoRA-adapted small language model - on a proxy code-to-text maintenance task. Our findings demonstrate that this AST-aware agentic approach substantially outperforms standard encoder-decoder baselines across semantic alignment, summary-line faithfulness, and automated judge preferences (e.g., achieving an automated judge score of 3.44/5.0 compared to 1.91 for CodeT5-base). Crucially, the iterative critic loop yields measurable improvements in semantic correctness without requiring scaled-up parameter counts. These results provide strong evidence that coupling structural retrieval with agentic refinement is a highly promising direction for autonomously mitigating documentation debt.
