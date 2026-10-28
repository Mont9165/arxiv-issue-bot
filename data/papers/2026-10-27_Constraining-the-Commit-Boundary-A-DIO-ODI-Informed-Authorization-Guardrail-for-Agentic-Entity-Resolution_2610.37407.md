# Constraining the Commit Boundary: A DIO/ODI-Informed Authorization Guardrail for Agentic Entity Resolution

- arXiv ID: `2610.37407v1`
- Authors: Daniel Beránek
- Published: 2026-10-27
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.37407v1) | [pdf](https://arxiv.org/pdf/2610.37407v1)

## Abstract

Agentic Entity Resolution (ER) systems iteratively plan actions, retrieve evidence, revise hypotheses, and propose graph mutations. An erroneous identity hypothesis may condition later retrieval and produce apparent confirmation. This paper proposes a Digital Identity Optimization (DIO) and Ontology of Digital Identity (ODI)-informed authorization boundary between evidence available for agent reasoning and evidence eligible to authorize persistent identity-changing mutations.
  A domain-governed constraint-binding function maps selected reconstruction-failure distinctions to explicit identity-preserving constraints. An abstract two-phase supervisor permits a commit only when claim-specific authorization-eligible evidence supports every required proposition, relevant conflicts are resolved, the operation remains within its authorized scope, and relevant state and policy versions remain valid. Admission as UNVERIFIED does not confer authorization eligibility. Separate claim-specific promotion governs evidentiary use; insufficient support or unresolved material conflict leads to deferral.
  The contribution is a specification connecting diagnostic-to-constraint mapping, evidence promotion, proposition coverage, conflict handling, scope binding, and commit-time version integrity. A proposed evaluation protocol is designed to assess the mapping's incremental value beyond generic authorization and conventional identifier rules. This is a conceptual architecture without implementation or empirical validation, not a theorem of semantic correctness. Its property depends on domain-policy adequacy, evidence promotion, and enforcement. It does not prevent erroneous hypotheses or hypothesis-conditioned retrieval; dependency-aware evidence flow remains future research.
