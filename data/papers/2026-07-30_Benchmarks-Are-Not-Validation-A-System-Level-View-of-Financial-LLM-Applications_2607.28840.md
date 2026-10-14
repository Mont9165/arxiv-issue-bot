# Benchmarks Are Not Validation: A System-Level View of Financial LLM Applications

- arXiv ID: `2607.28840v1`
- Authors: Burak Payzun, İrem Demirtaş, Simona Scala, Elena Ferretti, Seçil Arslan
- Published: 2026-07-30
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.28840v1) | [pdf](https://arxiv.org/pdf/2607.28840v1)

## Abstract

Large language models are increasingly deployed in financial applications that combine retrieval, proprietary data, tool use, orchestration logic, monitoring, and human escalation. Yet evaluation often remains model-centric: benchmark scores, task accuracy, or one-off qualitative reviews are treated as evidence of readiness. In financial settings, this is insufficient. We take the position that financial LLM systems should not be approved for production based on benchmark performance alone. They require system-level validation evidence across the application stack: data, model design, retrieval and generation performance, agent behavior, governance, and implementation. Drawing on industry experience validating GenAI applications in financial institutions, we outline a multi-layer validation view and explain why hybrid evaluation is necessary. We discuss where LLM-as-a-judge methods are useful and why they require controls such as multiple judges, rubrics, agreement, and auditability checks. We also highlight failure modes poorly captured by static benchmarks, including retrieval failures, unfaithful generation, tool misuse, escalation errors, and operational instability. Our position is that financial LLM validation should be an ongoing system discipline rather than a one-time model scoring exercise. Validation should produce decision-ready evidence, not only scores. We conclude with a research agenda for system-aware benchmarks, agent trace validation, judge alignment protocols, and lifecycle validation standards.
