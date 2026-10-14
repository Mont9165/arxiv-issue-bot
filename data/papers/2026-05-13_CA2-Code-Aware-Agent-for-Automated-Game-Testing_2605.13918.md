# CA2: Code-Aware Agent for Automated Game Testing

- arXiv ID: `2605.13918v1`
- Authors: Valliappan Chidambaram Adaikkappan, Vincent Martineau, Joshua Romoff, David Meger
- Published: 2026-05-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2605.13918v1) | [pdf](https://arxiv.org/pdf/2605.13918v1)

## Abstract

Automated game testing is important for verifying game functionality, but it remains a costly and time-consuming process. Manual testing often misses edge cases, and current automated methods struggle to provide full code coverage. Prior work has explored reinforcement learning (RL) for game testing, but without leveraging internal code signals such as the call stack. We present Code Aware Agent (CA2), which uses call stack information to learn effective testing strategies. The agent receives the current function call trace along with the game state and learns to reach specific target functions. We instrument two types of environments, 1) State-based and 2) Image-based, with support for efficient call stack extraction. Through experimental evaluation, we find that CA2 achieves consistent improvement over the non-code aware baselines, which does not leverage call stack information. Our results show that incorporating code signals like the call stack enables more effective and targeted game testing.
