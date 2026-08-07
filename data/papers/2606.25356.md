# Representation Matters: An Empirical Study of Program Representations for LLM Vulnerability Reasoning

- arXiv ID: `2606.25356v1`
- Authors: Andrew Stoltman, Johnathan Tang, Haipeng Cai
- Published: 2026-06-24
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.25356v1) | [pdf](https://arxiv.org/pdf/2606.25356v1)

## Abstract

Large Language Models (LLMs) are increasingly used for automated vulnerability detection, but it remains unclear how program structure and semantics should be represented for LLM-based reasoning. Most prompting-based approaches provide raw source code, implicitly assuming that more source-level context gives the model better evidence. This paper challenges that assumption through RepBench, an empirical benchmark comparing raw source code with static-analysis-based program representations. RepBench converts real-world C/C++ vulnerability testcases into multiple representations: raw source, Abstract Syntax Trees (ASTs), Control-Flow Graphs (CFGs), Program Dependence Graphs (PDGs), their combinations, and an auxiliary track of enriched PDGs (ePDGs). Using a curated PrimeVul-derived corpus of 107 Joern-based testcases across five CWE categories, we evaluate ten representation variants under a fixed Chain-of-Thought and structured-output protocol, plus 19 additional ePDG cases generated through VulChecker/Hector. Representation choice substantially affects LLM vulnerability reasoning. The strongest variant, AST+PDG, achieves 83.2% accuracy, compared with 53.5% for raw source. At the family level, graph-only prompts outperform both source-only and source-plus-graph prompts while requiring far less prompt overhead. These results reveal a context dilution effect: adding raw source code to compact structural graph evidence can degrade reasoning by making vulnerability-relevant evidence less salient. Overall, our findings show that carefully selected structural representations offer a better accuracy-overhead tradeoff than simply giving LLMs more raw input, and suggest that static analysis can serve as an effective prompt-construction layer for security-focused LLM reasoning.
