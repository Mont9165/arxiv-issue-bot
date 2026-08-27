# Vulnerable Code Search: Transferable Attack for Code Language Models

- arXiv ID: `2608.26031v1`
- Authors: Kaicheng Wang, Liyan Huang, Jesse Thomason, Weihang Wang
- Published: 2026-08-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2608.26031v1) | [pdf](https://arxiv.org/pdf/2608.26031v1)

## Abstract

Reliable code retrieval is crucial for developer productivity and effective code reuse. However, current neural code language models (CLMs) powering search tools are susceptible to adversarial attacks targeting non-functional textual elements. In this paper, we introduce a programming language-agnostic, transferable, adversarial attack that exploits this CLM vulnerability. Our approach perturbs identifiers within a code snippet without altering the snippet's functionality to artificially align the code with a target query. We demonstrate that our attack, even when computed using smaller code embedding models, such as CodeT5+, is highly effective and transferable to larger, closed-source embedding models, like Voyage-code-3, or LLMs like Gemini-3.1-Pro. Our attack can increase the similarity between the query and arbitrary, irrelevant code snippets, consequently degrading key retrieval metrics such as the Mean Reciprocal Rank (MRR) of state-of-the-art models by up to 77%. The experimental results highlight the fragility of current code search methods and underscore the need for more robust, semantic-aware approaches.
