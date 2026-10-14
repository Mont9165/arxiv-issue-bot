# Metadata Reconstruction from Values Alone: Recovering Column Semantics in Undocumented Warehouses

- arXiv ID: `2608.07946v1`
- Authors: Mike Helwig
- Published: 2026-08-08
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.07946v1) | [pdf](https://arxiv.org/pdf/2608.07946v1)

## Abstract

Text-to-SQL benchmarks ship schemas whose column names already say what the columns mean. Production warehouses are the inverse: cryptic identifiers, partial or absent documentation. We address the problem they pose first: recovering what columns and values mean from the data itself.
  Rosetta places a language model inside a verification harness: a deterministic profiler extracts structural evidence (value fingerprints, a 26-pattern library, checksum verdicts), the model proposes semantics conditioned on that evidence, and every fact carries provenance and a confidence bounded by its evidence class.
  Against human documentation on 680 paired columns across eleven BIRD databases, identifiers destroyed, the harness delivers metadata that is 0.475 accurate on the 42% of columns it commits to, against 0.223 on 94% for the same model used directly. Restricted to the 283 columns where both arms speak, the harness writes no better prose than the model alone; the gain is selection: deterministic evidence governs whether the system speaks (coverage +0.257 [0.128, 0.378]), not how well. The deterministic layer is a competence detector, not a competence amplifier. A backbone swap bounds the claim: the prose finding reproduces, but prompt-requested abstention does not transfer; a code-enforced commit gate (predictions registered first; measured on a third backbone and held-out databases) makes no-evidence coverage 0.000 on every backbone. On a blind i2b2 clinical warehouse Rosetta decodes 95.5% of 134 real ICD-9 codes from values alone and abstains on all 44 NDC drug codes. The catalog supports calibrated abstention at query time: under full schema opacity a naive translator falls from 0.92 to 0.42 execution accuracy while our gate answers at 86% accuracy over 59% coverage. Negative results are reported plainly, including that our own authority ladder is not the mechanism behind the headline.
