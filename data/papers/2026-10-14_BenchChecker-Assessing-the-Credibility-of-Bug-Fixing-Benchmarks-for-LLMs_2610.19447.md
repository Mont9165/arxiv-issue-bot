# BenchChecker: Assessing the Credibility of Bug-Fixing Benchmarks for LLMs

- arXiv ID: `2610.19447v1`
- Authors: Di Wu, Xu He, Shu Wang, Kun Sun
- Published: 2026-10-14
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.19447v1) | [pdf](https://arxiv.org/pdf/2610.19447v1)

## Abstract

While Large Language Models (LLMs) show promise for Automatic Program Repair (APR), existing benchmarks suffer from data contamination, in which test samples appear in training sets, artificially inflating performance. To address this, we propose BenchChecker, a framework compatible with both open-source and closed-source models that supports more credible evaluation by detecting such contamination. Grounded in the observation that persistent patches likely remain in recent repository snapshots used for training, BenchChecker employs a forensics-based two-stage detection process using only textual model outputs together with public repository history. The first stage conducts a repository presence test by probing the model with code prefixes to infer training inclusion; the second stage performs a patch presence test to verify patch persistence via similarity alignment and test-suite verification. Evaluations using StarCoder-15B, StarCoder2-15B, and CodeGen2-16B trained on The Stack v2 demonstrate that BenchChecker achieves robust detection with AUC scores around 0.9 across six benchmarks. Furthermore, applying BenchChecker to SWE-bench Verified and Multi-SWE-bench reveals that filtering contaminated samples reduces the reported resolution rates of most LLMs by more than 20% relative to the original rates on medium-difficulty tasks.
