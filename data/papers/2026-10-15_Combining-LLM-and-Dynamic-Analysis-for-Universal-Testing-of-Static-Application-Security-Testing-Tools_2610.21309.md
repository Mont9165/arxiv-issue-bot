# Combining LLM and Dynamic Analysis for Universal Testing of Static Application Security Testing Tools

- arXiv ID: `2610.21309v1`
- Authors: Huaien Zhang, Yu Pei, Hao Chen, Shin Hwei Tan
- Published: 2026-10-15
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.21309v1) | [pdf](https://arxiv.org/pdf/2610.21309v1)

## Abstract

Static application security testing (SAST) tools help detect potential software vulnerabilities, but they themselves contain faults undermining reliability and usability. Automated testing can address these issues, yet current techniques suffer from limited program transformation diversity and lack mechanisms to verify generated variants, leading to reduced fault detection and high manual effort. We present LLM4SAST, the first universal framework detecting faults in SAST tools using large language models and dynamic feedback. Our key insight is leveraging LLMs to understand and transform code in diverse programming languages. We design novel metamorphic relations with transformations to guide variant generation, using an LLM to produce multi-language variants that satisfy these relations. To reduce erroneous variants and identify unique faults, we propose two heuristics: dynamic-feedback-driven selection and program-differencing-based clustering. For each metamorphic relation, a report-centric test oracle detects variants that fail tests and identifies underlying faults by differentially analyzing SAST reports of the seed program and its variants. LLM4SAST identified 66 unique faults across six SAST tools, with 32 confirmed or fixed after being reported to developers, demonstrating effectiveness. The proposed heuristics eliminate 47.8% of false positives, and LLM4SAST detects 3.4 times more faults while requiring only 39.8% of the variants compared to existing approaches.
