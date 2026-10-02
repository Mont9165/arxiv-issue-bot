# Understanding and Mitigating Library-Related Issues in LLM-Generated Code

- arXiv ID: `2610.00622v1`
- Authors: Yacine Majdoub, Rinad Hamid, Eya Ben Charrada, Ahmad Abdellatif, Haifa Touati
- Published: 2026-09-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.00622v1) | [pdf](https://arxiv.org/pdf/2610.00622v1)

## Abstract

Software practitioners increasingly rely on Large Language Models (LLMs) to generate code that integrates external libraries. However, LLMs often produce incorrect library usage, such as invalid imports, outdated API calls, and hallucinated dependencies, leading to compilation or runtime failures that reduce the reliability of AI-assisted software development. In this paper, we propose an agentic approach to mitigate libraryrelated errors in LLM-generated code. More specifically, we first conduct an exploratory study to characterize the library-related issues produced by LLMs. Our analysis of 100 LLM-generated code files reveals that 84% of generated files contain at least one library-related error, with recurring patterns including incorrect import paths, missing imports, hallucinated libraries, deprecated library usage, and unused imports. Based on these findings, we design an agentic approach that integrates task analysis, documentation grounding, code generation, and automated validation to improve library usage during code synthesis. We evaluate our approach on 300 code generation tasks derived from realworld implementations of rapidly evolving Python frameworks, including LangChain and AutoGen, across five LLMs: GPT-5, DeepSeek-V3, Qwen3, Mistral, and Llama 3. The results show that our approach consistently improves code generation quality across all evaluated models, reducing library-related errors by 38.1% - 54.6% and increasing code correctness by up to 16%.
