# SCOPE: Leveraging Subgoal Critiques for Code Generation

- arXiv ID: `2607.05810v1`
- Authors: Yueke Zhang, Yifan Zhang, Zihan Fang, Kevin Leach, Wei Zhang, Yu Huang
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.05810v1) | [pdf](https://arxiv.org/pdf/2607.05810v1)

## Abstract

Code generation with large language models (LLMs) remains unreliable because generated programs can appear correct while still violating key semantic requirements in the natural language specification. Existing feedback-based methods improve over coder-only generation, but they often rely on unstructured critique or execution signals that do not explicitly identify what the code is semantically missing. We present SCOPE, a prover-initialized subgoal critic for code generation. SCOPE adapts a Lean-oriented prover model to produce three parseable feedback fields for downstream code generation: subgoals, gap analysis, and a robustness checklist. Our approach combines supervised fine-tuning, process-aligned reinforcement learning (RL), and feedback-guided inference, with two complementary rewards during RL: a dense reward for structured critique quality and a sparse reward based on whether the critique improves the coder's execution score.
  Experiments show that SCOPE improves over the compared feedback baselines. On LiveCodeBench V6, SCOPE achieves 39.4% pass@1, compared with 36.6% for Reflexion and 20.6% for the coder-only baseline. On BigCodeBench (Hard), it reaches 42.6%, surpassing Reflexion at 36.5% and coder-only generation at 34.5%. Further analysis shows that SCOPE's gains are concentrated in tasks with concrete semantic constraints and that its code corrections are more localized than Reflexion's.
