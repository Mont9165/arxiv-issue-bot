# LLM Ensemble Fault Classification for Automotive HiL Validation

- arXiv ID: `2608.10710v1`
- Authors: Hamza Ouarrad, Mohammad Abboush, Andreas Rausch
- Published: 2026-08-11
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.10710v1) | [pdf](https://arxiv.org/pdf/2608.10710v1)

## Abstract

Automotive HiL validation generates large multivariate test recordings whose analysis remains challenging due to manual review effort, rule-based limitations, and the need for explainable diagnostic decisions. Recent machine-learning and deep-learning approaches have improved fault diagnosis, but they often require large labelled datasets, generalise poorly across operating conditions, and provide limited insight into their predictions. This paper proposes an explainable multi-LLM ensemble framework for sensor-level fault classification in automotive validation. The framework uses compact evidence representations of fault-injection recordings and combines the outputs of heterogeneous large language models to improve diagnostic robustness, ranking quality, confidence reliability, and interpretability. The approach is evaluated on gasoline-engine and electric-vehicle HiL systems across three driving settings and ten single-fault classes. Among the individual models, Mistral Small~24B provides the strongest overall single-model trade-off, achieving 0.903 Top-1 accuracy, 0.887 MCC, and the lowest Brier score of 0.102. The final Top-3 ensemble combines Mistral Small~24B, Qwen2.5~32B, and Phi-4~14B using confidence-weighted voting, improving the scenario-averaged results to 0.917 Top-1 accuracy, 0.913 macro F1, and 0.902 MCC, while also providing the best calibration among the tested ensemble strategies. A Top-5 ensemble does not improve over the Top-3 configuration, indicating that model complementarity is more important than ensemble size. The results show that coordinated multi-LLM reasoning can support robust, calibrated, and engineer-interpretable fault classification for automotive HiL validation.
