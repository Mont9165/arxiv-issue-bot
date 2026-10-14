# Towards LLM-Enhanced Android Taint Analysis

- arXiv ID: `2608.24269v1`
- Authors: Nicholas Miazzo, Marco Alecci, Jordan Samhi, Jacques Klein, Eleonora Losiouk
- Published: 2026-08-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2608.24269v1) | [pdf](https://arxiv.org/pdf/2608.24269v1)

## Abstract

Taint analysis is a fundamental technique for detecting sensitive data leaks in Android apps. However, traditional static tools, such as FlowDroid, still face well-known challenges due to the complexity of accurately modeling the Android framework. In this paper, we investigate whether off-the-shelf Large Language Models (LLMs) can effectively reason about taint flows in Android apps. Our preliminary approach relies on an agentic interaction strategy, enabling the LLM to iteratively explore code and reason about data flows.
  We conduct an initial evaluation on the DroidBench benchmark against FlowDroid, where our approach outperforms the baseline: Gemini-3 Flash achieves an F1-score of 0.96, compared to 0.55 for FlowDroid. In particular, we observe improvements in challenging categories such as inter-component communication (0.95 vs. 0.17), implicit flows (0.94 vs. 0.00), and reflection (1.00 vs. 0.50), where FlowDroid typically struggles. On a small set of real-world apps, the LLM-based approach also identifies additional potential data leaks not reported by FlowDroid. These preliminary findings suggest that LLM reasoning may effectively complement traditional static taint analysis, motivating future research on hybrid LLM-enhanced taint analysis pipelines.
