# A local language model layered with rule-based and neural detectors for clinical text de-identification: an open-source toolkit and evaluation

- arXiv ID: `2611.12709v1`
- Authors: Valentin Burkin
- Published: 2026-11-09
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.CY`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.12709v1) | [pdf](https://arxiv.org/pdf/2611.12709v1)

## Abstract

Objectives: To measure whether a locally hosted large language model (LLM), stacked with deterministic and clinical named-entity recognition (NER) detectors, finds more protected health information (PHI) than open tools, and at what precision.
  Materials and Methods: DeidSharp, an open-source .NET toolkit, combines the findings of pluggable detectors (patterns, a clinical NER model, a local 26B mixture-of-experts LLM) and fails closed on any detector error. Configurations fixed on tuning halves were compared, under a prespecified protocol, with deid, Philter, the Stanford/Penn de-identifier, OpenAI Privacy Filter and GLiNER on reporting halves of PhysioNet's nursing notes (889 spans) and semi-synthetic MIMIC-IV-Note discharge summaries (29,023 spans), and on synthetic ASQ-PHI queries, with paired patient-level bootstrap intervals.
  Results: In the nursing notes, against Stanford/Penn, the recall-first stack found 98.9% of PHI (+2.8, 95% CI 1.4 to 4.4) at 9.3 points lower precision; the precision-first stack, without NER, found 96.5%, matching Stanford/Penn, at 19.6 points higher precision (83.2%). In the discharge summaries, both stacks led Stanford/Penn by more than 20 points (recall-first 95.3%, +21.5, 20.5 to 22.4), almost entirely on generated untyped names; on typed labels all three exceeded 99%. All four prespecified comparisons held. No configuration beat deid significantly on its home corpus; Philter found more discharge-summary spans than the recall-first stack at 23 points lower precision.
  Discussion: The LLM was the main detector and NER added place names; asked to verify its own findings, the LLM discarded a quarter of true PHI.
  Conclusion: A local LLM layered with deterministic detectors offers recall-first and precision-first operating points without sending text off-site.
