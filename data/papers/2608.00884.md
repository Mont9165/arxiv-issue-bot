# Documentation vs. Code Patterns: What Drives LLM-Based Exception Oracle Generation?

- arXiv ID: `2608.00884v1`
- Authors: Soneya Binta Hossain, Matthew B. Dwyer, Tasfia Tasnim
- Published: 2026-08-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.00884v1) | [pdf](https://arxiv.org/pdf/2608.00884v1)

## Abstract

LLM-based test oracle generation (TOG) methods report high accuracy on exception oracle generation, but it remains unclear what evidence drives these predictions. In particular, do models use explicit exceptional-behavior documentation such as Javadoc @throws clauses, or do they rely on recurring patterns in tests, code, and documentation?
  We investigate this question through a large-scale intervention-based study of three TOG systems spanning classifier-based and generative architectures and model sizes from roughly 110M to 7B parameters, evaluated on three real-world benchmarks comprising two generated-test datasets and a new benchmark of developer-written tests. We first remove Javadoc @throws clauses and find that accuracy changes only marginally, with the largest drop below one percentage point. This indicates that structured exception documentation is not the primary driver of exception-oracle prediction. We then apply attribution-guided substitution ablations to identify the signals that predictions depend on. The results show that high accuracy can be driven by shortcut signals: some models are highly sensitive to a small number of structural tokens, while others distribute reliance across many lexical cues. These findings challenge the assumption that strong exception-oracle accuracy reflects robust use of exception semantics. Future TOG systems should therefore be evaluated not only by whether they predict the correct oracle type, but also by whether their predictions are grounded in meaningful exception-triggering evidence.
