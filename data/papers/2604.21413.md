# An Alternate Agentic AI Architecture (It's About the Data)

- arXiv ID: `2604.21413v1`
- Authors: Fabian Wenz, Felix Treutwein, Kai Arenja, Çagatay Demiralp, Michael Stonebraker
- Published: 2026-04-23
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2604.21413v1) | [pdf](https://arxiv.org/pdf/2604.21413v1)

## Abstract

For the last several years, the dominant narrative in "agentic AI" has been that large language models should orchestrate information access by dynamically selecting tools, issuing sub-queries, and synthesizing results. We argue this approach is misguided: enterprises do not suffer from a reasoning deficit, but from a data integration problem.
  Enterprises are data-centric: critical information is scattered across heterogeneous systems (e.g., databases, documents, and external services), each with its own query language, schema, access controls, and performance constraints. In contrast, contemporary LLM-based architectures are optimized for reasoning over unstructured text and treat enterprise systems as either corpora or external tools invoked by a black-box component. This creates a mismatch between schema-rich, governed, performance-critical data systems and text-centric, probabilistic LLM architectures, leading to limited transparency, weak correctness guarantees, and unpredictable performance.
  In this paper, we present RUBICON, an alternative architecture grounded in data management principles. Instead of delegating orchestration to an opaque agent, we introduce AQL (Agentic Query Language), a small, explicit query algebra - Find, From, and Where - executed through source-specific wrappers that enforce access control, schema alignment, and result normalization. All intermediate results are visible and inspectable. Complex questions are decomposed into structured, auditable query plans rather than hidden chains of LLM calls.
  Our thesis is simple: enterprise AI is not a prompt engineering problem; it is a systems problem. By reintroducing explicit query structure, wrapper-based mediation, and cost-based optimization, we obtain the breadth of agentic search while preserving traceability, determinism, and trust in enterprise environments.
