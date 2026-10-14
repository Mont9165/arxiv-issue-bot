# Beyond Static Guarantees: Measuring the Static-Pass Dynamic-Fail Gap in Security-Sensitive and LLM-Generated Python Code

- arXiv ID: `2609.10762v1`
- Authors: Jessica Pourleyli, Maitreyee Das Urmi, Glaucia Melo
- Published: 2026-09-09
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.10762v1) | [pdf](https://arxiv.org/pdf/2609.10762v1)

## Abstract

Advances in large language models (LLMs) fuel the quest for scalable methods to assess the security of generated and security-sensitive software. Static analysis is widely adopted as a scalable, reproducible, and inexpensive security gate, but cannot directly observe runtime exploit behaviour. Vulnerabilities dependent on adversarial inputs, execution context, or exploit chaining may evade static checks while remaining exploitable in practice, yet passing static analysis is often treated as evidence of secure behaviour. This paper introduces the Static-Pass Dynamic-Fail (SPDF) phenomenon and a three-stage agentic pipeline combining static scanning, LLM-driven Common Weakness Enumeration (CWE) reasoning, and autonomous exploit verification in isolated Docker containers. We evaluate 1,355 Python samples from SecurityEval, RedCode, and CyberNative datasets. Of the 654 samples producing no findings under the composite Bandit-Semgrep gate, the LLM detection stage identified 394 candidate vulnerabilities across 235 files. Dynamic verification confirmed or partially confirmed exploitability in 95 files, yielding an inclusive pipeline rate of 14.53% (roughly 1 in 7 statically clean samples). This rate represents the proportion of Bandit-Semgrep-clean samples for which the pipeline identified a candidate vulnerability and obtained runtime evidence supporting exploitability. Outcomes varied by dataset: among candidate file--CWE pairs, confirmed exploitability was 33.7% for RedCode, 28.6% for CyberNative, and 5.4% for SecurityEval. Several frequently confirmed classes, including CWE-338 and CWE-916, were flagged by neither Bandit nor Semgrep. These findings indicate that static-analysis success and runtime security are hierarchical layers of software assurance rather than interchangeable measures, and have the potential to reshape how AI-generated and security-sensitive code is evaluated.
