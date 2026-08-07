# ATGBuilder: Feature-Assisted Graph Learning for Activity Transition Graph Construction with Seed Supervision

- arXiv ID: `2606.27080v1`
- Authors: Chenhui Cui, Zixiang Xian, Danyu Li, Tao Li, Rubing Huang, Dave Towey, Shikai Guo, Jiakun Liu
- Published: 2026-06-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.27080v1) | [pdf](https://arxiv.org/pdf/2606.27080v1)

## Abstract

Android applications are organized around activities that provide visual Graphical User Interface (GUI) containers that host the UI and handle user interaction events. Activity Transition Graphs (ATGs) have been widely used to model apps' GUI navigation. However, the construction of high-quality ATGs is challenging: ATGs based on static analysis may miss acceptable transitions and may extract infeasible ones; while dynamically explored ATGs can yield incomplete transitions. Recent learning-based approaches can treat ATG construction as a seed-supervised link-prediction task. However, the use of activity-layout and widget-trigger information for ATG construction remains limited. We propose ATGBuilder, a feature-assisted graph-learning approach for seed-supervised ATG construction. ATGBuilder uses a Large Language Model (LLM) to summarize UI activity metadata from layouts into compact textual functionality summaries. ATGBuilder explicitly models widget-trigger information into the edge attribute: It then uses an auxiliary widget-attribute reconstruction objective on this information during model training. ATGBuilder's performance was evaluated across a series of ablations on the frontmatter corpus, and an experiment on benchmark using manually-checked ground-truth ATGs. Experiments on multiple benchmarks show that ATGBuilder significantly outperforms state-of-the-art methods. We further demonstrate its effectiveness by improving automated GUI exploration tools through better navigation guidance.
