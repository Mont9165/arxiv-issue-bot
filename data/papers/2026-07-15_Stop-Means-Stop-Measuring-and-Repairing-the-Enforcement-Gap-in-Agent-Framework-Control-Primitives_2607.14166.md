# Stop Means Stop: Measuring and Repairing the Enforcement Gap in Agent-Framework Control Primitives

- arXiv ID: `2607.14166v1`
- Authors: Sajjad Khan
- Published: 2026-07-15
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2607.14166v1) | [pdf](https://arxiv.org/pdf/2607.14166v1)

## Abstract

Production LLM-agent frameworks expose control primitives -- human-in-the-loop approval gates, run cancellation, and execution timeouts -- whose names and documentation imply barrier semantics: while a run is paused, cancelled, or timed out, no gated side effect executes. We show this implied contract holds on none of the six widely used open-source frameworks we test. Model-free differential probes isolate a recurring sibling leak -- an approval gate suspends its own branch while a sibling branch's effect executes during the pause, so a later rejection cannot prevent it -- in every framework shipping a pre-execution gate (five of six), plus three further gaps: replay double-execution, cancellation orphans, and timeout zombies. The hazard is reachable, not merely constructible: under an a-priori-fixed protocol, frontier models emit the leak-triggering plan shape at pooled rates up to 14%, and when live models drive the unmodified frameworks under an approval pause, 215 of 1,200 runs execute their effect during the pause, across three schedulers and two language runtimes. To repair the measured gaps we present SOUNDGATE, an environment-external effect gate in Rust through which every side effect must be admitted, enforcing hold-until-decided, reject-cancels, dedup-on-replay, and fence-on-cancel -- one property per violation class -- under a stated complete-mediation contract discharged for network egress by kernel-enforced routes. We verify the properties over a model of the admission core (Verus; TLA+/TLC, exhaustive to 7.5e7 states; TLAPS), model-check the deployed Rust with Loom, and bridge model to code by differential conformance over 1.2e7 operations -- refinement evidence, not a mechanized proof. SOUNDGATE blocks every measured violation end-to-end on all six frameworks while releasing legitimate effects, at about 1 ms admission per write and 12k-26k durable admissions per second.
