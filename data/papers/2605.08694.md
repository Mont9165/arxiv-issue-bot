# A Learning Method for Symbolic Systems Using Large Language Models

- arXiv ID: `2605.08694v1`
- Authors: Jian Fang, Yixun Yao, Yingfei Xiong
- Published: 2026-05-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.08694v1) | [pdf](https://arxiv.org/pdf/2605.08694v1)

## Abstract

Automated theorem proving is essential for the formal verification of safety-critical systems. As the corpus of formal proofs grows, a natural paradigm is to learn from existing proofs. However, current learning-based approaches predominantly train Large Language Models (LLMs) as end-to-end provers, which yields resource-intensive, opaque systems. Conversely, while traditional symbolic provers are computationally efficient, how to automatically improve these solvers from data remains an open challenge.
  This paper bridges this gap by proposing LLM2Ltac, the first approach that leverages the reasoning power of LLMs not as end-to-end provers, but as intelligent synthesizers to mine purely symbolic tactics from data. Given a corpus of formal proofs, LLM2Ltac asks an LLM to identify latent proof strategies and formalize them into reusable tactics. These tactics are verified for validity and generalizability, and finally integrated into symbolic provers to enhance their automated proving capabilities without the runtime cost of LLMs.
  We implement LLM2Ltac on Rocq 8.20.0 and mine tactics from 11,725 theorems in the standard library. We evaluate our approach on 6,199 theorems from four large real-world verification projects, namely, compcert, Coq-Art, Ext-Lib, and VFA. Results show that the mined tactics improve CoqHammer to prove 23.87% more theorems, and when integrating the improved CoqHammer with Claude Code, the overall proved theorems increases by 9.90%, indicating the effectiveness of LLM2Ltac.
