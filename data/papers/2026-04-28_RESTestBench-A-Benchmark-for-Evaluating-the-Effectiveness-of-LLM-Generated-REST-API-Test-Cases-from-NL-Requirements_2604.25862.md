# RESTestBench: A Benchmark for Evaluating the Effectiveness of LLM-Generated REST API Test Cases from NL Requirements

- arXiv ID: `2604.25862v1`
- Authors: Leon Kogler, Stefan Hangler, Maximilian Ehrhart, Benedikt Dornauer, Roland Wuersching, Peter Schrammel
- Published: 2026-04-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.25862v1) | [pdf](https://arxiv.org/pdf/2604.25862v1)

## Abstract

Existing REST API testing tools are typically evaluated using code coverage and crash-based fault metrics. However, recent LLM-based approaches increasingly generate tests from NL requirements to validate functional behaviour, making traditional metrics weak proxies for whether generated tests validate intended behaviour. To address this gap, we present RESTestBench, a benchmark comprising three REST services paired with manually verified NL requirements in both precise and vague variants, enabling controlled and reproducible evaluation of requirement-based test generation. RESTestBench further introduces a requirements-based mutation testing metric that measures the fault-detection effectiveness of a generated test case with respect to a specific requirement, extending the property-based approach of Bartocci et al. . Using RESTestBench, we evaluate two approaches across multiple state-of-the-art LLMs: (i) non-refinement-based generation, and (ii) refinement-based generation guided by interaction with the running SUT. In the refinement experiments, RESTestBench assesses how exposure to the actual implementation, valid or mutated, affects test effectiveness. Our results show that test effectiveness drops considerably when the generator interacts with faulty or mutated code, especially for vague requirements, sometimes negating the benefit of refinement and indicating that incorporating actual SUT behaviour is unnecessary when requirement detail is high.
