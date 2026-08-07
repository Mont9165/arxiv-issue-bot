# Context-as-AI-Service: Surfacing Cross-File Dependency Chains for LLM-Generated Developer Documentation

- arXiv ID: `2606.04397v2`
- Authors: Ameya Gawde, Vyzantinos Repantis, Harshvardhan Singh, Lucy Moys
- Published: 2026-06-03
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2606.04397v2) | [pdf](https://arxiv.org/pdf/2606.04397v2)

## Abstract

LLM agents increasingly write and maintain developer documentation, but usefulness and accuracy often rely on dependency chains that are not obvious to follow. Even with more files in context, the agent must still decide which cross-file dependencies to trace. We present Context-as-AI-Service (CAIS), a retrieval layer that LLM agents query to find evidence across the codebase as they review or generate documentation. CAIS indexes source code, API references, and upstream documentation, then enables agents to query the index through tool calls that combine keyword and semantic search. We evaluate CAIS in two case studies using Claude Sonnet 4.6 on a production SDK: improving API reference comments in a core source file and validating an LLM-generated tutorial. In both studies, the baseline already had ordinary repository tools such as file reads, keyword search, and symbol navigation. CAIS adds a retrieval layer on top, so the comparison isolates added retrieval rather than basic repository access. In the API-reference review, the CAIS-augmented agent produced the same 5 missing-documentation fixes as the baseline and surfaced 4 findings the baseline missed: 2 cross-file factual errors and 2 underspecified API comments. In the tutorial validation, it surfaced 1 executable bug, 1 API-usage improvement, and 2 missing prerequisites that the baseline pipeline did not catch. These findings required tracing non-obvious dependency chains across utility files, framework internals, usage examples, tests, and component-creation logic. Over five runs per condition, adding CAIS reduced wall-clock time by 22% to 34% across the two tasks and lowered input-token usage.
