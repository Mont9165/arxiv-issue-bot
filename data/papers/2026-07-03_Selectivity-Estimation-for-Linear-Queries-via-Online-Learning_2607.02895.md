# Selectivity Estimation for Linear Queries via Online Learning

- arXiv ID: `2607.02895v1`
- Authors: Fangzhu Shen, Debmalya Panigrahi, Sudeepa Roy
- Published: 2026-07-03
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.02895v1) | [pdf](https://arxiv.org/pdf/2607.02895v1)

## Abstract

Learning-based approaches for selectivity estimation in databases have gained significant traction in recent years. However, theoretical studies of these learning-based approaches are essentially limited to fixed query distributions on static databases. In practice, both the underlying database and the query workload can dynamically change over time. In this work, we propose an algorithmic framework for learning selectivity of queries in this more general dynamic setup. Inspired by online learning, we measure the performance of the learning algorithm in this setting by its regret, which compares the cumulative loss incurred by the learning algorithm to that of the best fixed strategy. We establish upper and lower bounds on regret for histogram-based linear queries, such as point, range, and subset selection queries, under standard loss functions, in both static and dynamic database settings.
