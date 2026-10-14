# Path2Spec: Path-Aware Specification Generation via Large Language Models

- arXiv ID: `2609.33438v1`
- Authors: Dan Huang, Zhensu Sun, Huihui Huang, Jinfeng Jiang, Xiaofei Xie, Yintong Huo, David Lo
- Published: 2026-09-27
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.33438v1) | [pdf](https://arxiv.org/pdf/2609.33438v1)

## Abstract

Formal specifications are critical for program verification, comprehension, and maintenance. However, manually writing them is costly and difficult to scale. Recent studies have shown that Large Language Models (LLMs) are promising for automated specification generation, but existing methods suffer from quality issues. We analyze a state-of-the-art approach and find that at least 34.6% of successfully verified specifications actually fail to meaningfully capture the program's distinct behavior, which is a quality issue not captured by metrics that only measure verification success. We further found that a major factor contributing to such hidden quality issues stems from the design of existing methods: these methods treat a program as a single unit, resulting in overly general, coarse-grained constraints. To this end, we introduce Path2Spec, a divide-and-conquer framework that addresses these limitations through systematic path-based reasoning. Path2Spec leverages LLMs to extract all execution paths from an input program, generates path-specific specifications for each, and merges them into a comprehensive overall specification. For complex programs where path-based generation struggles, Path2Spec employs a decompose-then-retry strategy that recursively breaks a program into smaller subprograms based on logical branches, generates specifications for each, and merges them back. We evaluate Path2Spec on two public benchmarks: SG-Bench (120 programs) and SV-COMP (265 programs). Results show that Path2Spec can outperform the state-of-the-art baseline SpecGen: 87.5% versus 66.7% on SG-Bench, and 83.0% versus 44.2% on SV-COMP. Human evaluation further validates that Path2Spec generates higher-quality specifications with precise semantic alignment to the code.
