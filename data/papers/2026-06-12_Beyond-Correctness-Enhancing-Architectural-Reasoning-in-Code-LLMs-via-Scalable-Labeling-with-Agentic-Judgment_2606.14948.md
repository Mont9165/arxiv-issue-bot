# Beyond Correctness: Enhancing Architectural Reasoning in Code LLMs via Scalable Labeling with Agentic Judgment

- arXiv ID: `2606.14948v1`
- Authors: Kirill Vasilevski, Ximing Dong, Benjamin Rombaut, Ruochen Deng, Jiahuei Lin, Arthur Leung, Dayi Lin, Boyuan Chen, Shaowei Wang, Ahmed E. Hassan
- Published: 2026-06-12
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.14948v1) | [pdf](https://arxiv.org/pdf/2606.14948v1)

## Abstract

LLMs have substantially improved software engineering yet real-world development requires architectural understanding. Such understanding is prohibitively expensive to label manually and impossible to verify through tests alone. We propose an agentic judging pipeline using a strong LLM as a scalable proxy for expert architectural evaluation, comprising two judges: the Architecture Complexity Judge (ACJ), which estimates codebase-specific architectural understanding a task demands, and the Architecture Quality Judge (AQJ), which evaluates patch conformance to repository-specific architectural conventions via source-grounded rubrics. Fine-tuning Qwen3-8B/14B/32B on 3,360 curated instances achieves resolved rates of up to 27.2% on SWE-bench Verified - up to 540% over the base model and 256% over unfiltered fine-tuning. Meanwhile, the trained models achieve strong cross-language generalization and consistent improvements in architectural patch quality.
