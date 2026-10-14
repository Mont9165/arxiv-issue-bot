# Empirical Insights of Test Selection Metrics under Multiple Testing Objectives and Distribution Shifts

- arXiv ID: `2604.23342v1`
- Authors: Jingyu Zhang, Fan Wang, Jacky Keung, Yihan Liao, Yan Xiao, Lei Ma
- Published: 2026-04-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.23342v1) | [pdf](https://arxiv.org/pdf/2604.23342v1)

## Abstract

Deep learning (DL)-based systems can exhibit unexpected behavior when exposed to out-of-distribution (OOD) scenarios, posing serious risks in safety-critical domains such as malware detection and autonomous driving. This underscores the importance of thoroughly testing such systems before deployment. To this end, researchers have proposed a wide range of test selection metrics designed to effectively select inputs. However, prior evaluations of metrics reveal three key limitations: (1) narrow testing objectives, for example, many studies assess metrics only for fault detection, leaving their effectiveness for performance estimation unclear; (2) limited coverage of OOD scenarios, with natural and label shifts are rarely considered; (3) Biased dataset selection, where most work focuses on image data while other modalities remain underexplored. Consequently, a unified benchmark that examines how these metrics perform under multiple testing objectives, diverse OOD scenarios, and different data modalities is still lacking. This leaves practitioners uncertain about which test selection metrics are most suitable for their specific objectives and contexts. To address this gap, we conduct an extensive empirical study of 15 existing metrics, evaluating them under three testing objectives (fault detection, performance estimation, and retraining guidance), five types of OOD scenarios (corrupted, adversarial, temporal, natural, and label shifts), three data modalities (image, text, and Android packages), and 13 DL models. In total, our study encompasses 1,640 experimental scenarios, offering a comprehensive evaluation and statistical analysis.
