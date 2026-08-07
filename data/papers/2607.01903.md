# Rethinking Complexity Metrics for LLM-Integrated Applications: Beyond Source Code

- arXiv ID: `2607.01903v1`
- Authors: Zihao Xu, Yuekang Li, Gelei Deng, Yi Liu, Zhenchang Xing
- Published: 2026-07-02
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.01903v1) | [pdf](https://arxiv.org/pdf/2607.01903v1)

## Abstract

LLM-integrated applications blend natural language prompts with program code, and much of their runtime behavior originates in the prompt layer rather than in the code itself. Existing complexity metrics, however, operate solely at the code level and therefore overlook this behavioral logic entirely. We present HECATE, the first tool designed to assess complexity in both the prompt and code layers of such applications. Central to HECATE is Prompt-as-Specification, a Hoare-logic-inspired formalism that interprets every prompt as a specification of intended behavior. Grounded in 25 complexity dimensions identified across published taxonomies, the tool generates 52 candidate metrics. We assess each metric against 118 components collected from 18 open-source repositories, relying on maintenance activity derived from version history as an empirical proxy for complexity, and discard any metric that loses significance once code size is accounted for. Only ten metrics withstand this test. Seven belong to our newly introduced set; rather than measuring sheer volume, each tallies structurally distinct elements, such as LLM call sites, memory attributes, and prompt templates, an attribute we call structural breadth. Of the three surviving conventional metrics, RFC exhibits a similar breadth-oriented character, while Halstead N and V survive only as a residual effect of size; our top-performing metrics exceed all three. Crucially, the prompt-layer metrics retain significance even when the strongest code-level metric is added as a covariate, establishing prompt complexity as a dimension in its own right. A final validation on 20 components spanning six held-out repositories shows that the two best-performing metrics continue to predict maintenance effort, supporting their generalizability beyond the training set.
