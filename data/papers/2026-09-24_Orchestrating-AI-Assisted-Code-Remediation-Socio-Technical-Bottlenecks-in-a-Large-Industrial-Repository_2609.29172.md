# Orchestrating AI-Assisted Code Remediation: Socio-Technical Bottlenecks in a Large Industrial Repository

- arXiv ID: `2609.29172v1`
- Authors: Andreas Bexell, Lo Gullstrand Heander, Emma söderberg
- Published: 2026-09-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.29172v1) | [pdf](https://arxiv.org/pdf/2609.29172v1)

## Abstract

Background: Code degradation in large, long-lived codebases is costly to remediate through manual refactoring and opportunistic clean-ups. LLM-based coding assistants can perform mechanical remediation at scale, but their impact on industrial workflows is underexplored. Objective: We investigate how massive AI-assisted code remediation affects build-on-commit continuous integration (CI), code review, and team coordination in a large industrial repository, and which socio-technical bottlenecks constrain such remediation when source editing becomes cheap through AI assistance. Method: We report on a 15-day exploratory single-case field study in which an experienced developer used a command-line AI coding buddy to remediate widespread issues in a closed-source industrial C++ repository. We triangulate Gerrit metadata with a developer diary and team chat, analyzed through descriptive statistics and qualitative coding. Results: AI-assisted remediation rapidly generated hundreds of commits touching thousands of lines, saturating CI and reviewer attention. Naïve per-file commits overloaded build-on-commit CI; Switching to directory-based batching and capping the number of files per change restored throughput, but still required explicit review solicitation, negotiation of acceptable commit granularity, and iterative follow-up to resolve build and static-analysis failures. Conclusion: When mechanical editing is cheap, CI capacity, review effort, and change orchestration become primary bottlenecks. Sustainable AI-assisted remediation in very large repositories requires deliberate control of commit, review, and CI batch granularity and treating semantic change sets, such as ``fix all instances of warning X'', as first-class units of work that can be sliced differently for developers, reviewers, and CI.
