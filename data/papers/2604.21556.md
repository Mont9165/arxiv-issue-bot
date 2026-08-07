# Probabilistic Verification of Neural Networks via Efficient Probabilistic Hull Generation

- arXiv ID: `2604.21556v1`
- Authors: Jingyang Li, Xin Chen, Hongfei Fu, Guoqiang Li
- Published: 2026-04-23
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.21556v1) | [pdf](https://arxiv.org/pdf/2604.21556v1)

## Abstract

The problem of probabilistic verification of a neural network investigates the probability of satisfying the safe constraints in the output space when the input is given by a probability distribution. It is significant to answer this problem when the input is affected by disturbances often modeled by probabilistic variables. In the paper, we propose a novel neural network probabilistic verification framework which computes a guaranteed range for the safe probability by efficiently finding safe and unsafe probabilistic hulls. Our approach consists of three main innovations: (1) a state space subdivision strategy using regression trees to produce probabilistic hulls, (2) a boundary-aware sampling method which identifies the safety boundary in the input space using samples that are later used for building regression trees, and (3) iterative refinement with probabilistic prioritization for computing a guaranteed range for the safe probability. The accuracy and efficiency of our approach are evaluated on various benchmarks including ACAS Xu and a rocket lander controller. The result shows an obvious advantage over the state of the art.
