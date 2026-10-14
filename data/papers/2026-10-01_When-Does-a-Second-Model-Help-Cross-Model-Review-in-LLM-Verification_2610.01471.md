# When Does a Second Model Help? Cross-Model Review in LLM Verification

- arXiv ID: `2610.01471v1`
- Authors: Tae-Eun Song
- Published: 2026-10-01
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.01471v1) | [pdf](https://arxiv.org/pdf/2610.01471v1)

## Abstract

Large language models now generate code, documentation, and analyses, and are increasingly used to review such output. We ask when a second review by a different model helps. Building on the author's earlier preprints, which varied context, repetition, and role structure within one model, we test model independence in a controlled experiment: 30 artifacts with 150 planted errors, 10 review conditions, and 900 review sessions with three reviewer models from two developers. In this experiment, (1) a top-tier cross-model reviewer is not significantly different in F1 from same-model review in a fresh session (CCR), which does not establish equivalence; (2) the two find partly different errors (Jaccard 41.2%); and (3) at two review calls, one CCR plus one cross-model review matches more planted errors than two CCR reviews (56.7% vs. 42.7%; Holm-adjusted p=.006), but not significantly more than two reviews by the top-tier cross-model reviewer, so model difference and reviewer capability are not separated. A lightweight cross-model reviewer scores no higher than same-model review. Withholding requirements from the reviewer raises F1 for the two lower tiers but not the top tier, in untested point estimates whose pattern depends on how failed sessions are scored. Before analysis we audited all session records, excluding one baseline run of uncertain provenance and 14 failed calls; results with all sessions are also reported. A partial check on public detector outputs from another benchmark neither replicates nor contradicts the main comparison. Records, artifacts, and scripts are available from the author on request.
