# Finding Duplicates in 1.1M BDD Steps: cukereuse, a Paraphrase-Robust Static Detector for Cucumber and Gherkin

- arXiv ID: `2604.20462v1`
- Authors: Ali Hassaan Mughal, Noor Fatima, Muhammad Bilal
- Published: 2026-04-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2604.20462v1) | [pdf](https://arxiv.org/pdf/2604.20462v1)

## Abstract

Behaviour-Driven Development (BDD) suites accumulate step-text duplication whose
  maintenance cost is established in prior work. Existing detection techniques require
  running the tests (Binamungu et al., 2018-2023) or are confined to a single
  organisation (Irshad et al., 2020-2022), leaving a gap: a purely static,
  paraphrase-robust, step-level detector usable on any repository. We fill the gap
  with cukereuse, an open-source Python CLI combining exact hashing, Levenshtein
  ratio, and sentence-transformer embeddings in a layered pipeline, released alongside
  an empirical corpus of 347 public GitHub repositories, 23,667 parsed .feature
  files, and 1,113,616 Gherkin steps. The step-weighted exact-duplicate rate is 80.2
  %; the median-repository rate is 58.6 % (Spearman rho = 0.51 with size). The top
  hybrid cluster groups 20.7k occurrences across 2.2k files. Against 1,020 pairs
  manually labelled by the three authors under a released rubric (inter-annotator
  Fleiss' kappa = 0.84 on a 60-pair overlap), we report precision, recall, and F1 with
  bootstrap 95 % CIs under two protocols: the primary rubric and a score-free
  second-pass relabelling. The strongest honest pair-level number is near-exact at F1
  = 0.822 on score-free labels; the primary-rubric semantic F1 = 0.906 is inflated by
  a stratification artefact that pins recall at 1.000. Lexical baselines
  (SourcererCC-style, NiCad-style) reach primary F1 = 0.761 and 0.799. The paper also
  presents a CDN-structured critique of Gherkin (Cognitive Dimensions of Notations);
  eight of fourteen dimensions are rated problematic or unsupported. The tool, corpus,
  labelled pairs, rubric, and pipeline are released under permissive licences.
