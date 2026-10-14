# When Context Hurts: The Crossover Effect of Knowledge Transfer on Multi-Agent Design Exploration

- arXiv ID: `2605.04361v1`
- Authors: Saranyan Vigraham
- Published: 2026-05-05
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.04361v1) | [pdf](https://arxiv.org/pdf/2605.04361v1)

## Abstract

The prevailing assumption in agent orchestration is that more context is better. We test this on multi-agent software design across 10 tasks, 7 context-injection conditions, and over 2,700 runs, and find a crossover effect: the same artifact type improves design exploration on some tasks (up to 20$\times$ tradeoff coverage) and actively degrades it on others (up to 46% reduction). On several tasks, an irrelevant document performs as well as or better than every relevant artifact. The direction is predicted by a single measurable variable--baseline exploration without context--with Pearson $r = -0.82$ ($p < 0.001$). Probing the mechanism by manipulating convergence pressure through prompt design reveals two distinct regimes: convergence driven by training data priors (natural) responds to artifact disruption, while convergence driven by explicit instructions (induced) does not. The implication is that context injection should be conditional, not universal: one no-context trial is a cheap diagnostic that predicts whether knowledge artifacts will help or hurt a given task.
