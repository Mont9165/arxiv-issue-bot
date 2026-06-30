# When AI Reviews Its Own Code: Recursive Self-Training Collapse in Code LLMs

- arXiv ID: `2606.28438v1`
- Authors: Xinyuan Song, Zekun Cai, Liang Zhao
- Published: 2026-06-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.28438v1) | [pdf](https://arxiv.org/pdf/2606.28438v1)

## Abstract

Recursive self-training can degrade neural generative models when generated data is reused without fresh human data or external quality control. We study this risk in code LLMs, where AI-generated code can enter real repositories, later become training data, and create a repository-scale self-training loop. While software development traditionally interrupts this loop through pull-request review, tests, compilation, and human approval, AI coding tools now produce code faster than humans can review it, and code review itself is increasingly automated by AI systems. We therefore compare three recursive fine-tuning regimes: no review, Human-gate review using model-independent filters such as compilation and static quality checks, and AI-self-gate review using the code LLM's own signals such as perplexity and binary self-scoring. Across multiple code LLMs and benchmarks, no review collapses fastest, Human-gate filters slow but do not stop collapse, and AI-self-gate filters can look strong early but later lose their filtering effect. In the clearest case, the binary self-gate enters a rubber-stamp regime where acceptance scores rise while benchmark correctness falls. We explain this behavior by formulating review as gated distributional reweighting, proving that AI self-gating degenerates to ungated self-training under a self-confirming acceptance condition, and giving a spectral analysis of representation-level covariance concentration under recursive retraining. These results suggest that stable recursive code LLM training requires exogenous verification rather than model-coupled self-review.
