# Agentic Method for Deterministic Validation of Legacy Code Migration

- arXiv ID: `2607.28271v1`
- Authors: Andras Ferenczi, Jordan Docherty, Mariya Bessonov, Matthew Findlay, Krishna Lingamneni
- Published: 2026-07-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.28271v1) | [pdf](https://arxiv.org/pdf/2607.28271v1)

## Abstract

Migration of legacy COBOL programs to Java requires extensive testing to ensure correct functionality. This effort is often complicated by the lack of test data and the difficulty of validating all corner cases. In this paper we propose a novel agentic test-synthesis method, the "Locksmith Loop," which is initiated by preparing two runtime environments: the COBOL source and the generated Java target are each instrumented with mocks and executed off-mainframe on commodity hardware, then an iterative agentic loop performs Witness Search over input mocks to penetrate program branches, followed by parity-preserving mutations. When routing boundaries are reached, an analyzer identifies a Locked Paragraph: a condition preventing deeper exploration. Across three COBOL-Java case studies, spanning two open-source programs and one internal production-like COBOL program and ranging from 430 to 4,114 source lines, Locksmith consistently improved coverage beyond input-search plateaus, reaching nearly complete coverage on the two open-source programs and 91.90% branch coverage on the internal production-like COBOL program. The generated Java matched the COBOL reference under deterministic parity checks in all accepted test cases. Through these findings we demonstrate, to the best of our knowledge, a novel approach for validating agentic coding output using a deterministic oracle.
