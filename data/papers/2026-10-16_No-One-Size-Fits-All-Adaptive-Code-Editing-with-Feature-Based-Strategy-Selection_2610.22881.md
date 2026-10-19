# No One-Size-Fits-All: Adaptive Code Editing with Feature-Based Strategy Selection

- arXiv ID: `2610.22881v1`
- Authors: Jun Wan, Zhongxin Liu, Dajun Chen, Wei Jiang, Yong Li, Xiaoxue Ren
- Published: 2026-10-16
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.22881v1) | [pdf](https://arxiv.org/pdf/2610.22881v1)

## Abstract

Large language models have shown strong potential in automating code editing (CE) tasks, yet most existing systems rely on a fixed CE strategy (i.e., one-step, search-replace, and plan-apply) across diverse scenarios. In practice, CE tasks vary widely in code context, edit locality, and semantic complexity, causing no single strategy to perform consistently well. Moreover, systematic studies on the relationship between strategies and CE tasks remain scarce, limiting further optimization of LLM-based code editing strategies. To address this gap, we construct CEBench, comprising 500 real-world CE tasks curated from SWE-bench. Then we compare three representative CE strategies (one-step, search-replace, plan-apply). Our study reveals two key findings: (1) each strategy exhibits distinct advantages for specific CE tasks, with no universal optimality; (2) strategy effectiveness is significantly influenced by four core task features: total lines of code, modification type, modification scope, and task type. Motivated by these findings, we propose Ace, an adaptive code editing framework that dynamically selects optimal CE strategies based on task features. Unlike classifier-based or instruction-prompting approaches, Ace employs a fine-tuned LLM that learns feature-strategy mappings from empirical data to recommend strategies with interpretable rationales. Extensive experiments on our CEBench-verified show that Ace outperforms state-of-the-art baselines: it boosts Pass@1 by 21.7% while reducing token consumption by 27.3% compared to the best baseline (AutoCodeRover). Our strategy selector achieves 72.6% selection accuracy with 69.9% rationale accuracy (Cohen's Kappa = 0.807), providing transparent and trustworthy decision-making for developers.
