# LASSO: An LLM-Agent Synthesized System for SQL Validation

- arXiv ID: `2610.38294v1`
- Authors: Shreyas Jadhav, S. Sudarshan
- Published: 2026-10-28
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.38294v1) | [pdf](https://arxiv.org/pdf/2610.38294v1)

## Abstract

The rise of Large Language Models (LLMs) has significantly advanced text-to-SQL capabilities, but generated queries may have errors. Test datasets are important for catching errors, but having only one or a few test datasets leaves many bugs undetected. Effective testing requires multiple test datasets that can expose subtle semantic bugs and edge cases. Recent work on test data generation and equivalence checking has focused on using constraint solvers. However, constraint-based approaches are slow and not scalable. In this paper, we introduce LASSO, a framework inspired by XData, but designed to minimize the use of constraint solvers, instead prioritizing use of data generation strategies based on fast heuristics. LASSO deploys a number of "attack strategies", each targeting a specific class of semantic errors. LASSO code was built using LLM-based agentic coding. We used carefully designed workflows and rules to support effective code generation and to avoid common code generation issues. A large number of internal test cases are included in LASSO to catch errors in generated code, and more are added when we extend LASSO, to avoid subsequent regressions. Our empirical evaluation across multiple benchmarks demonstrates that LASSO outperforms the state of the art, including XData, SpotIT, ParSEval, and Polygon.
