# BackendForge: Benchmarking Agentic End-to-End Code Generation with Backend Services

- arXiv ID: `2607.11042v1`
- Authors: Yuzhe Guo, Mengzhou Wu, Yuan Cao, Jialei Wei, Dezhi Ran, Wei Yang, Tao Xie
- Published: 2026-07-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.11042v1) | [pdf](https://arxiv.org/pdf/2607.11042v1)

## Abstract

Large language models (LLMs) are increasingly used in agentic coding settings, where they can inspect files, execute commands, run tests, observe failures, and iteratively revise code. This shift raises a central evaluation question: can an agentic LLM generate an end-to-end software artifact that is both deployable and behaviorally correct under execution? Backend services provide a controlled but realistic substrate for this evaluation. Their APIs expose application-level executable semantics, and deployed behavior can be checked deterministically against an OpenAPI contract through black-box HTTP interactions. We introduce BackendForge, a benchmark of 56 contract-defined backend generation tasks rewritten from real open-source applications. Given a visible specification and an OpenAPI contract, an LLM must generate a Dockerized service that is built, deployed, and evaluated only through HTTP tests. To strengthen evaluation without introducing hidden requirements, BackendForge uses a test agent and a code agent to co-evolve the test oracle and reference service, where the test agent proposes specification-grounded backend tests and the code agent repairs the reference implementation. Although the best-performing model, GPT-5.5, succeeds on 55.4\% of tasks under the base oracle, it succeeds on only 28.6\% under the final oracle. This gap suggests that current LLMs can implement many local API behaviors, but still struggle to produce complete backend services.
