# REST API Testing with Verified LLM-Inferred Dependencies and Response-Driven Refinement

- arXiv ID: `2608.17546v1`
- Authors: Tu Nguyen, Thanh Nguyen, Huy Nguyen, Viet Nguyen, Tien N. Nguyen, Vu Nguyen
- Published: 2026-08-18
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.17546v1) | [pdf](https://arxiv.org/pdf/2608.17546v1)

## Abstract

Testing RESTful APIs requires generating sequences of API calls that satisfy dependencies among operations, parameters, and runtime-created resources. Recent LLM-based approaches infer such dependencies and generate test sequences from OpenAPI specifications, but they often treat LLM-inferred relationships as correct without execution-based validation. This can introduce spurious dependencies, miss feasible operation chains, and produce infeasible tests. In this paper, we propose APIPilot}, an execution-validated framework for REST API testing. APIPilot first derives candidate producer-consumer dependencies from OpenAPI specifications using structural heuristics and LLM-based semantic reasoning. It then treats these dependencies as hypotheses and validates them through concrete API executions before using them for test generation. The validated dependencies are organized into a dependency graph from which APIPilot constructs coverage-aware workflows via bounded top-k graph traversal, separating semantic dependency inference from sequence construction. To improve subsequent tests, APIPilot further performs response-driven refinement: runtime responses are analyzed to update resource pools, adjust input-generation constraints, and prune or revise invalid dependency mappings. Empirical evaluation on 16 real-world REST API services shows that APIPilot achieves 92.3% operation coverage, up to 58.6% code coverage, and an 88.1% workflow execution success rate, outperforming both LLM-based and traditional REST API testing baselines. APIPilot also detects 197 unique 5xx failures and specification-execution mismatches, demonstrating the benefit of grounding dependency inference in execution feedback.
