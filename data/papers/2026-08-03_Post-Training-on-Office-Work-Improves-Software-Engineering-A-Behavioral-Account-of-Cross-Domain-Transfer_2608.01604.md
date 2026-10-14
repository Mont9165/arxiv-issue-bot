# Post-Training on Office Work Improves Software Engineering: A Behavioral Account of Cross-Domain Transfer

- arXiv ID: `2608.01604v1`
- Authors: Logan Ritchie, Sushant Mehta, Liudas Panavas, Edwin Chen
- Published: 2026-08-03
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.01604v1) | [pdf](https://arxiv.org/pdf/2608.01604v1)

## Abstract

Long-horizon tasks require agents to maintain coherent state and goals across nested and branching work. We call this capability goal-directed execution (GDE): the repeated application of four behaviors, namely selecting goals, constructing task-relevant state, maintaining fidelity to higher-level objectives, and verifying completion against the environment. We hypothesize that long-horizon post-training strengthens these behaviors across domains. We test this by post-training Qwen3.5-122B-A10B on 363 Long-Horizon Multi-Tool Agent (LHMTA) tasks drawn from office workflows. The collection contained no software-engineering tasks, yet the model's pass@1 improved by 5.8 points on SWE-Bench Pro. Matched trajectory analysis shows gains in all four GDE behaviors in both office workflows and software repositories. Aggregate SWE-Bench Pro statistics showed related changes in information gathering, implementation, and verification. Together, the results support a behavioral interpretation in which long-horizon post-training changed how the model organized and applied knowledge across tasks, with effects extending beyond the training domain.
