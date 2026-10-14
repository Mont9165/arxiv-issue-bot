# Toward Localizing and Repairing Bias in Transformer Attention Heads

- arXiv ID: `2607.12863v1`
- Authors: Sigma Jahan
- Published: 2026-07-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.12863v1) | [pdf](https://arxiv.org/pdf/2607.12863v1)

## Abstract

Transformer language models are increasingly used as software components, yet biased outputs remain difficult to localize and repair inside the model. Existing fairness testing and repair methods largely operate at the input-output or retraining level, while recent work suggests that bias-related behavior can concentrate in a small set of attention heads. This paper studies whether attention heads can be localized and repaired through a targeted inference-time intervention. We introduce ROBIN, a white-box head-level fairness debugging method that ranks attention heads using sensitivity to fairness probes and removes a small bias subspace from selected head outputs. In a four-model pilot study, ROBIN reduces the measured WinoBias gap across all models while preserving language-modeling quality better than whole-head zeroing. These preliminary results suggest that head-level bias repair should consider not only which heads are selected, but also how selected heads are modified.
