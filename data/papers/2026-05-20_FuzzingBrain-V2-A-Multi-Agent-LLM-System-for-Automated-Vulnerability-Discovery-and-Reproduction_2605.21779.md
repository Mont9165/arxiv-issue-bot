# FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction

- arXiv ID: `2605.21779v1`
- Authors: Ze Sheng, Zhicheng Chen, Qingxiao Xu, Kewen Zhu, Jeff Huang
- Published: 2026-05-20
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.21779v1) | [pdf](https://arxiv.org/pdf/2605.21779v1)

## Abstract

Software vulnerabilities pose critical security threats, with nearly 50,000 CVEs reported in 2025. While Large Language Models (LLMs) show promise for automated vulnerability detection, three key challenges remain. First, LLM-generated vulnerability reports suffer from high false positive rates and lack
  reproducible verification. Second, existing LLM-based approaches use suboptimal granularities for vulnerability localization: function-level analysis overlooks bugs when context becomes extensive, while line-level analysis lacks sufficient context. Third, existing approaches have difficulty reasoning about
  vulnerabilities with complex cross-function dependencies and triggering conditions.
  We present FuzzingBrain V2, a multi-agent system that addresses these gaps through four key contributions: (1) fully automated vulnerability analysis built on Google's OSS-Fuzz, ensuring all reported vulnerabilities are fuzzer-reproducible; (2) Suspicious Point, a novel control-flow-based abstraction for precise
  vulnerability localization at the optimal granularity; (3) logic-driven hierarchical function analysis with dual-layer fuzzing enhancing function coverage under resource constraints; (4) MCP-based static and dynamic analysis tools with context engineering enhancing complex vulnerability reasoning.
  On the AIxCC 2025 Final Competition C/C++ dataset, FuzzingBrain V2 achieved 90% detection rate (36 of 40 vulnerabilities). In real-world deployment, FuzzingBrain V2 discovered 29 zero-day vulnerabilities across 12 open-source projects, all confirmed and fixed by maintainers, with 2 assigned CVE IDs.
