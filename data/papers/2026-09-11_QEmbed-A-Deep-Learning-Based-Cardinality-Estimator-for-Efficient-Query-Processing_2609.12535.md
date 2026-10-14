# QEmbed: A Deep Learning Based Cardinality Estimator for Efficient Query Processing

- arXiv ID: `2609.12535v1`
- Authors: Pooja Rajput, Suman Banerjee
- Published: 2026-09-11
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.12535v1) | [pdf](https://arxiv.org/pdf/2609.12535v1)

## Abstract

Cardinality estimation is at the core of any commercial database system for efficient query processing. Over the decades, non-learning-based estimation techniques (e.g., histogram-based, sampling-based) have been widely used in both commercial and open-source database platforms. However, these techniques are only effective when the number of columns in a table is small, as they cannot properly capture dependencies between multiple attributes. Recently, learning-based approaches have been shown to perform significantly better than the heuristic methods that have been used for the past three decades. Despite this success, existing learned models often struggle to balance memory efficiency and accuracy when dealing with datasets that mix high and low cardinality attributes. In this paper, we propose a deep learning model formally called QEmbed. Our model is built upon the Masked Autoencoder for Distribution Estimation (MADE) auto-regressive framework to learn joint data distributions for selectivity estimation. To improve data representation and overcome the limitations of using a single encoding method, we design a hybrid encoding scheme that combines one-hot and embedding encodings. This hybrid design enables QEmbed to retain fine-grained attribute information for smaller domains while capturing compact semantic patterns for large, sparse domains. We capture attribute correlations by factoring the joint data distribution into a series of conditional probabilities. This approach naturally accommodates both point and range queries. Through extensive experiments, we show that while QEmbed faces a latency trade-off on extremely wide schemas, it provides highly reliable cardinality estimates overall. A key advantage of our model is that it reduces extreme tail errors (maximum Q-errors), avoiding catastrophic estimation failures on complex, highly correlated workloads.
