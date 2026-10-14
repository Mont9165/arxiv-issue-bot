# Complexity-Aware Evaluation of LLM Comprehension

- arXiv ID: `2609.37405v1`
- Authors: Ali Mohammadi Esfahani, Nafiseh Kahani, Samuel A. Ajila
- Published: 2026-09-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.37405v1) | [pdf](https://arxiv.org/pdf/2609.37405v1)

## Abstract

Large language models (LLMs) are increasingly used for software engineering tasks that require understanding existing source code, including behavior prediction, function explanation, debugging, and code review. However, aggregate benchmark accuracy can conceal how model reliability changes as source code becomes structurally more complex. This paper presents a complexity-aware framework for evaluating LLM code comprehension using cyclomatic complexity, nesting depth, branching factor, and Halstead volume. We evaluate DeepSeek-Coder-V2 and Llama through two complementary tasks: automatic input-output prediction over 300 Python functions and manually assessed semantic comprehension over a balanced subset of 60 functions. The functions are grouped into Low-, Medium-, and High-complexity bands. DeepSeek-Coder-V2 achieves an overall automatic accuracy of 78.33%, compared with 70.33% for Llama. However, accuracy decreases substantially from Low to High complexity, from 93.52% to 52.78% for DeepSeek-Coder-V2 and from 87.04% to 47.22% for Llama. Incorrect predictions are consistently associated with higher values of all four complexity metrics, and correlation and logistic-regression analyses confirm broadly comparable negative associations between structural complexity and correctness. Manual semantic comprehension shows the same degradation pattern, with accuracy decreasing from 100.00% to 75.00% for DeepSeek-Coder-V2 and from 90.00% to 60.00% for Llama. These findings demonstrate that complexity-aware evaluation provides a more diagnostic assessment of LLM code-comprehension reliability than aggregate accuracy alone.
