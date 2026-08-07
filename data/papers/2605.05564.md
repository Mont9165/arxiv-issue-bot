# Is this Build Failure Related to my Patch? An Empirical Study of Unrelated Build Failures in Continuous Integration

- arXiv ID: `2605.05564v1`
- Authors: Andie Huang, Daniel Alencar da Costa, Grant Dick, Mariam El Mezouar
- Published: 2026-05-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.05564v1) | [pdf](https://arxiv.org/pdf/2605.05564v1)

## Abstract

Continuous Integration (CI) systems often run many builds concurrently. In this setting, a legitimate build failure may not be caused by the code push that triggered it. Such unrelated build failures can waste developer effort because developers must determine whether the failure is actionable for their current change. We study 77,354 CI build failures from seven open source Apache projects to understand and predict unrelated build failures. We find that developers spend a median of 4 hours identifying whether a failure is related or unrelated to their push. We also perform a document analysis of 371 confirmed unrelated build failures sampled from 10,316 potentially unrelated failures. The analysis shows that unrelated test failures account for 20% of the cases in which developers classify build failures as unrelated. To predict unrelated build failures, we extract 33 features from issue reports, issue comments, and commits associated with the triggering push. We build semi-supervised Positive and Unlabeled (PU) learning models for seven Apache projects. The models achieve precision from 0.70 to 0.88, recall from 0.30 to 1.00, F1-score from 0.44 to 0.91, and AUC from 0.63 to 0.97. Feature importance analysis shows that CI latency, repeated error messages, and the number of preceding comments are useful indicators of unrelated build failures. These results show that PU learning can help developers identify build failures that are unlikely to be caused by their current push.
