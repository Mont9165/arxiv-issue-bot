# Event-B Agent: Towards LLM Agent for Formal Model Synthesis and Repair

- arXiv ID: `2605.17475v1`
- Authors: Hongshu Wang, Xinyue Zuo, Yuhan Sun, Qin Li, Yamine Ait Ameur, Jin Song Dong
- Published: 2026-05-17
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.17475v1) | [pdf](https://arxiv.org/pdf/2605.17475v1)

## Abstract

Building software that is correct by construction is a long-standing goal in software engineering, as it ensures reliability during design and development rather than after deployment. Formal methods realize this vision by enabling the expression of system behavior and requirements in mathematics, thereby guaranteeing correctness through formal verification, including theorem proving and model checking. However, the steep learning curve and demand for mathematical expertise hinder the widespread adoption of formal methods. Large language models (LLMs) have recently shown promise in bridging this gap through autoformalization. However, existing LLM-based approaches are largely limited to isolated tasks, such as theorem proving without formalization or model synthesis with insufficient verification. While valuable, these efforts do not fully exploit the potential of a more comprehensive framework in which models and proofs evolve together, a process that closely reflects real-world development practice. To address this gap, we propose Event-B Agent, a novel framework inspired by the interleaved nature of software design. Given natural language requirements, Event-B Agent constructs an initial model and iteratively repairs and refines it using formal verification feedback. Refinement simplifies proof discharge, while repair of models and proofs ensures the soundness of each refinement step. Together, these two components reinforce each other to progressively improve the model quality. Evaluation across systems of varying complexity demonstrates that Event-B Agent substantially outperforms baselines in end-to-end formal model synthesis and repair, while maintaining reasonable efficiency. These results suggest that Event-B Agent is a promising step toward correct-by-construction formal model synthesis and repair.
