# CodeEvolve: LLM-Driven Evolutionary Optimization with Runtime-Enriched Target Selection for Multi-Language Code Enhancement

- arXiv ID: `2605.04677v1`
- Authors: Ajay Krishna Borra, Wenzhuo Yang, Samarth Arora, Akhilesh Deepak Gotmare, Gokulakrishnan Gopalakrishnan, Tharun Gali, Madhav Rathi, Doyen Sahoo, Manpreet Singh, Mayuresh Verma, Laksh Venka, Shuchita Singh
- Published: 2026-05-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.04677v1) | [pdf](https://arxiv.org/pdf/2605.04677v1)

## Abstract

We present CodeEvolve, an evolutionary framework for improving program performance and code quality with Large Language Models (LLMs). CodeEvolve extends OpenEvolve with runtime-guided target selection, Monte Carlo Tree Search (MCTS), automated code refinement, and language-specific evaluation pipelines for Java and Salesforce Apex. The system uses Java Flight Recorder (JFR) profiles to build weighted component graphs and select optimization targets that account for most execution cost, reducing reliance on manual bottleneck identification. For each target, CodeEvolve generates candidate edits, evaluates them through build validation, unit tests, performance checks, static analysis, and LLM-based review, and retains only variants that preserve functional correctness. Across real-world optimization tasks, CodeEvolve improves performance and code metrics while maintaining correctness. On a large enterprise Java codebase, it achieves an average speedup of 15.22$\times$ across seven hotspot functions and outperforms single-pass LLM optimization on five of them. An ablation study on Apex optimization shows that the full MCTS-augmented configuration produces 19.5 valid programs out of 20 on average, indicating that search, filtering, and refinement each contribute to more reliable optimization.
