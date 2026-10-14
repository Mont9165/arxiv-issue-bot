# EdgeLM: Edge Demonstrations for Language Models' Table Understanding

- arXiv ID: `2608.04390v1`
- Authors: Soroush Omidvartehrani, Mohammadamin Habibollah, Mohammadreza Daviran, Davood Rafiei
- Published: 2026-08-05
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.04390v1) | [pdf](https://arxiv.org/pdf/2608.04390v1)

## Abstract

Large language models (LLMs) perform table-centric prediction through in-context learning, making demonstration selection critical to performance. Existing retrieval methods prioritize similarity to the query, but similar demonstrations often reinforce the model's likely prediction rather than reveal the distinctions needed for difficult decisions. We propose EdgeLM, a retrieval framework that instead selects edge evidence, demonstrations that are both relevant to the query and informative about the decision boundary. EdgeLM retrieves two complementary forms of edge evidence by selecting data edges, nearby examples with different ground-truth labels, and model edges, similar examples previously misclassified by the deployed model. EdgeLM requires neither model retraining nor task-specific engineering. Across five data wrangling tasks, fifteen datasets, and five open-weight and proprietary LLMs, EdgeLM consistently achieves the best or near-best performance in every setting, while ablations show that the two forms of edge evidence provide complementary benefits. Our code and datasets are publicly available at https://github.com/soroushomidvar/EdgeLM.
