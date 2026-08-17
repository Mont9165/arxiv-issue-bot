# Never the Number: Structural Abstention for AI Systems Whose Answers Are Consumed as Fact

- arXiv ID: `2608.13926v1`
- Authors:  Zhelun,  Wu
- Published: 2026-08-14
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.13926v1) | [pdf](https://arxiv.org/pdf/2608.13926v1)

## Abstract

Large language models have made natural language interfaces to databases (NLIDB) newly credible, but LLM text-to-SQL systems fail in a way that matters for deployment: a hallucinated column or a mis-aggregated total yields a fluent wrong answer, indistinguishable at the point of use from a right one. Where the consumer cannot inspect the generated query, as in enterprise AI deployments and operational dashboards, and increasingly where the consumer is a tool-using agent rather than a person, accuracy alone is insufficient: nothing marks which answers to distrust. This is a reliability problem before it is an accuracy problem.
  We propose an architectural pattern for such systems, a trusted kernel with a generative shell, resting on one invariant: a component that can fabricate may influence which question the system answers, never which value it returns. A generative shell interprets underspecified input and phrases replies; a deterministic kernel matches fully specified questions against a bounded set of answerable question shapes and compiles them to queries by deterministic execution. The two meet at a confirmation the user reads before any value is computed, and requests the kernel cannot express are declined rather than approximated. We call this structural abstention, and distinguish it from the statistical abstention of selective prediction and calibrated confidence: refusal here needs no confidence estimate, because unanswerable requests are unrepresentable.
  We specify the pattern implementation-independently, give a five-decision recipe and work it across three domains, extend the invariant from returned values to the actions of agentic systems, and report a two-year production case study alongside two generative alternatives, a fine-tuned parser and a tool-retrieval agent. We close against enterprise and reliability benchmarks published since.
