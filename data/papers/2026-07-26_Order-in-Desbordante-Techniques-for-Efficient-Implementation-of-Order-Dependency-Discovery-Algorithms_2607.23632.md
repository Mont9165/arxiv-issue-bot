# Order in Desbordante: Techniques for Efficient Implementation of Order Dependency Discovery Algorithms

- arXiv ID: `2607.23632v1`
- Authors: Yakov Kuzin, Dmitriy Shcheka, Michael Polyntsov, Kirill Stupakov, Mikhail Firsov, George Chernishev
- Published: 2026-07-26
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.LG`, `cs.PF`
- Links: [abs](http://arxiv.org/abs/2607.23632v1) | [pdf](https://arxiv.org/pdf/2607.23632v1)

## Abstract

Science-intensive data profiling focuses on discovery and validation of various patterns in datasets. This study considers discovery of one such pattern - order dependency (OD). Simply put, OD states that some list of columns is ordered according to another one. It is of use for database query optimization, data cleaning and deduplication, anomaly detection, and much more.
  Existing discovery methods have approached this problem solely from the algorithmic standpoint, without focusing on the implementation side. At the same time, this problem is very computationally intensive, and therefore this part should not be ignored, as it brings ODs closer to industrial use.
  In this paper, we study two algorithms for OD discovery which target different OD axiomatizations - FASTOD and ORDER. We start by reimplementing these algorithms in C++ in order to speed them up and lower their memory consumption. We then analyze their bottlenecks and propose several techniques which improve their performance even further.
  To perform evaluation, we have implemented these algorithms inside Desbordante - a science-intensive, high-performance, and open-source data profiling tool developed in C++. Experiments have demonstrated a performance improvement of up to 3x obtained by reimplemented versions, and, with the application of our techniques, up to 10x. Memory consumption has been lowered by up to 2.9x.
