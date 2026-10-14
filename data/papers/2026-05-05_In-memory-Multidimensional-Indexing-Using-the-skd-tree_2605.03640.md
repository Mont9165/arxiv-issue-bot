# In-memory Multidimensional Indexing Using the skd-tree

- arXiv ID: `2605.03640v1`
- Authors: Achilleas Michalopoulos, Dimitrios Tsitsigkos, Nikos Mamoulis
- Published: 2026-05-05
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.03640v1) | [pdf](https://arxiv.org/pdf/2605.03640v1)

## Abstract

In this paper, we revisit the problem of indexing multi-dimensional data in memory for the efficient support of multi-dimensional range queries and nearest neighbor queries. This is a classic problem in main-memory databases, where there is a need for indexing multiple columns simultaneously. Established data structures include the R-tree, kd-tree, quad-tree, and grid-based partitioning. More recently, multi-dimensional learned indexes have also been proposed to address this problem. We propose slicing kd-tree (skd-tree), a variant of the kd-tree, where each node partitions the space of its subtree into multiple slices across a single splitting dimension. By compressing the splitters of the partitions and with the help of data-parallelism, we (i) radically reduce the number of levels of the tree and (ii) limit the number of computations required for multi-dimensional range and proximity queries. The nodes of the skd-tree resemble the nodes of a main-memory B+-tree, however, a different dimension is used at each level. Our novel range and kNN algorithms on the skd-tree apply only a small constant number of SIMD instructions at each node during tree traversal. Our contributions also include a novel top-down construction algorithm, different types of inner and leaf nodes that warrant tree balancing, and a novel update algorithm. Our skd-tree achieves strong performance compared to existing methods, according to our experimental evaluation on real and synthetic datasets.
