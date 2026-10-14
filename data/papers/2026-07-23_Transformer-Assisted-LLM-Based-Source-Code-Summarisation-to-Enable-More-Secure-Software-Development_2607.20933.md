# Transformer-Assisted LLM-Based Source Code Summarisation: to Enable More Secure Software Development

- arXiv ID: `2607.20933v1`
- Authors: Jesse Phillips, Tracy Hall, Paul Rayson, Mo El-Haj
- Published: 2026-07-23
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2607.20933v1) | [pdf](https://arxiv.org/pdf/2607.20933v1)

## Abstract

Neural Source Code Summarisation (NSCS) aims to generate natural language summaries of source code to improve developers' and maintainers' understanding of code. Source code summaries are vital during the maintenance phase of the Secure Software Development Lifecycle (SSDLC), as they improve maintainers' understanding of code and help reduce the number of bugs and vulnerabilities in a software system. However, summaries are often missing, incomplete, or outdated in many software systems. Solutions to this problem use small, task-specific Transformer models or code-aware Large Language Models (LLMs). Task-specific Transformer-generated summaries often score well across many natural language generation (NLG) metrics, but these metrics reward lexical overlap rather than summary quality. Conversely, the ability of LLMs to capture semantics and produce high-quality summaries presents an exciting solution to this problem. This is especially relevant given the increased availability of LLMs and improvements in workstation hardware in recent years, which mean that some LLMs can now be run on developers' workstations. However, because of their abstractive nature, LLM-generated code summaries often differ greatly from developer-written summaries in the words and phrases they use, resulting in low scores across NLG metrics. We show how combining these two methods, by using Transformer-generated summaries in prompt engineering, may enable LLMs to create better source code summaries and help software practitioners maintain secure systems. We prompt four LLMs using four different prompts, with a task-specific Transformer used to assist the LLMs within the prompts. We present "Transformer-Assisted LLM-Based Source Code Summarisation", a method through which we observe an improvement of 7.8% in BLEU-4 and 5%.
