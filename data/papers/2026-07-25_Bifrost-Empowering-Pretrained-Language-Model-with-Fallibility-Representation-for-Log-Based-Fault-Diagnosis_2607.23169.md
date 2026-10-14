# Bifrost: Empowering Pretrained Language Model with Fallibility Representation for Log-Based Fault Diagnosis

- arXiv ID: `2607.23169v1`
- Authors: Minghua He, Tong Jia, Lingzhe Zhang, Chiming Duan, Xinlong Zhao, Leyi Pan, Cheng Wang, Kangjin Wang, Yinghao Yu, Liping Zhang, Yifan Wu, Ying Li
- Published: 2026-07-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.23169v1) | [pdf](https://arxiv.org/pdf/2607.23169v1)

## Abstract

Log-based fault diagnosis is crucial for runtime debugging and maintenance. Existing fault diagnosis methods use language models pre-trained on natural language (PLMs) for log representation. However, system faults are reflected in the multi-level structure of system logs. PLMs pre-trained on natural language struggle to comprehensively capture multi-level fault information, failing to meet the requirements of fault diagnosis. We refer to this information as fallibility representations. To address this problem, we propose a novel log representation learning method, Bifrost. It draws inspiration from the log analysis experience of Site Reliability Engineers and meticulously designs strategies based on self-supervised contrastive learning to learn the fallibility representations of logs. Across three public systems and one industrial ML-as-a-Service system, the log representations produced by Bifrost outperform existing PLMs by average margins of 9.83% in F1 for anomaly detection, 18.28% in HR@k for root cause localization, and 20.88% in Macro-F1 for fault identification.
