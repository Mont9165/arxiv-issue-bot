# Reusable LLM-Based Plans with Probabilistic Guarantees for Self-Adaptive Systems

- arXiv ID: `2610.38039v1`
- Authors: Asher Tempest Arya, Rajan Maghera, Nicholas Wu Jiang, Federico Mora, Aren A. Babikian, Marsha Chechik
- Published: 2026-10-27
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.38039v1) | [pdf](https://arxiv.org/pdf/2610.38039v1)

## Abstract

Self-adaptive systems are designed to accommodate variants of their environment, which form a family of instances whose uncertainty is captured by probabilistic models, and must meet probabilistic requirements on each instance. Within such a family, changes in size and structure complicate the fundamental adaptation decision: whether to retain, reuse, or construct a new controller, since controllers are often synthesized for and specific to an instance. Large language models (LLMs) have recently been used to write reusable controllers, but existing approaches largely target deterministic domains, and probabilistic model checking of their output remains limited to preliminary single-instance studies. In this paper, we propose a verifier-guided framework for controller reuse with explicit support for families of environments. The framework introduces a novel combination of LLM-written controllers with probabilistic model checking to provide per-instance guarantees for probabilistic requirements. We evaluate our approach using three LLMs on three benchmarks, assessing its effectiveness and cost with respect to baseline implementations, the distribution of adaptation decisions, and the impact of individual framework components. On grid worlds, LLM-written rule lists are verified on about 90% of held-out instances, against at most 77% for the baselines, and verifying a stored rule list is 15 to 103 times faster than per-instance synthesis. Reuse serves most episodes at a small fraction of the cost of generation or per-instance synthesis, and model-checking feedback increases verified coverage over independent restarts.
