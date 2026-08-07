# From If-Statements to ML Pipelines: Revisiting Bias in Code-Generation

- arXiv ID: `2604.21716v1`
- Authors: Minh Duc Bui, Xenia Heilmann, Mattia Cerrato, Manuel Mager, Katharina von der Wense
- Published: 2026-04-23
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.21716v1) | [pdf](https://arxiv.org/pdf/2604.21716v1)

## Abstract

Prior work evaluates code generation bias primarily through simple conditional statements, which represent only a narrow slice of real-world programming and reveal solely overt, explicitly encoded bias. We demonstrate that this approach dramatically underestimates bias in practice by examining a more realistic task: generating machine learning (ML) pipelines. Testing both code-specialized and general-instruction large language models, we find that generated pipelines exhibit significant bias during feature selection. Sensitive attributes appear in 87.7% of cases on average, despite models demonstrably excluding irrelevant features (e.g., including "race" while dropping "favorite color" for credit scoring). This bias is substantially more prevalent than that captured by conditional statements, where sensitive attributes appear in only 59.2% of cases. These findings are robust across prompt mitigation strategies, varying numbers of attributes, and different pipeline difficulty levels. Our results challenge simple conditionals as valid proxies for bias evaluation and suggest current benchmarks underestimate bias risk in practical deployments.
