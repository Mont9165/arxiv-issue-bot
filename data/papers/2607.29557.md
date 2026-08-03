# Alteron: A Tool for Behavioral Regression Testing Across NLP Classifier Versions

- arXiv ID: `2607.29557v1`
- Authors: Shazzad Hossain, Proma Chowdhury, Mridha Md. Nafis Fuad
- Published: 2026-07-31
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.29557v1) | [pdf](https://arxiv.org/pdf/2607.29557v1)

## Abstract

Evaluating evolving Natural Language Processing (NLP) models is important for ensuring reliable behavior across updates, but standard benchmark metrics do not fully capture how model behavior changes across versions. Existing work has focused mainly on testing models in isolation rather than comparing successive versions in continuous integration workflows. We present Alteron, a tool for detecting behavioral regressions across NLP model versions with metamorphic testing. Alteron constructs a test corpus from labeled source examples and compares model versions on metamorphically transformed inputs. In an evaluation spanning 10 metamorphic relations (MRs), 4 model versions, and 3 model-update transitions, Alteron identified 16 behavioral regressions, 11 of which were release-blocking. The results show that common model updates can preserve overall task performance while still introducing undesirable behavior changes, and that behavioral checks across model versions can reveal failures that aggregate benchmark metrics alone do not capture. The tool is open-source and available at https://github.com/shazzad5709/alteron. A screencast demonstration is available at https://youtu.be/szwiWW5O4do.
