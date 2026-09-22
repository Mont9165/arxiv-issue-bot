# Evaluating the effectiveness of class-level LLM-generated test suites in Python

- arXiv ID: `2609.24341v1`
- Authors: Bilal Al-Ahmad, M. Harshvardhan, Khaled El-Fakih, Anas AlSobeh
- Published: 2026-09-21
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.24341v1) | [pdf](https://arxiv.org/pdf/2609.24341v1)

## Abstract

Context: Large language models (LLMs) can generate unit tests quickly, but high structural coverage does not establish that those tests execute reliably or detect faults. Existing evidence often treats coverage as the principal outcome and rarely compares prompt strategies and models through mutation testing at class level. Objective: This study examines how prompt strategy and model choice shape the executability, structural coverage, fault-detection effectiveness, and structural quality of LLM-generated Python test suites relative to human-written suites. Method: We evaluate multiple prompt strategies across a diverse set of current LLM configurations on the ClassEval benchmark. The evaluation combines execution outcomes, line and branch coverage, Cosmic Ray mutation scores, and structural quality indicators. Primary analyses treat successful execution as a prerequisite; paired comparisons use only classes shared by the relevant executable subsets. Results: Structural coverage is consistently near its ceiling and offers little discrimination among configurations. Executability varies substantially. The proposed prompt performs strongly for mutation score, but no prompt dominates across models. Model choice explains more variation than prompt choice, and their interaction shows that prompt effectiveness depends on the selected model. Human and LLM suites are evaluated on unequal executable subsets, so their relative mutation scores do not establish superiority. Conclusion: Reliable assessment of LLM-generated tests should treat executability as a gate and combine coverage with mutation testing and structural quality indicators. In practice, model selection should precede prompt tuning.
