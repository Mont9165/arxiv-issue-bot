# Knowledge-Graph-Guided Retrieval-Augmented LLMs for Explainable Root Cause Analysis in Automotive HiL Validation

- arXiv ID: `2608.11277v1`
- Authors: Hamza Ouarrad, Mohammad Abboush, Andreas Rausch
- Published: 2026-08-11
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.11277v1) | [pdf](https://arxiv.org/pdf/2608.11277v1)

## Abstract

Hardware-in-the-Loop validation of automotive software systems generates large multivariate time-series recordings whose manual analysis is time-consuming and often limited to anomaly detection and fault classification rather than root-cause analysis. Although deep learning methods have shown strong performance in fault detection and classification, they usually require task-specific training or retraining when new fault locations, systems, or operating conditions are introduced. They also tend to treat localization as a classification task, without explicitly representing the spatial and functional relationships between fault locations, sensors, and downstream subsystem effects. This limits their generalizability and their usefulness for engineering root cause analysis and diagnosis. This paper proposes a knowledge-graph-guided retrieval-augmented large language model framework for RCA (root cause analysis) and fault localization in automotive HiL data. The method converts raw time-series recordings into compact diagnostic evidence, enriches this evidence with sensor-to-location and propagation knowledge, and retrieves similar historical cases to support the final reasoning step. The LLM is then used as a decision and explanation layer rather than as a direct time-series classifier, producing a ranked fault-location prediction together with an interpretable RCA explanation. The framework is evaluated on two automotive HiL case studies: an ASM gasoline engine and an electric vehicle system. The best-performing model achieves Top-1 accuracies of 90\% and 94\%, respectively, while recording-level aggregation reaches perfect file-level fault localization in the evaluated subset. These results demonstrate the potential of KG-guided RAG-LLM reasoning for explainable and generalizable HiL RCA.
