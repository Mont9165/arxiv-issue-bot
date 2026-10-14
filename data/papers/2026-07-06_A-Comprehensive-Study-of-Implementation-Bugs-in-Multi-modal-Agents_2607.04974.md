# A Comprehensive Study of Implementation Bugs in Multi-modal Agents

- arXiv ID: `2607.04974v1`
- Authors: Suwan Li, Lei Bu, Shangqing Liu, Yile Wang, Guangdong Bai, Fuman Xie, Kai Chen, Chang Yue
- Published: 2026-07-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.04974v1) | [pdf](https://arxiv.org/pdf/2607.04974v1)

## Abstract

Multi-Modal Agents (M-agents), empowered by Large Language Models (LLMs), excel in various complex, open-world scenarios such as autonomous driving and robotics. However, their unique requirements to interact with dynamic and diverse multi-modal environments introduce novel implementation challenges beyond those faced by traditional agents. Outdated perception, untrustworthy planning and inapplicable execution could cause traffic accident and financial loss. Despite growing study on agent issues, there has not been a systematic study focusing on M-agent-specific implementation bugs. To address this gap, we conducted the first systematic study of implementation bugs in M-agents. We collected 34 representative M-agents from diverse sources and, through meticulous filtering,identified 158 M-agent-specific bugs from 1,268 issue reports. Using a top-down strategy, we developed a comprehensive taxonomy that classifies bugs by global symptoms, functionality component-level symptoms, and root causes. We then implemented MATester, an automatic proof-of-concept bug identifier by analyzing runtime inter-component outputs. When applied to 12 extra M-agents, MATester successfully covered 61.4% of known open issues and discovered 31 additional bugs, demonstrating the practical usefulness of our study. Our work provides a comprehensive reference and guideline for classification, prevention and fix of M-agent bugs.
