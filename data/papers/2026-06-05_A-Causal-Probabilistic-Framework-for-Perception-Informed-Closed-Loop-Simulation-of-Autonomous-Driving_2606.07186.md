# A Causal Probabilistic Framework for Perception-Informed Closed-Loop Simulation of Autonomous Driving

- arXiv ID: `2606.07186v1`
- Authors: Zhennan Fei, Rickard Johansson, Mikael Andersson, Matthias Eng, Mattias Eriksson, Kaveh Kianfar, Sadegh Rahrovani, Chris van der Ploeg, Michael Borth, Maren Buermann, Michiel Braat, Henk Goossens, Zijian Han, Majid Khorsand Vakilzadeh, Gabriel Rodrigues de Campos
- Published: 2026-06-05
- Primary category: `cs.RO`
- Categories: `cs.RO`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.07186v1) | [pdf](https://arxiv.org/pdf/2606.07186v1)

## Abstract

Software-in-the-loop (SIL) simulation is a cornerstone for the validation of modern automotive safety functions. However, many current frameworks utilize ideal sensing, which bypasses the functional insufficiencies of perception algorithms, leading to over-optimistic safety assessments. This paper proposes a perception-informed SIL testing methodology that bridges the gap between ground-truth simulation and real-world perception behavior. We present a framework for incorporating causal probabilistic models into standardized, scenario-based simulation toolchains, applicable to both Advanced Driver Assistance Systems (ADAS) and Autonomous Driving Systems (ADS). Our approach enables the systematic injection of realistic perception errors, such as loss of detection, sizing inaccuracies, and positioning offsets, derived from physical triggering conditions like fog, rain, and object-merging scenarios. By evaluating these ``faults'' within a standardized simulation environment, we demonstrate that perception-informed testing reveals latent operational risks that ideal SIL environments fail to capture, providing a scalable pathway for SOTIF (ISO 21448) validation.
