# EduPluginBench: Executable Assurance for AI-Generated Educational Plugins

- arXiv ID: `2608.00739v1`
- Authors: Nizam Kadir
- Published: 2026-08-01
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.00739v1) | [pdf](https://arxiv.org/pdf/2608.00739v1)

## Abstract

Code-generation models can produce executable components, but compilation and functional tests do not establish compliance with least privilege, telemetry consent, provenance, privileged-write authority, lifecycle constraints, or bounded failure. We introduce EduPluginBench, an executable benchmark and staged admission method for generated plugins in governed software ecosystems. Across 1,440 activation-checked first-order mutants from 30 specifications, P0-P4 increased release-blocking-defect recall by 74.7 percentage points (specification-clustered 95% CI 73.4-75.8) over P0-P2, with no observed rejection among 120 clean references (95% Wilson upper bound 3.1%). A frozen transfer study of 600 unmodified generations from two current coding models found that 300/600 parsed, but none passed P0 or achieved P0-P4 conformance (95% upper bound 0.64%); downstream assurance estimands were undefined. An independently labelled Moodle study retained 16 vulnerable/fixed pairs; the frozen generic PHP detector found no vulnerable revisions. These negative transfer results prevent controlled contract consistency from being read as independent real-defect effectiveness. An earlier 540-generation diagnostic found that post-hoc bounded repair yielded 112 P0 passes, all nonconforming, with recall increasing from 13.4% to 100%. The artifact retains protocols, public-source provenance, raw generations, row-level decisions, audits, analysis code, and reproduction instructions.
