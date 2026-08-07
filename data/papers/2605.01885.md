# QASecClaw: A Multi-Agent LLM Approach for False Positive Reduction in Static Application Security Testing

- arXiv ID: `2605.01885v1`
- Authors: Mohd Ruhul Ameen, Md Takrim Ul Alam, Akif Islam
- Published: 2026-05-03
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.01885v1) | [pdf](https://arxiv.org/pdf/2605.01885v1)

## Abstract

Static Application Security Testing tools help developers find security vulnerabilities before release, but they often produce many false positives. This increases manual review effort, reduces developer trust, and may cause real vulnerabilities to be ignored among noisy reports. We present QASecClaw, a multi agent approach that combines conventional Static Application Security Testing with coding specialized Large Language Model based contextual code review. A SAST engine first reports candidate vulnerabilities, and a Large Language Model based SAST Filter Agent then reviews each finding with source code context to decide whether it is likely to be a true positive or a false positive. QASecClaw is coordinated by a Mission Orchestrator and includes specialized agents for test planning, security validation, evidence correlation, filtering, and reporting. We evaluate QASecClaw on OWASP Benchmark v1.2, which contains 2,740 Java test cases across 11 Common Weakness Enumeration categories with ground truth labels. QASecClaw achieves an F1 score of 90.93 percent, compared with 78.39 percent for standalone Semgrep. The improvement is mainly driven by an 88.6 percent reduction in false positives, from 560 to 64, with only a 3.1 percent reduction in recall. These results show that Large Language Model augmented multi agent verification can make Static Application Security Testing output more accurate, useful, and trustworthy.
