# A Universal Cliff and a Design Fingerprint: Cross-Section Defect Detection Under LLM Orchestration

- arXiv ID: `2605.26174v1`
- Authors: Hiroki Fukui
- Published: 2026-05-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2605.26174v1) | [pdf](https://arxiv.org/pdf/2605.26174v1)

## Abstract

Production language-model systems answer a request by partitioning it across an invisible orchestration of worker agents that recompose one integrated report. We ask what this does to a class of defect no single worker can see: a contradiction in the relation between two distant sections of a document. Holding the documents, defects, mechanism, scoring, and seed fixed, we vary only the model -- ten systems across five generations from one developer and five providers from distinct alignment paradigms.
  Two layers separate. First, a universal detection cliff: every model that finds these cross-section defects under a single agent loses that ability under orchestration, detection falling two-thirds or more across every paradigm tested. The cliff is mechanism-derived and not closed by scale or extended reasoning. Second, how models behave once fallen. A signal-detection decomposition shows that, among the six models discriminating above chance, only one developer's generations move along the reporting-criterion axis: as alignment is strengthened, the model misses fewer defects yet raises more false alarms on clean documents -- two faces of one criterion shift, scaling with generation within that developer (p < 0.001) and near-absent elsewhere.
  At the floor the missed defect is often not out of view: the model's private record reconstructs the structural fault accurately, while the integrated report signs off on its soundness, its concern spent on the artifact and an absent collaborator. This resists quantification -- an automated judge is unstable (precision 17-50%) and keywords cannot separate it from ordinary agreement -- a resistance we report as a finding. We release all runs, probes, defect keys, scorer prompts, and scripts. An integrated report's confidence is uninformative about partition-spanning defects, the most aligned systems are not the safest, and the cliff is structural.
