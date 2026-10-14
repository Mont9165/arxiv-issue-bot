# Improving Code Translation with Syntax-Guided and Semantic-aware Preference Optimization

- arXiv ID: `2605.13229v1`
- Authors: Yuhan Wu, Huan Zhang, Wei Cheng, Chen Shen, Jingyue Yang, Wei Hu
- Published: 2026-05-13
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.13229v1) | [pdf](https://arxiv.org/pdf/2605.13229v1)

## Abstract

LLMs have shown immense potential for code translation, yet they often struggle to ensure both syntactic correctness and semantic consistency. While preference-based learning offers a promising alignment strategy, it is hindered by unreliable semantic rewards derived from sparse test cases or restrictive reference translations. We argue that a robust semantic reward for code translation must be derived directly from the source code. In this paper, we propose CTO to improve code translation with syntax-guided and semantic-aware preference optimization. Through contrastive learning, we train a cross-lingual semantic model to directly assess functional equivalence between source and translated code. By formulating code translation as a multi-objective optimization problem, this robust semantic signal is seamlessly unified with compiler-based syntactic feedback within the direct preference optimization framework. Extensive experiments on C++, Java, and Python translations demonstrate that CTO significantly outperforms existing baselines and alternative preference optimization strategies.
