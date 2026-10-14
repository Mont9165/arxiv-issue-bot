# CONTRA: Discovering and Qualifying Behavior-Changing Questions for Selective Clarification in LLM Code Generation

- arXiv ID: `2610.01769v1`
- Authors: Zheng Fang, Yongmin Li, Yichang Zhang, Dongming Jin, Haoyu Wang, Shuai Wang, Zhi Jin, Ge Li
- Published: 2026-10-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.01769v1) | [pdf](https://arxiv.org/pdf/2610.01769v1)

## Abstract

Coding agents can generate code that appears correct but implements behavior the user never intended. This mismatch can arise when an agent silently resolves underspecified requirements through its own assumptions. As subsequent development builds on these assumptions, correcting the resulting behavior can become increasingly costly. Early clarification can help prevent such mismatches, but unnecessary questions can interrupt developers and slow down development. Existing methods struggle to identify key clarification questions while avoiding unnecessary ones. Therefore, we propose CONTRA, a training-free method that combines broad question discovery with semantic and execution-based question qualification. CONTRA first generates candidate questions and filters out those unrelated to required behavior or already resolved by the requirement. For each remaining question, it generates programs conditioned on two plausible answers and checks for stable behavioral differences on shared inputs. It then uses the interaction history to select among qualified questions or stop asking. Experiments on ClarifyCodeBench show that CONTRA achieves the highest F1 with all four coding agents, exceeding the best baseline macro-average F1 by 13.88 percentage points. With the same LLM and evaluation protocol, CONTRA also achieves higher clarification recall and F1 than the coding harnesses Claude Code and OpenHands. To support practical use, we also implement CONTRA as a Claude Code plugin that integrates selective clarification into everyday development.
