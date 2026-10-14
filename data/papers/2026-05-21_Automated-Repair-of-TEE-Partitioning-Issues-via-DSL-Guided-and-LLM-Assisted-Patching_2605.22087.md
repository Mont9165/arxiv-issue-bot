# Automated Repair of TEE Partitioning Issues via DSL-Guided and LLM-Assisted Patching

- arXiv ID: `2605.22087v1`
- Authors: Chengyan Ma, Jieke Shi, Ruidong Han, Ye Liu, Feng Li, Yuqing Niu, David Lo
- Published: 2026-05-21
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2605.22087v1) | [pdf](https://arxiv.org/pdf/2605.22087v1)

## Abstract

Trusted Execution Environments (TEEs) provide hardware-based isolation to protect sensitive data and computations from potentially compromised operating systems (OS). However, TEE applications inevitably interact with the untrusted OS through SDK interfaces, and improper partitioning can introduce severe vulnerabilities such as data leakage and code injection. While prior work has proposed static analysis tools to detect such issues, automated repair remains largely unexplored. This problem is particularly challenging due to three TEE-specific factors: the lack of standardized secure development guidelines, the difficulty of extracting semantic information from low-level C code, and the absence of mature testing and validation methods. In this work, we present TEERepair, a framework for automatically repairing bad partitioning issues in TEE applications. Our approach tackles the above challenges by introducing a domain-specific language (DSL) to encode repair rules that express and capture common TEE security patterns, which are instantiated as patch templates with placeholders for context-specific variables. We then leverage large language models (LLMs) to reason about code semantics and synthesize context-aware patches, and further generate test clients to validate the repairs. We evaluate TEERepair on the TEE Partitioning Errors Benchmark (PartitioningE-Bench), achieving a significantly higher repair success rate of 87.6% compared to baselines. Furthermore, applying TEERepair to real-world TEE projects, we submitted 5 repair pull requests, 2 of which have been confirmed and merged by project maintainers.
