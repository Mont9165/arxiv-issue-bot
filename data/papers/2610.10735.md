# DITTO: A Context-aware Pickle-based Pre-Trained Model Scanner for Effective Security Audits

- arXiv ID: `2610.10735v1`
- Authors: Qiaolin Qin, Wanpeng Li, Benoit Baudry, Lorenzo De Carli, Heng Li, Ettore Merlo
- Published: 2026-10-07
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.10735v1) | [pdf](https://arxiv.org/pdf/2610.10735v1)

## Abstract

Pre-trained models (PTMs) are widely distributed as serialized binaries, but their reuse often exposes software supply chains to deserialization attacks. Despite the emergence of safer serialization formats, the unsafe Pickle format remains prevalent: our analysis of over 10,000 popular Hugging Face repositories reveals that 9.3% rely on Pickle. While many defense mechanisms have been proposed, state-of-the-art model scanners suffer from a coverage-precision gap, missing security-sensitive behaviors and generating excessive false alerts. In this paper, we introduce DITTO, the first stack-based, context-aware scanner for Pickle-based PTMs. DITTO faithfully tracks Pickle virtual machine state transitions and performs context-aware semantic analysis to infer model intentions. We also present PickleBench, a benchmark of 959 benign and 92 malicious real-world models, including extension registry attacks previously missed by existing tools. Across multiple evaluations, DITTO achieves 100% scanning coverage, a 0% false-negative rate, and a 0.7% false-positive rate, yielding an F1 score of 0.966, significantly outperforming state-of-the-art scanners. By minimizing false alerts while preserving detection accuracy, DITTO generates actionable security reports with contextual evidence, enabling safe PTM reuse and strengthening software supply chain integrity.
