# Quipu: A Governed Bitemporal Knowledge Graph Store

- arXiv ID: `2608.16813v1`
- Authors: Steve Brown
- Published: 2026-08-17
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.16813v1) | [pdf](https://arxiv.org/pdf/2608.16813v1)

## Abstract

Agents now write knowledge graphs, but knowledge-graph stores still carry defaults set when humans curated them: accept writes now and clean later, keep one time axis or none, treat every writer's facts as equally trustworthy, and leave governance to dashboards and middleware. These four defaults are individually convenient and jointly untenable under agent workloads. We present Quipu, an embeddable store that inverts all four: no fact enters except through a gate whose predicates evaluate the pending post-state; data, trust labels, verdicts, and the rules themselves are bitemporal; named graphs are the unit of authority and trust, composed under a lattice whose one invariant is that composition never widens; and the governance specification $Σ$, the trace, and signed verdicts are facts in the store they govern, making the audit $T \models Σ$ a query. We evaluate with Census, a deterministic multi-writer lifecycle whose single seeded run scores every research question against planted ground truth: the gated store ends with 0 of 6 planted defects versus 6 of 6 ungated; all 7 composition probes uphold the lattice contract; 50 of 50 satisfied verdicts re-derive faithfully as of their instant while all 50 would be misreported under a latest-only rule set; and the SARC reference checker agrees with the in-store audit verdict-for-verdict, differing only on coverage semantics. A recorded trace from a governed writer surfaces a live enforcement gap the audit names with its remediation. On DEMM-Bench, an external decision-evidence sufficiency benchmark, a content-only reading of the exported records answers all 512 property-level governance questions correctly with zero overclaim under all eight degradation conditions, while container-presence baselines overclaim on up to 87.5% of them -- and the run surfaced, and led us to close, a gap in what a denial's verdict attests.
