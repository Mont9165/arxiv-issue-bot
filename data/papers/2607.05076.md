# Can Code Specify a System Precisely Enough to Formally Verify It?

- arXiv ID: `2607.05076v1`
- Authors: Jean-Jacques Dubray
- Published: 2026-07-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.FL`
- Links: [abs](http://arxiv.org/abs/2607.05076v1) | [pdf](https://arxiv.org/pdf/2607.05076v1)

## Abstract

Formal verification is seldom applied to production software, because writing and maintaining a model has historically cost more than it returns. A companion study [1] extended SysMoBench [4] with a lower-cost alternative: specifications are graded against traces captured from the running system. It found that when large language models write the specifications, reliability is governed by the structure of the specification contract, not the language. This paper evaluates both on production software: the payment workflow of an operational restaurant point-of-sale system, which must keep the register, payment terminal, and payment processor in agreement. We report three results. First, the core protocol is correct relative to a hand-built, line-cited model under a precisely stated failure model. The audit found seven failure-handling gaps, nearly all with a common root cause; three were reproduced as real executions, and a patch closing them was re-checked with all failure gates enabled, after which a follow-up patch closed a defect the re-check itself exposed. Systematic extensions of the failure model (crash-restart, stale reads, two attempts) each found the windows they were designed to probe. Second, a single probe of the production payment sandbox exposed a response-shape divergence that makes an entire recovery ladder unreachable against the live API. The emulator-based audit could not detect it, because code and emulator share the same misreading: a correlated-oracle failure. Third, the companion study's central finding replicates across seven models from two vendors: contract structure, not language, governs what LLMs specify reliably. The replication concerns the ordering of contracts and the failure taxonomy, not the absolute level: only the strongest models reached the corpus ceiling, and the harder task restores discriminating power the benchmark had lost.
