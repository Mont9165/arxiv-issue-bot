# Strategic Heterogeneous Multi-Agent Architecture for Cost-Effective Code Vulnerability Detection

- arXiv ID: `2604.21282v1`
- Authors: Zhaohui Geoffrey Wang
- Published: 2026-04-23
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.21282v1) | [pdf](https://arxiv.org/pdf/2604.21282v1)

## Abstract

Automated code vulnerability detection is critical for software security, yet existing approaches face a fundamental trade-off between detection accuracy and computational cost. We propose a heterogeneous multi-agent architecture inspired by game-theoretic principles, combining cloud-based LLM experts with a local lightweight verifier. Our "3+1" architecture deploys three cloud-based expert agents (DeepSeek-V3) that analyze code from complementary perspectives - code structure, security patterns, and debugging logic - in parallel, while a local verifier (Qwen3-8B) performs adversarial validation at zero marginal cost.
  We formalize this design through a two-layer game framework: (1) a cooperative game among experts capturing super-additive value from diverse perspectives, and (2) an adversarial verification game modeling quality assurance incentives.
  Experiments on 262 real samples from the NIST Juliet Test Suite across 14 CWE types, with balanced vulnerable and benign classes, demonstrate that our approach achieves a 77.2% F1 score with 62.9% precision and 100% recall at $0.002 per sample - outperforming both a single-expert LLM baseline (F1 71.4%) and Cppcheck static analysis (MCC 0). The adversarial verifier significantly improves precision (+10.3 percentage points, p < 1e-6, McNemar's test) by filtering false positives, while parallel execution achieves a 3.0x speedup.
  Our work demonstrates that game-theoretic design principles can guide effective heterogeneous multi-agent architectures for cost-sensitive software engineering tasks.
