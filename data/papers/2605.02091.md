# How Compliant Are GitHub Actions Workflows? A Checklist-Based Study with LLM-Assisted Auditing

- arXiv ID: `2605.02091v1`
- Authors: Edward Abrokwah, Taher A. Ghaleb
- Published: 2026-05-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.02091v1) | [pdf](https://arxiv.org/pdf/2605.02091v1)

## Abstract

GitHub Actions (GHA) CI workflows are critical infrastructure, but current tooling offers only syntactic or heuristic checks and does not enforce documented best practices for security, maintainability, or performance. Consequently, issues like over-privileged permissions, weak secrets management, and missing failure notifications remain undetected in real-world pipelines. This paper proposes a novel, documentation-grounded GHA compliance checklist with 30 criteria spanning four workflow sections and eight themes, and assesses Large Language Models (LLMs) for scalable compliance auditing. On 95 real-world Java workflows (2,850 assessments) using four open-weight LLMs, we find only fair agreement (Fleiss' kappa = 0.28), with systematic disagreement on structural reasoning and security-sensitive judgments. To address this, we introduce a multi-tier adjudication framework in which GPT 5 resolves model conflicts before targeted manual review, reducing verification effort by 81% while retaining 87% agreement with expert judgment. At scale, it reveals major compliance gaps: overall compliance is 28%, dropping to 4% for permission controls; Security (26%) lags far behind Clarity (68%). Our results show that LLMs enable scalable compliance measurement but cannot replace experts, highlighting the need for hybrid human-AI auditing and providing empirical benchmarks and guidance for defensible GHA workflow audits.
