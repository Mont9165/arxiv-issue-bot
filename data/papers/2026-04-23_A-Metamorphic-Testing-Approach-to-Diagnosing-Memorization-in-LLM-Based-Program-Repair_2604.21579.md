# A Metamorphic Testing Approach to Diagnosing Memorization in LLM-Based Program Repair

- arXiv ID: `2604.21579v1`
- Authors: Milan De Koning, Ali Asgari, Pouria Derakhshanfar, Annibale Panichella
- Published: 2026-04-23
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.21579v1) | [pdf](https://arxiv.org/pdf/2604.21579v1)

## Abstract

LLM-based automated program repair (APR) techniques have shown promising results in reducing debugging costs. However, prior results can be affected by data leakage: large language models (LLMs) may memorize bug fixes when evaluation benchmarks overlap with their pretraining data, leading to inflated performance estimates. In this paper, we investigate whether we can better reveal data leakage by combining metamorphic testing (MT) with negative log-likelihood (NLL), which has been used in prior work as a proxy for memorization. We construct variant benchmarks by applying semantics-preserving transformations to two widely used datasets, Defects4J and GitBug-Java. Using these benchmarks, we evaluate the repair success rates of seven LLMs on both original and transformed versions, and analyze the relationship between performance degradation and NLL. Our results show that all evaluated state-of-the-art LLMs exhibit substantial drops in patch generation success rates on transformed benchmarks, ranging from -4.1% for GPT-4o to -15.98% for Llama-3.1. Furthermore, we find that this degradation strongly correlates with NLL on the original benchmarks, suggesting that models perform better on instances they are more likely to have memorized. These findings show that combining MT with NLL provides stronger and more reliable evidence of data leakage, while metamorphic testing alone can help mitigate its effects in LLM-based APR evaluations.
