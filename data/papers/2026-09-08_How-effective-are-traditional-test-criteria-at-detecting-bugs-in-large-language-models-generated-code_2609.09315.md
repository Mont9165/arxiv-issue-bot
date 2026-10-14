# How effective are traditional test criteria at detecting bugs in large language models generated code?

- arXiv ID: `2609.09315v1`
- Authors: Asma Hamidi, Michael Konstantinou, Renzo Degiovanni, Mike Papadakis
- Published: 2026-09-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.09315v1) | [pdf](https://arxiv.org/pdf/2609.09315v1)

## Abstract

Test adequacy criteria are widely used to evaluate and guide software testing. Although prior research has extensively examined these criteria using human-written programs, faults, and tests, the increasing adoption of Large Language Models (LLMs) for code generation raises important questions about their effectiveness in detecting LLM-induced faults. To investigate this, we conduct an empirical study involving 5 LLMs and 4 benchmarks, simulating end-to-end workflows in which both code and tests are automatically generated. We collect 6,000+ faulty program instances and evaluate the effectiveness and efficiency of 3 widely used adequacy criteria: statement coverage, branch coverage, and mutation testing. Our findings reveal several key insights. First, most faults introduced by LLMs are relatively trivial to catch. Second, the challenging faults are difficult to trigger using either traditional coverage-based or mutation-based criteria. Third, actual fault detection rates remain extremely low, often near zero, because test oracles fail to capture faulty behavior triggered by the generated test prefixes, exposing a critical limitation of automated test generation. Fourth, prompt-aware oracles can improve fault detection, but their overall effectiveness remains limited, highlighting the need for users to manually reason about test assertions. We further observe that mutation testing only marginally outperforms traditional coverage criteria in both triggering and detecting faults, raising questions about whether its significantly higher application cost is justified in this context.
