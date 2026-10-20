# Beyond Leaderboards: A Method for Application-Specific Capability Profiling of Large Language Models

- arXiv ID: `2610.25659v1`
- Authors: Oleg Grynets, Vasyl Lyashkevych, Andrii Salyk, Dmytro Koziuberda, Dmytro Kostetskyi, Oleh Kaskun, Olena Pochernina, Alona Seletska, Oleksii Ilchuk, Viktoriia Tsymbal, Daryna Tukalo, Bohdan Saukh, Ivan Fedorchuk, Hryhorii Petrenko
- Published: 2026-10-19
- Primary category: `cs.LO`
- Categories: `cs.LO`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.25659v1) | [pdf](https://arxiv.org/pdf/2610.25659v1)

## Abstract

Public leaderboards rank large language models (LLMs) in general, but an engineer has to choose a model for a specific application, architecture and cost. This paper presents a method for application-specific capability profiling of LLMs and its realization as a containerized testbed. The method treats each application as a unit of extension: an Oracle-to-PostgreSQL migration agent, a documentation-grounded chatbot or an enterprise-support automation agent runs in its own container behind a small contract, brings its own dataset, evaluator and owned attributes, and is onboarded together with its dashboards. Measurements accumulate in a versioned, sparse metamodel of every model. The method separates the model under test from judges and agents, freezes and hashes plans, refuses to compare values from different contexts, diagnoses the instrument before the system, and applies a null-agent check and a noise rule whose operating characteristics are quantified by simulation. In the evaluated automation conditions, model choices produced larger differences on selected observable outcomes than framework choices, although the experimental design does not establish a general causal ranking of these factors. The experiments also show that instruction tuning is deployment-specific and that system-reported success can exceed independently observed success: of 216 migration units checked against a real Oracle database, 108 were demonstrably correct. These measurements establish application-specific observations, not a universal model ranking.
