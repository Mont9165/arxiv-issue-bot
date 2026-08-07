# Q-ARE: An Evaluation Dataset for Query Based API Recommendation

- arXiv ID: `2605.00472v1`
- Authors: Shenglong Wu, Xunhui Zhang, Tao Wang
- Published: 2026-05-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.00472v1) | [pdf](https://arxiv.org/pdf/2605.00472v1)

## Abstract

As software systems grow in scale, developers face increasing difficulty in selecting appropriate Application Programming Interfaces (APIs) from numerous options. Efficiently identifying APIs that satisfy functional requirements has become a key challenge. To evaluate the semantic understanding of existing query-based API recommendation methods, this paper constructs Q-ARE (Query-based API Recommendation Evaluation), a dataset based on open-source Java projects from GitHub. Methods and their invocation chains are analyzed to identify third-party APIs directly or indirectly invoked by target methods, recursively expanding multi-level invocations to unify hierarchical call structures into API recommendation target sets. Furthermore, we introduce two metrics: API Call Depth, measuring the invocation distance between a query method and a target API, and Invocation Density, quantifying the proportion of code lines associated with the target API in the invocation chain. Based on Q-ARE, we systematically evaluate several query-based API recommendation methods and general Large Language Models (LLMs). Results show that performance drops significantly as API Call Depth increases and invocation density decreases, indicating that existing methods still struggle with multi-level method invocation structures. Q-ARE and its metrics provide a new benchmark for assessing semantic understanding in API recommendation and offer insights for improving future algorithms.
