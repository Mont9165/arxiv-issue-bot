# From Business Requirements to Test Assertions: Evaluating LLM-Generated Oracles on Real Bugs

- arXiv ID: `2607.10277v1`
- Authors: Tiancheng Ma, Nasir U. Eisty
- Published: 2026-07-11
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.10277v1) | [pdf](https://arxiv.org/pdf/2607.10277v1)

## Abstract

The oracle problem (determining the correct expected outcome for a test) remains a major bottleneck in automated testing, and is increasingly relevant as non-experts rely on AI-generated code they cannot reliably validate. We study whether large language models (LLMs) can generate generalizable test oracles directly from natural-language business requirements, without access to source code or example input-output pairs. We propose a reproducible, requirement-driven pipeline grounded in Defects4J. For each of 10 real bugs from Defects4J Lang (Bugs 1 and 3-11), we (i) extract behavioral changes via buggy/fixed diffs, (ii) manually translate the change into a business requirement, (iii) construct a requirement-derived oracle (REQ) as a gold standard, and (iv) prompt five LLMs (DeepSeek-V3, Gemma-3n, Llama-3, Mistral-7B, and Qwen-3) to generate Java oracle code. We evaluate oracle correctness and generalization under two targets: agreement with REQ and agreement with the system under test (SUT), reporting macro-averaged accuracy, precision, recall, and F1. LLMs achieve non-trivial generalization but with substantial bug- and model-level variance. Generated oracles align more closely with REQ than with SUT, and correlations between requirement technicality/ambiguity ratings and oracle accuracy are weak with wide confidence intervals. No detectable linear relationship exists between requirement properties and oracle accuracy in this dataset, suggesting that pretraining coverage and the semantic specificity of the required behavior dominate oracle correctness. As a pilot proof of concept, these findings are preliminary and are intended to establish feasibility and motivate larger-scale empirical investigation.
