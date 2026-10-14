# ScratchLens: Lens-Parametric Behavioral Equivalence for Scratch Programs

- arXiv ID: `2606.15817v1`
- Authors: Yuan Si, Jialu Zhang
- Published: 2026-06-14
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.15817v1) | [pdf](https://arxiv.org/pdf/2606.15817v1)

## Abstract

Two Scratch programs can be syntactically far apart-renamed variables, split scripts, extracted custom blocks, or reordered initialization-and still behave identically; a one-block edit, such as replacing a blocking broadcast with an asynchronous one, can create divergences visible only under specific schedules. Deciding behavioral equivalence is central to automated feedback, grading support, and repair validation, yet tree differencing is too strict and single-run dynamic comparison is unsound for concurrent, random, and timing-dependent behavior.
  We observe that equivalence for block-based programs is lens-parametric: final state, frame traces, monitors, event causality, and debug traces induce different observation relations. SPECTRA makes this explicit through a taxonomy of causal divergence phenomena and observation lenses. It compiles Scratch projects into a causal IR of typed resources and semantic transactions, canonicalizes renamings, guards, and procedure bodies, quotients same-trigger concurrency with Mazurkiewicz trace normal forms, separates program order from races, and handles residual frontiers through SMT obligations and VM-backed counterexample-guided refinement. Conclusive verdicts carry evidence: equivalence by bijection and trace quotient, difference by a typed witness, and unresolved cases remain unknown.
  On a VM-witnessed mutation corpus from real Scratch projects, SPECTRA decides all 444 validated pairs and makes 0/158 false-equivalence claims on witnessed-different pairs under strict scoring. Structural, dynamic-only, and LLM baselines fail on the classes predicted by the taxonomy; ablations quantify the contribution of partial-order reduction and lens parametricity; and targeted scenarios expose ambiguous-mutant divergences missed by random testing.
