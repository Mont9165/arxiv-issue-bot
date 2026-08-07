# Multi-Agent LLM-based Metamorphic Testing for REST APIs

- arXiv ID: `2605.28321v1`
- Authors: Shehroz Khan, Abdullah Mughees, Gaadha Sudheerbabu, Tanwir Ahmad, Dragos Truscan
- Published: 2026-05-27
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.28321v1) | [pdf](https://arxiv.org/pdf/2605.28321v1)

## Abstract

As REST APIs become an increasingly significant part of software systems, their validation is becoming more critical. Hence, testing and uncovering underlying issues are of utmost importance for improving software quality. However, testing REST APIs is challenging mainly due to the difficulty of assessing whether the output of an API call is correct, i.e., the test oracle problem. Metamorphic testing is a specification-based testing approach for situations where correct outputs are unknown or not specified explicitly. To check the correctness of a system, relations between the different outputs are specified. We present ARMeta, a tool-supported approach that uses an LLM-based multi-agent workflow to support metamorphic testing of REST APIs documented with OpenAPI. The agentic workflow is used to identify metamorphic test scenarios and specify them in the Given-When-Then format. These scenarios are automatically implemented as executable tests and executed against the system under test. We evaluate ARMeta on two publicly available web applications that expose REST interfaces and compare its performance with a scenario-based testing baseline. The results show that ARMeta explores behaviors that serve as a complement to existing scenario-based testing approaches.
