# A-ProS: Towards Reliable Autonomous Programming Through Multi-Model Feedback

- arXiv ID: `2605.18073v1`
- Authors: Anika Tabassum, Md Sifat Hossain, Md. Fahim Arefin, Tariqul Islam, Tarannum Shaila Zaman
- Published: 2026-05-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.18073v1) | [pdf](https://arxiv.org/pdf/2605.18073v1)

## Abstract

Large Language Models (LLMs) demonstrate strong potential for automated code generation, yet their ability to iteratively refine solutions using execution feedback remains underexplored. Competitive programming offers an ideal testbed for this investigation, as it demands end-to-end algorithmic reasoning, precise implementation under strict computational constraints, and complete functional correctness with rigorous evaluation. In this paper, we present A-ProS, an autonomous AI agent that solves competitive programming problems through a hybrid multi-model feedback framework separating solution generation from specialized debugging. A-ProS combines ChatGPT-based generators (GPT-4 and GPT-5) with three debugging critics: Codestral-2508, Llama-3.3-70B, and DeepSeek-R1, under a 2 x 3 factorial design. We evaluate six workflows on 367 problems from ICPC World Finals (2011-2024) and Codeforces (rated 1200-1800). The results show that GPT-5 workflows improve from 39 initial accepted solutions to 85-90 after three refinement rounds, while GPT-4 improves from 15 to 31-38. A controlled ablation on 47 problems shows that stateful refinement outperforms stateless approaches by 8.5-10.6 percentage points and reduces repeated failures by up to 3.5x. Compared to baseline agent loops, A-ProS achieves over 2x greater gains, highlighting the importance of persistent context and multi-model feedback for reliable autonomous program synthesis.
