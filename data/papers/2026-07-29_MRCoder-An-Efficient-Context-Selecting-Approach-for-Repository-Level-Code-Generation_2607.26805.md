# MRCoder: An Efficient Context Selecting Approach for Repository-Level Code Generation

- arXiv ID: `2607.26805v1`
- Authors: Peiding Wang, Li Zhang, Fang Liu
- Published: 2026-07-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.26805v1) | [pdf](https://arxiv.org/pdf/2607.26805v1)

## Abstract

Large language models (LLMs) have demonstrated strong capabilities in code generation. However, repository-level code generation remains challenging, as it requires effectively identifying and utilizing repository-specific context. While retrieval-augmented generation (RAG) incorporates relevant code snippets, it often introduces redundant context that interferes with the LLM's ability to utilize relevant information, leading to degraded generation quality and increased computational cost. Moreover, existing context selection and compression methods struggle to balance efficiency and quality, either introducing additional computational overhead or failing to effectively select valid context. In this paper, we propose MRCoder, an efficient context selection framework that improves both the effectiveness and efficiency of repository-level code generation. MRCoder adopts a Map-Reduce paradigm: in the Map Phase, a lightweight draft model generates drafts over partitioned contexts, and Structure-Aware Draft-Guided Selection (SADGS) selects informative contexts based on drafts through API consistency and logical similarity; in the Reduce Phase, the refined contexts are aggregated for final generation, with a parallel verification strategy further accelerating decoding. We evaluate MRCoder on two widely used repository-level code generation benchmarks, CoderEval and DevEval, using Qwen2.5-Coder and DeepSeek-Coder as backbone LLMs. Experimental results show that MRCoder improves code generation accuracy over strong baselines while reducing token consumption by 30 to 50% and inference time by up to 52%. These results demonstrate that our proposed structured and draft-guided context selection strategy is crucial for improving both the quality and efficiency of repository-level code generation
