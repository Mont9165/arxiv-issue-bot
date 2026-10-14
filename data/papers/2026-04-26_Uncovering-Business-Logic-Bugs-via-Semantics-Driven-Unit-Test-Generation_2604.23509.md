# Uncovering Business Logic Bugs via Semantics-Driven Unit Test Generation

- arXiv ID: `2604.23509v1`
- Authors: Chen Yang, Junjie Chen
- Published: 2026-04-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.23509v1) | [pdf](https://arxiv.org/pdf/2604.23509v1)

## Abstract

Business logic bugs violate intended business semantics and are particularly prevalent in enterprise software. Yet most existing unit test generation techniques are code-centric, making such bugs difficult to expose. We present SeGa, a semantics-driven unit test generation technique for uncovering business logic bugs. SeGa constructs a semantic knowledge base from product requirement documents, represented as a set of functionality entries that group related requirements under a common business intent. Given a focal method, SeGa retrieves the relevant functionality entries and derives fine-grained business scenarios with explicit preconditions, triggering actions, expected outcomes, and semantic constraints to guide LLM-based test generation. We evaluate SeGa on four industrial Go projects containing 60 real-world business logic bugs. SeGa detects 22-25 more bugs than four state-of-the-art LLM-based techniques and improves precision by 26.9%-34.3%. Deployment across 6 production repositories further uncovers 16 previously unknown business logic bugs that were confirmed and fixed by developers. From our industrial study, we summarize a series of lessons and suggestions for practical use and future research.
