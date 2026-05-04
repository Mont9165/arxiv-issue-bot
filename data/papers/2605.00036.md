# Cross-level Privacy Preserving Utility Mining

- arXiv ID: `2605.00036v1`
- Authors: Jiahong Cai, Wensheng Gan, Philip S. Yu
- Published: 2026-04-28
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.00036v1) | [pdf](https://arxiv.org/pdf/2605.00036v1)

## Abstract

Privacy-preserving utility mining (PPUM) aims to hide sensitive high-utility patterns while preserving the utility of the sanitized database. In practice, however, many datasets are associated with taxonomic information, which makes the identification and processing of generalized items more challenging. To address this, we investigate the cross-level privacy-preserving utility mining (CLPPUM) problem and propose a method for protecting generalized items. Based on different victim item selection strategies, we develop three CLPPUM algorithms: minimum RGISU first (Min-RF), maximum RGISU first (Max-RF), and best NSC first (Best-NSCF). Furthermore, to enable efficient victim item identification, a novel dictionary structure named GI-dic is designed to accelerate the computation of required utility metrics. Experimental results on multiple datasets demonstrate that the proposed algorithms successfully hide all sensitive cross-level high-utility itemsets without introducing artificial itemsets. The results also show that our method performs well on sparse datasets, and both Min-RF and Best-NSCF consistently outperform Max-RF. Overall, Min-RF achieves the best performance, particularly when the minimum utility threshold is low and the dataset is dense.
