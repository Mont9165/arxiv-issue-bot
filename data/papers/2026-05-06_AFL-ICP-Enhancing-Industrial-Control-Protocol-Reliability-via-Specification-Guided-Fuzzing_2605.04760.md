# AFL-ICP: Enhancing Industrial Control Protocol Reliability via Specification-Guided Fuzzing

- arXiv ID: `2605.04760v1`
- Authors: Jiaying Meng, Xuewei Feng, Qi Li, Min Liu, Ke Xu
- Published: 2026-05-06
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.NI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.04760v1) | [pdf](https://arxiv.org/pdf/2605.04760v1)

## Abstract

Industrial Control Protocols (ICPs) are critical to the reliability and stability of industrial infrastructure, yet their security is fundamentally compromised by a specification-blindness bottleneck. Modern fuzzers, constrained by observation-driven inference, struggle to penetrate deep protocol states or detect subtle semantic deviations. In this paper, we present AFL-ICP, an autonomous fuzzing framework that pioneers a specification-driven paradigm. AFL-ICP features a context-aware specification formalization pipeline to transform complex specifications into rigorous machine-executable grammars. Building on this formalized specification, AFL-ICP leverages LLMs to enable automated protocol adaptation and seed generation, allowing for rapid extension to new protocols with minimal manual effort. Additionally, it includes an LLM-powered differential checker that cross-references implementation outputs with specification requirements to detect subtle semantic and logic bugs that existing fuzzers cannot detect. We implement AFL-ICP and evaluate it on four widely used ICPs, including both open-source and closed-source variants. Results show that AFL-ICP significantly outperforms state-of-the-art fuzzers in coverage and uncovers 24 previously unknown vulnerabilities, for which we have received acknowledgments from affected vendors (e.g., FreyrSCADA). Specifically, the identified vulnerabilities include 16 semantic and logic bugs that can silently disrupt industrial operations and degrade service availability.
