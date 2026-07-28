# Metamorphic Testing for Clinical ML Models: A Framework Proposal and Pilot Study

- arXiv ID: `2607.22984v1`
- Authors: Jie JW Wu, Feiyu E, Bo Chen
- Published: 2026-07-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.22984v1) | [pdf](https://arxiv.org/pdf/2607.22984v1)

## Abstract

Machine learning models for clinical prediction tasks, such as in-hospital mortality and sepsis onset, routinely achieve high AUROC scores. However, AUROC measures ranking performance rather than clinical sensibility. A model may rank patients correctly overall while predicting a lower mortality risk when a patient's SOFA score worsens, contradicting established medical knowledge.
  This paper proposes applying metamorphic testing (MT) to clinical machine learning models to evaluate behavioral correctness without requiring ground-truth labels for individual predictions. We design a catalog of 12 candidate metamorphic relations (MRs) for three ICU prediction tasks using the MIMIC-III and MIMIC-IV datasets, with each MR grounded in an authoritative clinical guideline. We further propose a five-layer validation strategy to ensure that MRs are clinically sound before deployment.
  As a feasibility study, we evaluate the approach on the UCI Heart Disease dataset. Although the three clinical models achieve strong predictive performance (AUROC = 0.849-0.900), they exhibit MT violation rates ranging from 27% to 87% across five pilot MRs. An injected-fault experiment further shows that a sign-negation error in a blood pressure feature remains undetected by AUROC but increases the MT violation rate by 31-67 percentage points. These findings suggest that metamorphic testing provides a valuable complement to conventional performance metrics for assessing the behavioral correctness of clinical prediction models.
