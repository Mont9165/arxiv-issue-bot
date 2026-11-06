# RouteAlign: Aligning Task Requirements with Model Profiles for LLM Service Selection

- arXiv ID: `2611.08162v1`
- Authors: Jihao Zhao, Ding Chen, Yanfang Chen, Bo Tang, Feiyu Xiong, Junchi Yan, Zhiyu Li
- Published: 2026-11-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2611.08162v1) | [pdf](https://arxiv.org/pdf/2611.08162v1)

## Abstract

LLM service selection requires performance evidence that reflects the demands of the current task. Aggregate scores obscure differences in capability and difficulty, while semantically related examples can involve different combinations of skills. We present RouteAlign, which uses task requirements to structure both the measurement of model performance and the selection of services. Task requirements describe capability demand and difficulty, enabling alignment with corresponding model performance measurements. Historical requirements determine how outcomes contribute to global profiles and local capability estimates; incoming requirements determine how those measurements inform the current decision. A shared scorer integrates the evidence, and a generation-cost preference controls selection among eligible services. Evaluation across diverse tasks and heterogeneous LLM services shows that RouteAlign extends the empirical quality-cost frontier toward higher task quality. Comparisons with open Jev-style decision backends show consistent quality gains, with lower generation cost than their strongest tested configuration. Ablations support the contribution of local performance evidence, while catalog-update experiments demonstrate effective reuse of the fitted scorer with refreshed model measurements.
