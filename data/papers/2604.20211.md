# Towards Secure Logging: Characterizing and Benchmarking Logging Code Security Issues with LLMs

- arXiv ID: `2604.20211v1`
- Authors: He Yang Yuan, Xin Wang, Kundi Yao, An Ran Chen, Zishuo Ding, Zhenhao Li
- Published: 2026-04-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2604.20211v1) | [pdf](https://arxiv.org/pdf/2604.20211v1)

## Abstract

Logging code plays an important role in software systems by recording key events and behaviors, which are essential for debugging and monitoring. However, insecure logging practices can inadvertently expose sensitive information or enable attacks such as log injection, posing serious threats to system security and privacy. Prior research has examined general defects in logging code, but systematic analysis of logging code security issues remains limited, particularly in leveraging LLMs for detection and repair. In this paper, we derive a comprehensive taxonomy of logging code security issues, encompassing four common issue categories and 10 corresponding patterns. We further construct a benchmark dataset with 101 real-world logging security issue reports that have been manually reviewed and annotated. We then propose an automated framework that incorporates various contextual knowledge to evaluate LLMs' capabilities in detecting and repairing logging security issues. Our experimental results reveal a notable disparity in performance: while LLMs are moderately effective at detecting security issues (e.g., the accuracy ranges from 12.9% to 52.5% on average), they face noticeable challenges in reliably generating correct code repairs. We also find that the issue description alone improves the LLMs' detection accuracy more than the security pattern explanation or a combination of both. Overall, our findings provide actionable insights for practitioners and highlight the potential and limitations of current LLMs for secure logging.
