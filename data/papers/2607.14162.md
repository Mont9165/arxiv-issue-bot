# Natural-Language to SysMLv2 Translation via Conformance-Driven Iterative Refinement

- arXiv ID: `2607.14162v1`
- Authors: Chance LaVoie, Eladio Andujar Lugo, Taylan G. Topcu, Levent Burak Kara
- Published: 2026-07-14
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.14162v1) | [pdf](https://arxiv.org/pdf/2607.14162v1)

## Abstract

Model-Based Systems Engineering (MBSE) relies on formal system models as primary technical artifacts for representing requirements, structure, and behavior across the system lifecycle. With the standardization of SysMLv2 as a textual language, interest is increasing in translating natural-language descriptions directly into executable models. For practical deployment, generated models must be accepted by industrial modeling environments, not merely satisfy grammar constraints. We present a conformance-checker-driven framework for reliable natural-language-to-SysMLv2 translation that enforces production-level acceptance as the termination condition. The system embeds a SysMLv2 conformance checker within a generate-check-repair loop. Each model is evaluated using the checker, and deterministic diagnostics are incorporated into revisions until zero conformance errors are achieved. Using the production checker as the oracle ensures the framework targets deployability rather than grammar plausibility. We evaluate the approach on the full SysMBench prompt set of 151 prompts across four large language model backends, yielding 604 prompt-model cases. Single-shot generation achieves 51.16% production-conformance acceptance, while our approach achieves 100.00% conformance. By elevating production conformance from a post-processing check to a control mechanism within generation, the framework converts probabilistic outputs into production-accepted SysMLv2 artifacts suitable for loading, visualization, and engineering use.
