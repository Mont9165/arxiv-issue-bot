# Domain-Adaptable Reinforcement Learning for Code Generation with Dense Rewards

- arXiv ID: `2605.21180v1`
- Authors: Erfan Aghadavoodi Jolfaei, Daniel Maninger, Abhinav Anand, Mert Tiftikci, Mira Mezini
- Published: 2026-05-20
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.21180v1) | [pdf](https://arxiv.org/pdf/2605.21180v1)

## Abstract

Large language models show strong potential for automated code generation, but lack guarantees for correctness, quality, safety, and domain-specific constraints. For instance in robotics, where code generation is increasingly being used for planning and executing actions, awareness of the environment and physical constraints is critical. To facilitate the adaption of code-generating LLMs to diverse requirements, including domain-specific ones, we present a reinforcement learning framework that fine-tunes pre-trained LLMs using proximal policy optimization. Our customizable execution-aware reward formula captures and optimizes syntax, functional correctness, code style, security, and simulator executability. A token-level reward mapping mechanism enables effective credit assignment from execution outcomes to generated tokens. The framework is evaluated on general-purpose code generation (MBPP/MBPP+) and robotic program synthesis (RoboEval). The results show substantial improvements in functional correctness and simulator executability, including an absolute pass@1 increase of 19% on MBPP and a reduction in execution failures by 51% on RoboEval. These findings demonstrate that structured reinforcement learning can effectively align language models to correct program generation and domain-specific requirements.
