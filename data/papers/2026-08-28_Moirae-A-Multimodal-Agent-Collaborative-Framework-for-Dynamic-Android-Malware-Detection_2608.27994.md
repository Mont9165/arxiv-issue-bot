# Moirae: A Multimodal Agent Collaborative Framework for Dynamic Android Malware Detection

- arXiv ID: `2608.27994v1`
- Authors: Xueying Zeng, Youquan Xian, Yanze Li, bowen hu, Ziqi Shan, Xu Luo, DanPing Yang, Peng Liu, Lei Cui, Bo Li
- Published: 2026-08-28
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.27994v1) | [pdf](https://arxiv.org/pdf/2608.27994v1)

## Abstract

The Android ecosystem faces persistent and rapidly evolving malware threats. Existing machine learning detectors are vulnerable to concept drift because they rely on implementation-specific features whose distributions change over time. Large language models (LLMs) offer strong semantic understanding and zero-shot reasoning, but current LLM-based detectors typically depend on code-centric or single-dimensional evidence, making them susceptible to obfuscation and limiting comprehensive behavior analysis. We present {\sysname}, a multimodal agent collaborative framework for dynamic Android malware detection. {\sysname} dynamically collects multimodal runtime evidence and employs ReAct-based specialized agents to analyze complementary behavioral views. The detection process begins by identifying visual deception cues, modeling UI state transitions, and integrating runtime API behaviors to fuse multi-dimensional evidence across user-visible interfaces and hidden backend operations. Experiments on temporally and distributionally unseen datasets show that {\sysname} achieves an accuracy of 90.06\% without fine-tuning, outperforming state-of-the-art baselines and demonstrating strong zero-shot generalization against Android malware concept drift.
