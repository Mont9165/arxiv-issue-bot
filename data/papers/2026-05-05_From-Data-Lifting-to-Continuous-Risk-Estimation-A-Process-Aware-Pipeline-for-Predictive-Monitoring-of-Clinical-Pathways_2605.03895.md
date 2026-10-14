# From Data Lifting to Continuous Risk Estimation: A Process-Aware Pipeline for Predictive Monitoring of Clinical Pathways

- arXiv ID: `2605.03895v1`
- Authors: Pasquale Ardimento, Mario Luca Bernardi, Marta Cimitile, Samuele Latorre
- Published: 2026-05-05
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.03895v1) | [pdf](https://arxiv.org/pdf/2605.03895v1)

## Abstract

This paper presents a reproducible and process-aware pipeline for predictive monitoring of clinical pathways. The approach integrates data lifting, temporal reconstruction, event log construction, prefix-based representations, and predictive modeling to support continuous reasoning on partially observed patient trajectories, overcoming the limitations of traditional retrospective process mining. The framework is evaluated on COVID-19 clinical pathways using ICU admission as the prediction target, considering 4,479 patient cases and 46,804 prefixes. Predictive models are trained and evaluated using a case-level split, with 896 patients in the test set. Logistic Regression achieves the best performance (AUC 0.906, F1-score 0.835). A detailed prefix-based analysis shows that predictive performance improves progressively as new clinical events become available, with AUC increasing from 0.642 at early stages to 0.942 at later stages of the pathway. The results highlight two key findings: predictive signals emerge progressively along clinical pathways, and process-aware representations enable effective early risk estimation from evolving patient trajectories. Overall, the findings suggest that predictive monitoring in healthcare is best conceived as a continuous, dynamically aware process, in which risk estimates are progressively refined as the patient journey evolves.
