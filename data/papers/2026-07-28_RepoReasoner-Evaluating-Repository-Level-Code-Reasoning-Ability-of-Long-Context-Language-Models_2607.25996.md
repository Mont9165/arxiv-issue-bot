# RepoReasoner: Evaluating Repository-Level Code Reasoning Ability of Long-Context Language Models

- arXiv ID: `2607.25996v1`
- Authors: Yanlin Wang, Suiquan Wang, Yanli Wang, Bowen Zhang, Daya Guo, Jiachi Chen, Zibin Zheng
- Published: 2026-07-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.25996v1) | [pdf](https://arxiv.org/pdf/2607.25996v1)

## Abstract

Recent large language models (LLMs) have shown strong performance on software engineering tasks, yet most existing benchmarks evaluate code reasoning at the function level, where all relevant information is localized. This setting fails to reflect real-world development, which requires reasoning across multiple files and complex dependency structures. We introduce RepoReasoner, a benchmark for evaluating repository-level code reasoning. It assesses two complementary abilities: Output Prediction, which measures fine-grained, stateful execution reasoning across files, and Call Chain Prediction, which evaluates high-level architectural dependency understanding under noisy context. Our benchmark is constructed through a multi-stage pipeline that leverages dynamic tracing of pytest executions to obtain ground-truth call chains, along with LLM-based I/O rewriting to reduce memorization effects. We evaluate seven state-of-the-art LLMs. Even under oracle context, the best-performing model achieves only 69.1% Pass@1 on Output Prediction, indicating that cross-file reasoning remains a major challenge. In Call Chain Prediction, models exhibit high precision but low recall, suggesting limited multi-hop dependency understanding. Furthermore, performance drops on rewritten data reveal partial reliance on memorization, and longer contexts do not consistently improve results due to noise. These findings highlight fundamental limitations in current LLMs' repository-level reasoning and motivate future work on structured architectural understanding and cross-file inference.
