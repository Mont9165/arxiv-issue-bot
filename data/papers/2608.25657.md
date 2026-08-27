# Narcissus: Program Synthesis Using Context-Aware LLM Approximations

- arXiv ID: `2608.25657v1`
- Authors: Tilman Hinnerichs, Sebastijan Dumancic, Neil Yorke-Smith
- Published: 2026-08-26
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.LG`, `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.25657v1) | [pdf](https://arxiv.org/pdf/2608.25657v1)

## Abstract

Large language models (LLMs) excel at programming, but not when the task fixes the target language: prompted with a grammar rare in their training data, their programs usually break the grammar or fail the given specification. Enumerative synthesizers search the space of syntactically correct programs systematically guided by LLMs; the state of the art guides them by approximating LLM proposals into rule frequencies, which loses where each construct belongs and prunes every rule the proposals miss, exactly when the proposals are wrong. We present Narcissus, a synthesizer that keeps the proposals as syntax trees and scores each expansion of a candidate program in its context: does a proposal with the same surrounding structure continue the same way, and does the expansion rebuild a fragment the proposals repeat? A regularization term keeps every rule reachable, so wrong proposals delay the solution but cannot hide it. Across five domains and two search backends, Narcissus beats static guidance at every budget and consistently outperforms re-prompting the LLM to fix its own proposals; it reaches proposal-like programs an order of magnitude sooner and solves $40\%$ of ARC tasks where the raw proposals solve $13\%$, all without a single LLM call during search.
