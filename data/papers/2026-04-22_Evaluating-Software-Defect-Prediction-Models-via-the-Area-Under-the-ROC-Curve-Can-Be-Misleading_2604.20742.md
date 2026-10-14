# Evaluating Software Defect Prediction Models via the Area Under the ROC Curve Can Be Misleading

- arXiv ID: `2604.20742v1`
- Authors: Luigi Lavazza, Gabriele Rotoloni, Sandro Morasca
- Published: 2026-04-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.20742v1) | [pdf](https://arxiv.org/pdf/2604.20742v1)

## Abstract

Background: Receiver Operating Characteristic (ROC) curves are widely used to evaluate the performance of Software Defect Prediction (SDP) models that estimate module fault-proneness, i.e., the probability that a module is faulty. A ROC curve maps a model's performance in terms of True Positive Rate and False Positive Rate for any possible threshold set on fault-proneness. The Area Under the ROC Curve (AUC) summarizes the performance of a model across all possible thresholds. Traditionally, ROC curves completely above the bisector of the ROC space are considered better than random, and high AUC values are associated with good performance. Aim: We investigate whether these beliefs are correct, hence if SDP model evaluation based on ROC curves and AUC is reliable. Method: We decorate ROC curves by highlighting the points corresponding to threshold values. We also represent True Positive Rate and False Positive Rate as functions of the threshold. Thus, we can evaluate whether a model classifies both faulty and non-faulty modules better than the random model. Results: We show that commonly used evaluation criteria may lead to wrong conclusions. Conclusions: A high value of AUC does not guarantee that both the True Positive Rate and the False Positive Rate of a model are better than the random model's for all possible thresholds. Either decorated ROC curves or alternative representations are needed to appreciate all the relevant aspects of SDP models.
