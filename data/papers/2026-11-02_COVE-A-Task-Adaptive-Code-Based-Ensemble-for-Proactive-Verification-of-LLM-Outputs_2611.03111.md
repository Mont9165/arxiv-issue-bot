# COVE: A Task-Adaptive, Code-Based Ensemble for Proactive Verification of LLM Outputs

- arXiv ID: `2611.03111v1`
- Authors: Anjaney Shrivastava, Dharmala Hrudai Aditya
- Published: 2026-11-02
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.03111v1) | [pdf](https://arxiv.org/pdf/2611.03111v1)

## Abstract

Large Language Models (LLMs) are now embedded in enterprise workflows, yet their outputs remain prone to hallucinations: plausible-sounding but factually incorrect or malformed content. Most verification approaches are reactive, detecting errors only after generation and often spending additional expensive LLM calls to do so. We present COVE, a task-adaptive, code-based ensemble that takes the opposite stance: it prevents errors before generation and validates structure and consistency afterwards using six deterministic, pure-Python innovations that add no extra LLM calls. On an internal evaluation spanning 11 text datasets (1,020 examples) and 4 image datasets (200 examples), COVE lifts text accuracy from a 45.2% unverified baseline to 82.1% (an 81.7% relative improvement), improves image accuracy by 69.5%, and reduces token usage by 48 to 96% (simulated cost model), at a measured verification overhead of 0.26 ms per output (excluding the LLM call). This article describes the engineering design of each innovation (with pseudocode and the exact parameters we use), the measured impact, an ablation of every component, and the practical lessons learned from deploying code-based verification in enterprise pipelines.
