# A.S.E 2.0: Understanding How Repository Context Impacts the Security of LLM-Generated Code

- arXiv ID: `2611.06294v1`
- Authors: Jiongchi Yu, Keke Lian, Junqing Wang, Zhikang Fan, Zhaoxuan Li, Yongheng Huang, Ziming Zhao, Dong Zhang
- Published: 2026-11-04
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.06294v1) | [pdf](https://arxiv.org/pdf/2611.06294v1)

## Abstract

Large language model (LLM) coding assistants and agents construct a repository context before generating code. For security-sensitive code, this context decides whether the model sees the project's safeguards (e.g., authorization checks) or insecure code to imitate. However, context construction is designed almost exclusively for functional correctness, and secure-code benchmarks treat the context as fixed, so how repository context affects the security of generated code remains unclear. We construct CASE-Bench, a benchmark of 145 repository-level tasks from real CVEs in 51 projects. Each task runs in Docker, has functional tests and a proof-of-concept exploit validated in both directions, and is annotated with the repository code that enforces or undermines its security. Using CASE-Bench, we compare 13 context construction methods and six controls with six LLMs, edit single context elements, and analyze coding-agent trajectories. We find that (1) functionality-oriented context raises the functional pass rate by up to 8.2 percentage points (pp) but the secure pass rate by at most 3.7 pp, (2) withholding a safeguard lowers the secure pass rate by up to 8.1 pp, while one inserted insecure exemplar raises correct-but-exploitable code by 6.3 pp, and (3) coding agents observe the relevant safeguard in only 27-36% of trajectories. These findings inform security-aware context construction and secure-code evaluation.
