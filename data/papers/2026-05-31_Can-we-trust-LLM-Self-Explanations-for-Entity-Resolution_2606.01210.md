# Can we trust LLM Self-Explanations for Entity Resolution?

- arXiv ID: `2606.01210v1`
- Authors: Tommaso Teofili, Donatella Firmani, Nick Koudas, Paolo Merialdo, Divesh Srivastava
- Published: 2026-05-31
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.01210v1) | [pdf](https://arxiv.org/pdf/2606.01210v1)

## Abstract

Large Language Models (LLMs) have recently shown strong performance on Entity Resolution (ER). Additionally, akin to their prowess in providing accurate predictions, these models often generate self-explanations alongside their predictions through prompting. While such self-explanations are appealing due to their negligible computational cost, their actual reliability remains largely unexplored.
  In this paper, we present the first large-scale systematic evaluation of LLM self-explanations for ER, focusing on feature attribution and counterfactual explanations at both the attribute and token levels. Across three LLMs, ten datasets, and multiple prompting strategies, we show that self-explanations are often unstable, weakly faithful, and poorly aligned with counterfactual evidence, revealing a substantial gap between plausibility and causal relevance.
  We further demonstrate that established post-hoc explanation methods provide significantly higher trustworthiness, but at a prohibitive computational cost when applied to LLMs. To bridge this gap, we introduce \uncerta{}, a hybrid explanation framework that leverages self-explanations as priors to guide post-hoc exploration. \uncerta{} achieves explanation quality comparable to post-hoc methods while reducing cost by up to an order of magnitude.
