# One Gate Is Not Enough: Composing Stateful Pre-Action Controls for Agentic AI

- arXiv ID: `2608.18360v1`
- Authors: Gaston Besanson
- Published: 2026-08-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CY`
- Links: [abs](http://arxiv.org/abs/2608.18360v1) | [pdf](https://arxiv.org/pdf/2608.18360v1)

## Abstract

Agentic AI systems take consequential actions governed by more than one pre-action control at once: authority, resource, and evidence gates that can admit, degrade, or remediate an action before it executes. This paper's central object is remediation-induced control coupling: a remediation applied by one control can change the action, evidence, or context another control evaluates, invalidating that control's earlier judgment. We formalize this coupling and give a remediate-and-regate protocol that restores per-action soundness in the current bounded, idempotent setting under its stated assumptions. We further show that the two implemented remediation operators (evidence substitution and resource-budget downroute) do not commute -- a finite-model checker finds concrete counterexample instances -- making remediation order part of the control-plane semantics rather than an implementation detail. A governed evidence buffer that trusts its own most recent admitted write is a further instance of the same problem at the level of state -- current admissibility does not imply future reference trustworthiness -- and is vulnerable to poisoning from declared-uncovered defect classes; two mitigations reduce, not eliminate, that exposure. Supporting results establish the exact condition under which positive-weight linear aggregation of gate outcomes can compensate a member veto, a unified cross-control Evidence Set, and that composition manufactures no new detection coverage, reported honestly. Empirically, on a deterministic open-data artifact composing three published engines unmodified, CH1-CH5 meet their registered decision rules across all 30 pre-registered seeds; CH6 does so under W1 but not under the smaller W2 workflow, reported as such. This is a mechanism demonstration on open payload data with a synthetic metadata layer, not a claim about production prevalence.
