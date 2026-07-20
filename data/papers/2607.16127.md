# CADAQUES: A Cost-Aware Dual Architecture for Query-Efficient Autonomous Discovery

- arXiv ID: `2607.16127v1`
- Authors: Jorge Bravo-Abad
- Published: 2026-07-17
- Primary category: `physics.comp-ph`
- Categories: `physics.comp-ph`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.16127v1) | [pdf](https://arxiv.org/pdf/2607.16127v1)

## Abstract

Autonomous discovery systems couple a resource that answers queries (a simulator, instrument, or analytic model) to an algorithm that selects what to query next. Most software frameworks for this loop inherit the control structure of numerical optimization: campaigns run for a fixed number of iterations, query costs are absent from the programming interface, and decision-making is treated as free. In practice, queries may differ in cost by orders of magnitude, and planners built on large language models or expensive surrogates consume resources of their own. Here we present CADAQUES, an open-source Python framework built on one architectural principle: cost is a first-class primitive of the discovery loop. CADAQUES separates the loop into two structural protocols, an Oracle that answers queries and a Driver that proposes them, and charges both evaluations and decisions against a common vector-valued budget spanning wall time, CPU hours, monetary cost, and language model tokens. An append-only ledger records, for each transaction, the cost declared before execution and the cost settled afterwards, making their discrepancy an observable property of the campaign. We evaluate the architecture by locating the critical temperature of the two-dimensional Ising model from noisy finite-size estimates against the exact thermodynamic-limit reference. In this noisy setting, strategies that concentrate around the best observed result can be misled by noise-induced peaks, whereas a schedule that explores with cheap low-fidelity queries and refines with higher-fidelity ones yields lower and less variable errors than high fidelity throughout, at the studied budget scale. Metering adds tens of microseconds per iteration, three orders of magnitude below the cheapest oracle query. The framework is MIT-licensed and archived at Zenodo (doi:10.5281/zenodo.21293589).
