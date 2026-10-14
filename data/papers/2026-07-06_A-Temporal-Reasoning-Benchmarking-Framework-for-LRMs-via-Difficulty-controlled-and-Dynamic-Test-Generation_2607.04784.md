# A Temporal Reasoning Benchmarking Framework for LRMs via Difficulty-controlled and Dynamic Test Generation

- arXiv ID: `2607.04784v1`
- Authors: Shide Zhou, Kailong Wang, Ling Shi, Haoyu Wang
- Published: 2026-07-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.04784v1) | [pdf](https://arxiv.org/pdf/2607.04784v1)

## Abstract

Defining the reasoning boundaries and ensuring the reliability of Large Reasoning Models (LRMs) remains a critical challenge. Current benchmarks primarily rely on static datasets susceptible to data contamination or synthetic tasks lacking fine-grained difficulty control. Furthermore, standard outcome-based evaluations often conceal reasoning flaws by neglecting the reasoning process.
  To address these limitations, we introduce TRACE, a testing framework that models temporal reasoning as constraint satisfaction problems via Allen's Interval Algebra. This approach enables precise regulation of logical complexity and incorporates a Trace-Based Verification Oracle to validate reasoning faithfulness. Using this framework, we construct TRACEBench, an extensive benchmark comprising 1,200 synthesized test instances across graded difficulty levels. We employ TRACE to evaluate eight widely used LRMs on TRACEBench. The results confirm a strong negative correlation between model performance and our difficulty metric (Pearson's r approximately -0.96), validating the effectiveness of our difficulty control mechanism. Moreover, our trace-based analysis exposes significant discrepancies between reasoning validity and final answers, revealing a high spurious guessing rate of approximately 28% in mid-sized models. In addition, we diagnose scale-dependent failure modes, ranging from Degenerative Loops in small models to Reasoning Explosion in advanced architectures. TRACE thus provides a robust, automated platform for benchmarking the true temporal reasoning capabilities of LRMs.
