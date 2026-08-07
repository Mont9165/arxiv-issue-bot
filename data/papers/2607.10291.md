# Partial Contracts Suffice: Sound, LLM-Inferred Regression Verification

- arXiv ID: `2607.10291v1`
- Authors: Yiannis Charalambous, Rafael Menezes, Youcheng Sun, Lucas C. Cordeiro
- Published: 2026-07-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.10291v1) | [pdf](https://arxiv.org/pdf/2607.10291v1)

## Abstract

Software evolves continuously, yet ensuring that a patch preserves intended behavior without re-verifying an entire codebase remains difficult. Regression verification addresses this problem, but existing techniques require expensive whole-program reasoning or rely on manually written specifications that are rarely available in practice. We present the first contract-based regression verification tool. Contract soundness is ensured by proving all function versions match the behavior. The contract then verifies program flow via assume-guarantee. We ask whether a partial, caller-sufficient contract, rather than a full behavioral specification, is enough. On Frama-C-Problems we strengthen each inferred contract past what the caller needs and measure how much tighter it becomes. It barely moves: for most targets in every model the caller-sufficient contract is already the tightest the loop reaches, and our tightness comparator rates the partial and strengthened contracts equivalent for the large majority of targets it can compare. Partial-spec contracts thus capture nearly all the attainable tightness, so stopping at caller-sufficiency costs almost nothing. The regression check underneath is sound: on the third-party EqBench-C suite it never fabricates an equivalence, returning zero false proofs and reporting an unprovable difference instead. It also surfaced nine pairs that EqBench mislabels as equivalent, more than a concurrent tool reports. The contracts themselves are inferred automatically from the checker's own counterexamples, with no separate specification step; on Frama-C-Problems and the ANSSI X509 parser this reaches a verification rate comparable to tools AutoSpec and Preguss, while a passing result certifies at least as strong a property, which we call \emph{safety-preserving conditional equivalence}: enforcement plus caller-sufficiency.
