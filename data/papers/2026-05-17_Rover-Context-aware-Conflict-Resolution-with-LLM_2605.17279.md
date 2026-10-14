# Rover: Context-aware Conflict Resolution with LLM

- arXiv ID: `2605.17279v1`
- Authors: Qingyu Zhang, Junzhe Li, Jiayi Lin, Changhua Luo, Chenxiong Qian
- Published: 2026-05-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.17279v1) | [pdf](https://arxiv.org/pdf/2605.17279v1)

## Abstract

Code merging is a significant challenge, particularly in large-scale projects. Existing solutions, including program analysis and machine learning, show promise but face critical limitations. Program analysis lacks the ability to infer developers' intentions, relying on conservative strategies that offload unresolved conflicts for manual handling. Meanwhile, model-based approaches struggle with conflicts involving complex code dependencies due to insufficient contextual awareness. To address these gaps, we introduce Rover, a novel conflict resolution system that integrates program analysis with large language models (LLMs). To obtain context-aware prompts, we propose Multi-layer Code Property Graph (MtCPG), a new representation capturing inter-file dependencies and enabling contextual analysis for a given conflict. Using graph connectivity algorithms, Rover further clusters conflicting code and associated changes into meaningful "contexts" that guide the LLM in generating accurate resolutions. We compared Rover with standalone LLMs, machine learning baseline MergeGen, and suggestion provider tool WizardMerge with adjacent code as the contexts. Evaluation results show that Rover surpasses all of these approaches in terms of conflict resolution, achieving higher similarity to ground-truth resolutions at character, lexical, and semantic levels.
