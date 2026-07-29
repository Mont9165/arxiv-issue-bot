# Specula: Scaling formal specifications for autonomous model checking of system code

- arXiv ID: `2607.25333v1`
- Authors: Qian Cheng, Saad Mohammad Rafid Pial, Ruize Tang, Yiming Su, Emilie Ma, Finn Hackett, Ivan Beschastnikh, Yu Huang, Tianyin Xu
- Published: 2026-07-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.DC`, `cs.OS`
- Links: [abs](http://arxiv.org/abs/2607.25333v1) | [pdf](https://arxiv.org/pdf/2607.25333v1)

## Abstract

Specula is a push-button agentic system that generates high-quality formal specifications for large, complex system code and uses the specifications for highly effective model checking and bug finding. Specula employs large language model (LLM) based coding agents to autonomously develop TLA+ specifications, including invariants that describe correctness properties of the target system and formal models that describe the system implementation with the right level of abstractions. Specula is fully autonomous and thus eliminates the barrier of applying formal methods to real-world system code (as in traditional human-centric approaches). Meanwhile, Specula addresses limitations of LLM-driven techniques like reward hacking and hallucinations through self-evolving loops that iteratively improve specification quality by enabling the agents to deepen their understanding of system code and its behaviors. We have used Specula to check 48 open-source system projects; Specula found 249 bugs including many deep bugs that are hard to find by existing approaches. Specula has been used by several companies and is maintained at https://github.com/specula-org/Specula.
