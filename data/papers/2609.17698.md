# A Large-Scale Empirical Study of Quality Assurance Practices and Gaps in AI Agents

- arXiv ID: `2609.17698v1`
- Authors: Wuyang Dai, Moses Openja, Jiho Shin, Hung Viet Pham, Song Wang
- Published: 2026-09-15
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.17698v1) | [pdf](https://arxiv.org/pdf/2609.17698v1)

## Abstract

Large language model (LLM)-based agents are increasingly used across software engineering, web automation, research, and productivity applications. Their integration of planning, memory, tool use, code execution, and external interactions enables greater autonomy but also introduces new reliability, safety, and security risks. We present a large-scale empirical study of quality assurance (QA) practices in 157 open-source LLM-based agent projects with at least 100 GitHub stars. We analyze documentation, source code, configurations, and tests to characterize QA practices across execution surfaces, safeguards, testing artifacts, risk scenarios, and recurring gaps. We find that current QA primarily focuses on basic functionality and high-risk actions, while coverage remains fragmented. Safeguards are inconsistently applied across equivalent execution routes, tests rarely examine boundary, adversarial, or multi-step tool-use failures, and identified risks are seldom translated into end-to-end QA checks. These findings highlight the need to move beyond feature-level testing toward systematic end-to-end validation that ensures agent workflows remain within intended boundaries when interacting with untrusted inputs, tools, persistent state, and external APIs.
