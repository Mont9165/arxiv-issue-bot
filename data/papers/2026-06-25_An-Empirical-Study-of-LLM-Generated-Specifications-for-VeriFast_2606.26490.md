# An Empirical Study of LLM-Generated Specifications for VeriFast

- arXiv ID: `2606.26490v1`
- Authors: Wen Fan, Minh Tran, Sanya Dod, Xin Hu, Marilyn Rego, Danning Xie, Jenna DiVincenzo, Lin Tan
- Published: 2026-06-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LO`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2606.26490v1) | [pdf](https://arxiv.org/pdf/2606.26490v1)

## Abstract

Static verification tools can assure industrial scale software, but require significant human labor to write specifications. This is particularly true of static verifiers based on separation logic (SL verifiers), which excel at verifying heapmanipulating programs, but require many complex auxiliary specifications to reason about heap structure. Recent work applies large language models (LLMs) to generate code, tests, and proofs, including specifications for verifiers, but mostly targeting non-SL verifiers. To address this gap, this paper thoroughly evaluates how well LLMs perform when prompted to generate specifications for verifying 303 C functions with the SL verifier VeriFast. We explored eight prompting approaches, ten LLMs, and three input types in two stages. Quantitative and qualitative analyses are used to assess the LLM-generated code and specifications for functional behavior, verifiability and errors. The results show that LLMs preserve functional behavior in source code and specifications (both over 91%), but achieve modest verification success (31.4%). Using Gemini 2.5 Pro and providing formal contracts lead to higher success rates in our setting. Moreover, most errors (94%) come from LLMs' mistakes in the domainspecific knowledge of SL verifiers such as VeriFast. These findings provide guidance for optimizing LLM-generated specifications for SL verifiers.
