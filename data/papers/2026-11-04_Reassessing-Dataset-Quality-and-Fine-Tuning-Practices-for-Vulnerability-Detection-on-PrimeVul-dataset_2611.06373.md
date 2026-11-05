# Reassessing Dataset Quality and Fine-Tuning Practices for Vulnerability Detection on PrimeVul dataset

- arXiv ID: `2611.06373v1`
- Authors: Norbert Sándor Szolnoki, Gábor Antal
- Published: 2026-11-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.06373v1) | [pdf](https://arxiv.org/pdf/2611.06373v1)

## Abstract

Recent studies report promising results from supervised fine-tuning of pre-trained code language models for automated vulnerability detection on benchmarks such as PrimeVul. In this paper, we present a large-scale empirical evaluation of both model performance and dataset quality in this setting.
  We systematically fine-tune three widely used encoder models (CodeBERT, GraphCodeBERT, and UniXCoder) across five imbalance mitigation strategies, extensive hyperparameter sweeps, and multiple random seeds, resulting in 770 independent training runs.
  Our results reveal a consistent pattern. While standard metrics such as F1 and ROC-AUC occasionally suggest improvements, security-critical and calibration-aware measures tell a different story. Matthews Correlation Coefficient remains near zero, predicted probabilities are poorly calibrated, and evaluation under strict false-positive constraints reveals high false-negative rates. Neither imbalance handling, threshold optimization, nor post-hoc calibration recovers a meaningful discriminative signal.
  We also conduct a data quality assessment of the PrimeVul benchmark and identify structural issues such as minimal semantic differences between vulnerable and fixed functions, and annotation noise introduced by commit-level labeling.
  These findings suggests that the PrimeVul dataset, in its current form, presents significant challenges for reliable AI-based vulnerability detection in software engineering with the methodologies we used. Our study highlights the need for more robust dataset design, improved evaluation protocols, and rethinking of fine-tuning practices for security-critical tasks.
