# Inferring Code Correctness from Specification

- arXiv ID: `2605.29822v1`
- Authors: Tambon Florian, Papadakis Mike
- Published: 2026-05-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.29822v1) | [pdf](https://arxiv.org/pdf/2605.29822v1)

## Abstract

Large language models (LLMs) have become integral to modern software development, enabling automated code generation at scale. However, validating the correctness of LLM-generated code remains a critical and largely unsolved challenge. Existing approaches either rely on dynamic consensus across multiple code candidates - making them costly and difficult to scale - or on static reasoning that is susceptible to dynamic bugs and order bias. In this paper, we propose TRAILS~ (Targeted Reasoning Agreement via Inputs and Specifications), an approach that grounds LLM reasoning with concrete (input, output) pairs. TRAILS~ first generates diverse test inputs via category partitioning based on the specification, then executes them against the candidate code and prompts LLMs to assess whether the resulting input-output pairs conform to the specification - without ever reasoning over the code itself. Scores are aggregated across inputs, to determines whether the program is likely correct. We evaluate TRAILS~ on two datasets, LiveCodeBench and CoCoClaNeL, across three LLMs (Qwen3Coder-30B, Devstral-Small-24B, and Olmo3.1-Instruct), comparing against HoarePrompt and a Zero-Shot Chain-of-Thought baseline. TRAILS~ improves Matthew Correlation Coefficient by up to 39\% relative to Zero-Shot COT and consistently outperforms HoarePrompt. Beyond accuracy, TRAILS~ demonstrates greater stability across seeded runs, reducing sensitivity to LLM non-determinism, and assigns correct labels to a larger set of unique code samples than competing approaches.
