# Machine Learning-Based Pre-Test Risk Stratification for PCR-Confirmed Chlamydia Using Patient-Reported Data and Urine Biomarkers

- arXiv ID: `2605.16365v1`
- Authors: Mehrab Mahdian, Marko Lehes, Katrin Krolov, Tamas Pardy
- Published: 2026-05-09
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.16365v1) | [pdf](https://arxiv.org/pdf/2605.16365v1)

## Abstract

Early identification of individuals at elevated risk of Chlamydia trachomatis infection may enable optimal use of molecular testing in resource-aware screening. We evaluate the feasibility of pre-test risk stratification (PTRS) using machine-learning models trained on routinely available, non-invasive clinical data.
  A curated dataset of 93 urine samples with PCR reference labels was analyzed using three feature groups: patient-reported history and symptoms, urine biomarkers from standard urinalysis, and their combination. Five supervised classifiers were evaluated using stratified 5-fold cross-validation with out-of-fold probability estimates. Performance was assessed using area under the receiver operating characteristic curve (AUC) and threshold-dependent metrics, with uncertainty quantified via bootstrap confidence intervals.
  Models using only patient-reported data showed moderate discrimination (AUC up to 0.72). Urine biomarker-based models demonstrated slightly lower peak discrimination but more consistent performance, with ensemble methods yielding the strongest results. Combining feature groups marginally increased the peak AUC and reduced performance variability across models, indicating improved robustness.
  Findings indicate that urine biomarkers provide a reliable predictive signal for PTRS that is complementary to patient-reported information, while feature integration enhances robustness. This work supports the integration of non-invasive, routinely available information for PTRS into screening workflows, including decentralized or home-based PCR contexts, to optimize testing prioritization.
