# Testing Neural Networks via Bayesian-Guided Exploration of Decision Landscapes

- arXiv ID: `2606.04314v1`
- Authors: Bin Duan, Meiru Che, Guowei Yang
- Published: 2026-06-03
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.04314v1) | [pdf](https://arxiv.org/pdf/2606.04314v1)

## Abstract

As neural networks are increasingly deployed in safety-critical domains, testing is essential to evaluate and improve their reliability. Existing testing methods, whether black-box or white-box, primarily use global mutation or coverage-guided strategies, both of which struggle to efficiently uncover diverse model failures while remaining proximate to the original data distribution and semantics. We propose BayesWarp, a testing framework that addresses this limitation by mutating decision-critical input regions identified via interpretable saliency techniques and adaptively guiding the testing process using an uncertainty-aware Bayesian Optimization strategy, enabling the discovery of diverse failures while preserving distributional and semantic proximity to the original data. Evaluation on MNIST, CIFAR-10, and ImageNet across six neural network models shows that BayesWarp improves failure discovery, failure diversity, test case quality, and critical neuron coverage under a fixed mutation budget. These results demonstrate that BayesWarp improves testing effectiveness. Moreover, fine-tuning with the generated failure cases leads to improvements in model performance.
