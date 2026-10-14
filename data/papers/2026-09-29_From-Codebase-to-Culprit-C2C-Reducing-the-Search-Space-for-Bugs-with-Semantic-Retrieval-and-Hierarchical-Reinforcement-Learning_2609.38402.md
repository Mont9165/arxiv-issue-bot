# From Codebase to Culprit (C2C): Reducing the Search Space for Bugs with Semantic Retrieval and Hierarchical Reinforcement Learning

- arXiv ID: `2609.38402v1`
- Authors: Ankur Garg, Corey Yang-Smith, Rishav Rishav, Ahmad Abdellatif, Samira Ebrahimi Kahou
- Published: 2026-09-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2609.38402v1) | [pdf](https://arxiv.org/pdf/2609.38402v1)

## Abstract

We introduce C2C (From Codebase to Culprit), a framework for precise bug localization that progressively reduces the debugging search space across multiple levels of granularity: files, functions, and lines of code. To mirror developer's natural top-down debugging workflows, C2C integrates semantic retrieval and Hierarchical Reinforcement Learning (HRL) in a two-stage process. First, it performs recall-oriented retrieval of buggy candidates via semantic vector similarity search using bug-report text, including available stack-trace information, against a database of embeddings, where the embeddings are fine-tuned via contrastive learning with CodeBERT. Building on this reduced search space, the HRL framework incrementally localizes bugs, reasoning from files to functions and ultimately to individual lines of code. Unlike prior approaches which operate at a single granularity, C2C enables multi-resolution localization while maintaining contextual consistency across decisions. Experiments on real-world Java and Python datasets demonstrate that C2C improves retrieval precision and localization accuracy. Ablation studies further highlight the contributions of hierarchical decomposition, structured learning signals, and reward shaping in advancing multi-level bug localization.
