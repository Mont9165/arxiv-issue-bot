# Probabilistic indirect models for undrained shear strength: addressing significant data missing and variability with advanced imputation and machine learning techniques

- arXiv ID: `2608.13934v1`
- Authors: Haibin Xiong, Shaoheng Dai, Peng Lan, Xuzhen He, Chenxi Tong, Sheng Zhang, Daichao Sheng
- Published: 2026-08-14
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.13934v1) | [pdf](https://arxiv.org/pdf/2608.13934v1)

## Abstract

Accurate prediction of undrained shear strength (su) is crucial for geotechnical design, but is often hampered by substantial uncertainty in traditional empirical methods. This study uses the CLAY/10/7490 global database to develop probabilistic indirect models to predict su based on Atterberg limits and piezocone cone penetration (CPTU) measurements. Firstly, the dataset has a high missing data rate and variability. We test three imputation methods - multivariate normal (MN), multiple imputation by chained equations (MICE), and miss forest (MF) - to fill the missing values. To validate their effectiveness, a Probabilistic Extreme Gradient Boosting (PXGB) model is developed, and the imputation methods are evaluated by comparing the PXGB's performance when trained on the imputed datasets against that on the original incomplete data. Secondly, the indirect model is built by integrating a multi-head attention (MHA) mechanism into an artificial neural network (ANN) to enhance information extraction from limited data, which leads to the MHA-based probabilistic neural networks (MHA-PNN) model. The models' performance, alongside a conventional MN-based prediction model, was evaluated using root mean square error (RMSE), coefficient of determination (R2), mean absolute percentage error (MAPE), conditional interval width (wCI), and coverage rate (CR). Results demonstrate that the proposed MN-enhanced MHA-PNN model substantially outperforms other models in both prediction accuracy and uncertainty quantification. These findings highlight the potential of this integrated strategy for building robust probabilistic indirect models in geotechnical applications, particularly when confronted with sparse and incomplete datasets.
