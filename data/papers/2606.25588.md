# IntentTester: Intent-Driven Multi-agent Framework for Cross-Library Test Migration

- arXiv ID: `2606.25588v1`
- Authors: Yi Gao, Ziyuan Zhang, Xing Hu, Xiaohu Yang, Xin Xia
- Published: 2026-06-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.25588v1) | [pdf](https://arxiv.org/pdf/2606.25588v1)

## Abstract

Unit tests capture both functional checks and domain-specific knowledge, but this knowledge remains locked within individual projects and is rarely reused across libraries with overlapping functionality. Existing migration techniques based on structural code mappings (e.g., API signatures) often break down under divergent designs or cross-language settings, resulting in non-executable migrated tests. In this paper, we present IntentTester, a multi-agent framework for intent-driven test reuse. Instead of translating raw code, IntentTester abstracts tests into a language-agnostic Test Description Language (TDL), aligns them with semantically related entities and dependencies in a repository graph, and synthesizes executable tests through LLM-guided reasoning and iterative validation. This design enables cross-library and cross-language migration without manual intervention, producing migrated tests that existing structure-mapping approaches cannot achieve. We evaluate IntentTester on nine open-source projects across three domains (JSON, HTML, and Time) and two languages (Java and Python). IntentTester generates 2,776 syntactically correct tests with 85\% correctness; in comparison, the two baselines achieve 51\% and 43\%. Among them, 2,410 tests executed successfully, yielding a 74\% effectiveness rate. Beyond higher success rates, IntentTester also surfaced previously unknown defects including stack overflows, null dereferences, and parsing inconsistencies, several of which have been acknowledged or patched by maintainers. Our results show that intent-driven migration shifts the focus from code mappings to semantic alignment, allowing practical cross-library and cross-language test reuse while improving test quality and exposing implementation flaws.
