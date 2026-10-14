# Regression Accumulation in Multi-Turn LLM Programming Conversations

- arXiv ID: `2607.01855v1`
- Authors:  Yonghui,  Huang, Lin Ma, Amjed Tahir, Qian Zhang, Liwen Xiao, Lysa Xiao
- Published: 2026-07-02
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.01855v1) | [pdf](https://arxiv.org/pdf/2607.01855v1)

## Abstract

In LLM-assisted software development, coding is often iterative. We study regression accumulation in multi-turn LLM programming conversations, where later code suggestions may break requirements introduced in earlier turns. Reliability therefore depends not only on satisfying the current request, but also on preserving previously satisfied behavior.
  We construct 542 tasks from HumanEval+ and MBPP+ and extend each task into an 8-turn requirement-evolution chain. We evaluate six LLMs on 26,016 turn instances (542 x 6 x 8). At each turn, we test whether the current code still passes earlier benchmark tests. We also analyze 384 failure cases from the failure population and build a taxonomy of multi-turn regression bugs through independent four-annotator labeling.
  Our results show that regression accumulation appears across all six models: 40% to 73% of tasks lose previously correct behavior over the full conversation. Final-turn quality is lower than initial-turn quality across models, especially when later turns add input validation or broader input types. Manual analysis shows that Cross-Turn Conflict, where later code conflicts with earlier requirements, is the main failure class. We further find that Verification Gate, which checks new code against prior tests and triggers rollback and retry, is the only strategy that consistently improves all models, raising final-turn quality from 75.8% to 87.9% on DeepSeek-V3 and from 31.6% to 47.3% on Llama-3.1-8B.
  These findings suggest that strong single-turn performance can overestimate reliability in multi-turn coding conversations. Future evaluation and tool design should test whether later code suggestions preserve earlier requirements and should include Verification Gate mechanisms.
