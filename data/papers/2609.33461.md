# Protected Cores Are Not Enough: Certifying AI-Proposed Revisions of Temporal Specifications

- arXiv ID: `2609.33461v1`
- Authors: Ruggero Lanotte
- Published: 2026-09-27
- Primary category: `cs.LO`
- Categories: `cs.LO`, `cs.AI`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.33461v1) | [pdf](https://arxiv.org/pdf/2609.33461v1)

## Abstract

Runtime monitoring traditionally evaluates a specification that is fixed before execution or externally modified when requirements change. In learning-enabled and data-intensive systems, however, the temporal relationships represented by a specification may themselves evolve. Allowing an AI component to directly replace a formal specification is unsafe: it may overfit transient behavior, weaken protected requirements, or activate statistically unsupported revisions.
  We introduce an intersymbolic architecture in which an untrusted AI proposer suggests temporal specification revisions and a symbolic governor controls their activation. Two results organize the framework. First, origin-version semantics makes the outcome of each obligation invariant to later revisions. Second, aggregate certification can conceal systematic failures on protected triggers; simultaneous aggregate and core-conditional post-selection certification controls both targets. A structural invariant preserves designer-protected components, and a proposer-independent lifetime error bound supports repeated activation decisions. The statistical bound concerns the predictable means of completed certification samples; interpreting it as future operational validity requires an additional stability assumption. Controlled synthetic experiments use a frozen supervised AI proposer to illustrate the masked-core failure at one decision and across repeated governed revisions. The proposer is a supervised regressor trained offline on synthetic tasks and frozen before use; it ranks candidates by predicted aggregate margin and never observes the protected-trigger success rate, so the masked-core failure arises from optimising the aggregate rather than from an adversary constructed by hand.
