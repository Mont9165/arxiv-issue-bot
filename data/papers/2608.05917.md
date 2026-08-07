# Escaping the Self-Repair Trap: Improving Test Oracle Generation via Dual-Context Awareness

- arXiv ID: `2608.05917v1`
- Authors: Kefan Li, Hongyue Yu, Yuan Yuan
- Published: 2026-08-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.05917v1) | [pdf](https://arxiv.org/pdf/2608.05917v1)

## Abstract

Large Language Models (LLMs) have shown strong potential for regression-oracle completion, where a test prefix is given and the current program version is treated as expected behavior. Recent approaches increasingly rely on iterative self-repair and execution feedback, but optimizing execution success does not necessarily yield strong fault-revealing oracles. This objective, widely adopted in repair-based methods, serves only as a proxy and may be misaligned with the true goal of oracle generation. Such misalignment biases the repair process, giving rise to a feedback-driven degeneration that we term the Self-Repair Trap, where iterative repair progressively drives models toward assertions that are easier to satisfy but less effective at detecting faults. To address this issue, we propose DCAware, a computationally efficient, non-iterative framework that prioritizes high signal-to-noise contextual grounding over multi-round repair. DCAware integrates structured static context with selectively retrieved dynamic states, enabling precise and robust oracle generation without iterative feedback loops. Extensive experiments based on execution and mutation testing show that DCAware consistently improves fault-revealing effectiveness while maintaining high execution success, outperforming prior methods with substantially lower computational cost. Our results suggest that improving contextual quality is more effective than adding iterative repair complexity in the studied regression-oracle setting.
