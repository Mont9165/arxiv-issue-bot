# V$^3$AST-Bench: Verifiable, Valid, and Versatile Safety Evaluation for Coding Agents

- arXiv ID: `2610.35188v1`
- Authors: Weitao Feng, Hengheng Xiong, Zihao Zeng, Jun Chen, Jiyang Guan, Xiaofeng Wang, Jialing Tao, Hui Xue, Wei Dong
- Published: 2026-10-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.35188v1) | [pdf](https://arxiv.org/pdf/2610.35188v1)

## Abstract

Large language models increasingly act through code, modifying repositories, executing programs, and interacting with services in agent form. Their actions introduce risks that cannot be assessed from generated responses alone. Safety evaluation must verify actual consequences, distinguish harm avoidance from task incapability, and cover realistic workflows. We introduce V$^3$AST-Bench, a benchmark for Verifiable results, Valid interpretation, and Versatile risk coverage of Agent Safety. It comprises 212 risk tasks spanning 18 categories. Dedicated runtime environments verify harm and task outcomes through executable checks over states, records, and artifact behavior, while paired capability twin tasks verify workflow competence. Our experiments span 51 combinations of 11 models and five harnesses, spanning 86,496 trials and over 9 billion tokens of model interaction. Results show that V$^3$AST-Bench remains challenging even for frontier coding agents, as Claude Opus 4.8 with Claude Code still causes verified harm on 20.9% of tasks. Across model-harness combinations, agents with comparable competence exhibit markedly different safety outcomes, showing that task capability alone does not guarantee safe execution. More importantly, even explicit recognition of risks does not reliably prevent harmful actions, revealing a critical gap between risk awareness and safe execution. These findings highlight the need to move beyond risk recognition toward enforcing safety throughout execution.
