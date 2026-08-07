# Hallucination Inspector: A Fact-Checking Judge for API Migration

- arXiv ID: `2604.20202v1`
- Authors: Marcos Tileria, Santanu Kumar Dash, Profir-Petru Pârţachi, Earl T. Barr
- Published: 2026-04-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.20202v1) | [pdf](https://arxiv.org/pdf/2604.20202v1)

## Abstract

Large Language Models (LLMs) are increasingly deployed in automated software engineering for tasks such as API migration. While LLMs are able to identify migration patterns, they often make mistakes and fail to produce correct glue code to invoke the new API in place of the old one. We call this issue Scaffolding Hallucination, a failure mode where models generate incorrect calling contexts by inventing Phantom Symbols -- such as imaginary imports, constructors, and constants -- that do not exist in the API specification. In this paper, we show that standard metrics cannot be relied upon to detect these instances of hallucination. We propose Hallucination Inspector, a static analysis tool to detect Scaffolding Hallucination in LLM-generated code. Our approach includes a lightweight evaluation framework that verifies symbols extracted from the abstract syntax tree against a knowledge base derived directly from software documentation for the API. A preliminary evaluation on Android API migrations demonstrates that our approach successfully identifies hallucinations and significantly reduces false positives compared to standard metrics and probabilistic judges
