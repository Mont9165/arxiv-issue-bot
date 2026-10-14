# Evaluating and Generating Query Workloads for High Dimensional Vector Similarity Search

- arXiv ID: `2606.14511v1`
- Authors: Matteo Ceccarello, Alexandra Levchenko, Ioana Ileana, Themis Palpanas
- Published: 2026-06-12
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.14511v1) | [pdf](https://arxiv.org/pdf/2606.14511v1)

## Abstract

Similarity search lies at the heart of many modern applications, ranging from databases to deep learning to data series analysis. As such, a vast effort has been invested in developing algorithms, data structures and implementations to speed up this crucial subroutine. To empirically validate these approaches, several benchmarking efforts have been initiated covering a wide array of datasets. In this paper, we observe that usually little control is exercised on the hardness of the workloads with which methods are tested and compared. To address this issue, we first evaluate several query hardness measures with respect to their ability to capture the empirical hardness of a query, i.e. the effort invested by an index data structure to provide an answer. Then, we propose two methods, deemed \HephAnn and \HephGrad, for synthesizing query workloads so that they meet a user-specified hardness target. Both methods allow to produce workloads with the desired hardness: we find that \HephGrad is faster, while \HephAnn makes fewer assumptions on the target hardness measure. The resulting workloads can be used to gain insights into the behavior of similarity search algorithms.
