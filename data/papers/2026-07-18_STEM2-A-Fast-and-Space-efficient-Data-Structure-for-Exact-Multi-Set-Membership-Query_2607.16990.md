# STEM2: A Fast and Space-efficient Data Structure for Exact Multi-Set Membership Query

- arXiv ID: `2607.16990v1`
- Authors: Niu Yannian, Han Song, Wang Minmei
- Published: 2026-07-18
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DS`
- Links: [abs](http://arxiv.org/abs/2607.16990v1) | [pdf](https://arxiv.org/pdf/2607.16990v1)

## Abstract

Multi-set membership queries are ubiquitous in networking and database systems. Current solutions force a difficult compromise: hash tables guarantee correctness but suffer from high memory footprints, while filter-based approaches optimize space at the cost of probabilistic errors. In this paper, we propose STEM2, a fast and space-efficient data structure that achieves 100% query accuracy and can support dynamic key updates for multi-set membership queries. STEM2 utilizes a balanced binary tree architecture where each non-leaf node incorporates a novel Exact Binary Set Separator (XBSS) to partition keys into two disjoint groups. A key innovation of our design is a minimized hashing scheme that requires only two hash computations per key lookup, significantly reducing computational overhead. Additionally, STEM2 separates the control plane and the data plane: the control plane handles construction and dynamic updates, while the data plane is dedicated to serving efficient membership queries. Extensive experiments show that STEM2 achieves over 120 million operations per second (Mops) in lookup throughput, outperforming the state-of-the-art Coloring Embedder by 20% and the Ludo hashing by up to 21.6X, while maintaining compact memory cost and exact correctness.
