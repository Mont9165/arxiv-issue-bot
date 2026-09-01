# EvoGenUI-Bench: Evaluating LLMs as Multi-Turn Generative UI Assistants

- arXiv ID: `2608.29387v1`
- Authors: Yue Peng, Lanke Xia, Zihan Wang, Jiahao Ye, Ke Ning, Hongyi Wen
- Published: 2026-08-29
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.29387v1) | [pdf](https://arxiv.org/pdf/2608.29387v1)

## Abstract

Large language models can generate interactive web interfaces, but reliable generative UI requires maintaining an executable artifact as user requests evolve. We introduce EvoGenUI-Bench, a benchmark for multi-turn interface maintenance comprising 150 five-turn tasks and 750 turns across three scenarios: information presentation, executable interaction, and tool-grounded external state. We execute generated artifacts in a browser and evaluate them using screenshots, source and DOM evidence, actor traces, and runtime logs. Beyond turn-level and episode-level success, we measure cross-turn retention with Adjacent Pass Retention. Across eight models, even the strongest achieves 74.9% Turn Pass while completing only 37.3% of five-turn episodes; APR further falls to 52.4% on tool-grounded tasks. Diagnostic analysis shows that presentation failures center on information architecture, interaction failures on derived-state propagation and affordance binding, and tool-grounded failures additionally involve external-state grounding and requirement decomposition. These results reframe generative UI evaluation from judging isolated outputs to testing whether interface behavior, derived state, external state, and assistant claims remain synchronized as the artifact evolves.
