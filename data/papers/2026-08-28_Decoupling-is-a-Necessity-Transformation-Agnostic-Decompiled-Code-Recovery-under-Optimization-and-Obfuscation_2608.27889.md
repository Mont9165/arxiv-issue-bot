# Decoupling is a Necessity: Transformation-Agnostic Decompiled Code Recovery under Optimization and Obfuscation

- arXiv ID: `2608.27889v1`
- Authors: Zhiping Zhou, Xiaohong Li, Ruitao Feng, Yao Zhang, Yuekang Li, Wenbu Feng
- Published: 2026-08-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.27889v1) | [pdf](https://arxiv.org/pdf/2608.27889v1)

## Abstract

Reverse engineering is essential for software security analysis and vulnerability detection. Decompilation, the process of lifting binaries to high-level pseudocode, is central to this task. However, production binaries are hostile environments: aggressive compiler optimizations and adversarial obfuscation jointly mangle control structures, obscure variable intents, and disguise high-level program logic. Consequently, existing LLM-based decompilation tools frequently suffer from structural collapse and semantic hallucinations. We present ReSource, the first multi-phase LLM framework designed for transformation-agnostic source recovery. To tackle these intertwined distortions, ReSource conceptualizes the binary-to-source discrepancies into three orthogonal tiers, namely lexical, syntactic, and semantic, and decouples the recovery process accordingly. First, to ground the LLM and prevent logic drift, it retrieves empirical priors from a curated Semantic Distortion Database. Second, to resolve control-flow flattening, it integrates a lightweight predictor to reconstruct the source-level structural skeleton. Finally, a contextual lexical deduction stage refines identifiers to restore human readability. Evaluated on a massive benchmark of over 80,000 decompiled-source function pairs across three optimization levels and four obfuscation techniques, ReSource achieves an 83% Top-5 source retrieval accuracy and an average similarity score of 0.66. By maintaining robust semantic identifiability where state-of-the-art baselines (DeGPT, LLM4Decompile, and FidelityGPT) severely overfit or degrade, ReSource provides a scalable and reliable foundation for downstream security analysis.
