# Duration-constrained Interval Joins

- arXiv ID: `2608.06856v1`
- Authors: Naoya Ehara, Daichi Amagata
- Published: 2026-08-07
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.06856v1) | [pdf](https://arxiv.org/pdf/2608.06856v1)

## Abstract

Many databases, including temporal, uncertain, spatial, and trajectory databases, use interval data, and interval joins are among the most frequently used operators. Many studies proposed efficient interval join algorithms, but they do not consider the overlap duration. They return any pairs of intervals, even if they overlap very slightly, e.g., with no essential correlation or relationship. Subsequent applications may suffer from such interval pairs, as they may be noise or unnecessary for the analysis. Furthermore, outputting such pairs also increases join time. To address the above issues, this paper addresses the problem of duration-constrained interval join. Given two interval collections $R$ and $S$ and an overlap duration constraint $ε$, this problem returns all interval pairs $(r,s)$ such that $r \in R$, $s \in S$, and the overlap duration between $r$ and $s$ is at least $ε$. A straightforward approach for this problem is to run a state-of-the-art interval join algorithm and then filter qualified interval pairs. However, this is inefficient, as it generates unnecessary interval pairs and incurs duration computations, which cannot overcome the above efficiency concern. We propose an efficient algorithm for this problem that removes the above drawback. Furthermore, we propose two optimization techniques to improve the efficiency of our algorithm. We conduct extensive experiments on three real-world interval datasets, and the results demonstrate that our algorithm outperforms existing techniques applicable to our problem.
