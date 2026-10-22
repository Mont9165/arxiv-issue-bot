# CertMoE: Robustness Certification for Mixture-of-Experts LLMs via Routing-Aware Smoothing

- arXiv ID: `2610.29395v1`
- Authors: Qingyue Wang, Yudong Gao, Lixia Wang, Ruixuan Huang, Yuanyuan Yuan, Yangqiu Song, Shuai Wang
- Published: 2026-10-21
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.29395v1) | [pdf](https://arxiv.org/pdf/2610.29395v1)

## Abstract

Provable robustness is a cornerstone of trustworthy machine learning, aiming to guarantee model predictions under adversarial perturbations. Existing certification frameworks, inspired by abstract interpretation or symbolic execution, typically assume a fixed computation graph, where input perturbations or variations affect only model outputs but not the underlying execution path. This assumption, however, is violated in Mixture-of-Experts (MoE) Large Language Models (LLMs), whose input-dependent routing induces discrete and dynamic execution paths. Crucially, this dynamic computation changes the certified object from a single fixed function to a composition of input-dependent sub-functions, leading to unreliable certification guarantees.
  This paper presents \textsc{CertMoE}, the first routing-aware robustness certification framework for MoE LLMs, which explicitly accounts for input-induced routing dynamics in certification. Specifically, we introduce a relaxed routing-containment criterion, which certifies that perturbed Top-$K$ routing is contained within a larger certified expert pool. Based on this guarantee, \textsc{CertMoE} then constructs the corresponding induced sub-network and certifies its prediction consistency. This hierarchical certification procedure yields a joint probabilistic guarantee over routing containment and sub-network robustness, providing sufficient conditions under which the original prediction remains invariant. Extensive experiments across recent MoE LLMs demonstrate that dynamic routing makes certificates issued by existing methods frequently violated, while \textsc{CertMoE} reduces the empirical violation rate with routing-aware guarantees, e.g., from more than $30\%$ to $0$, yielding certificates that more faithfully reflect the robustness of MoE models.
