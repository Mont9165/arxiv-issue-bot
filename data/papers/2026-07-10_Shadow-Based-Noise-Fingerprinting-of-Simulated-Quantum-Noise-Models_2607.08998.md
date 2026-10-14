# Shadow-Based Noise Fingerprinting of Simulated Quantum Noise Models

- arXiv ID: `2607.08998v1`
- Authors: Vridhi Jain, Lei Zhang
- Published: 2026-07-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `quant-ph`
- Links: [abs](http://arxiv.org/abs/2607.08998v1) | [pdf](https://arxiv.org/pdf/2607.08998v1)

## Abstract

Accurate noise classification is essential for operating near-term quantum processors, yet existing approaches, such as quantum process tomography, scale exponentially with system size, limiting their practicality for routine calibration. We propose a scalable noise fingerprinting pipeline that combines structured classical shadow tomography with physics-informed feature engineering to identify noise channels from a fixed set of 3-qubit probe circuits. Each sample is represented by a 279-dimensional feature vector constructed from randomized Pauli measurements and derived observables, designed to resolve physically similar noise channels that produce overlapping signatures under generic measurement sets. We evaluate three classifiers, i.e., random forest, extra trees, and a multilayer perceptron, on a dataset of 14,000 labeled samples spanning 10 noise types. The random forest classifier achieves the highest test accuracy of 0.8426 with a macro F1 score of 0.8437, outperforming both baselines. Confusion analysis reveals that many noise types are classified with high reliability, with the remaining confusions occurring between channels sharing similar physical decay mechanisms, motivating future work on richer probe states and noise parameter estimation.
