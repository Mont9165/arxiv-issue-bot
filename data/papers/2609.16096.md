# Coaching Qwen3 Coder 30B to Think Like a CodeClash Arena Agent

- arXiv ID: `2609.16096v1`
- Authors: Ivy Ning Zhang
- Published: 2026-09-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2609.16096v1) | [pdf](https://arxiv.org/pdf/2609.16096v1)

## Abstract

Large language model coding agents have recently become useful for software tasks, but weaker or open-weight agents still struggle to reliably interpret user intent and execute complex multi-step workflows. This gap is especially visible in long-horizon settings, where an agent must repeatedly inspect prior outcomes, diagnose failure, and choose the next code edit under interaction constraints. It motivates a natural question: what can we do to improve the thinking process of a weak code agent? We study this question in CodeClash, a code-arena benchmark where the original work evaluates 8 commercial coding agents across 6 arenas through multi-round tournaments. Since Qwen3 Coder Plus ranks last among them, we take the open-weight Qwen3-Coder-30B as a case study and investigate how to improve it with distilled knowledge from stronger agents. Our analysis shows that Qwen3-Coder-30B is not well optimized for arena-style interaction: it frequently produces syntax and protocol-breaking errors and exhibits weak strategic adaptation across rounds. These failures are difficult to correct with vanilla instruction tuning alone, since offline SFT cannot directly verify whether a generated action is valid or beneficial. To address this, we propose ReAct SFT, which rewrites teacher trajectories into explicit [obs][thought][act] chains, and trajectoryquality weighted SFT, which reweights samples to encourage post-edit checking. ReAct SFT substantially improves strategic behavior, and our fine-tuned model outperforms the original Qwen3 Coder Plus in tournament evaluation.
