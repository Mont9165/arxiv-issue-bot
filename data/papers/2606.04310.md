# Latent Anchor-Driven Test Generation for Deep Neural Networks

- arXiv ID: `2606.04310v1`
- Authors: Bin Duan, Matthew B. Dwyer, Guowei Yang
- Published: 2026-06-03
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.04310v1) | [pdf](https://arxiv.org/pdf/2606.04310v1)

## Abstract

Deep Neural Networks (DNNs) are increasingly being deployed in security-critical and safety-sensitive applications, which makes rigorous testing essential to identify and mitigate model weaknesses. Existing DNN testing approaches explore either the input space or a learned latent space. While latent-space generation can better maintain plausibility than direct input-space mutation, current methods still face a trade-off among exploration controllability, failure diversity, and seed-relative semantic drift. To overcome these limitations, we propose Latte, a black-box testing framework that generates semantically proximate, diverse, and fault-revealing test cases by leveraging the latent space. Specifically, Latte encodes each input seed with a pre-trained VQ-VAE and performs a seed-centered, one-step latent mutation along directions defined by anchors sampled from alternative classes, followed by quantization and decoding back to the input space. This explores local neighborhoods around each seed within the learned latent manifold, resulting in a larger number and broader diversity of oracle-triggering prediction discrepancies under the same budget. We evaluated Latte on 5 datasets and 10 DNN models in single-model and multi-model testing scenarios. Across the evaluated datasets and models, Latte improves fault exposure and behavioral diversity under matched testing budgets. Under the single-model setting, it also maintains low seed-relative semantic drift with respect to the source seeds.
