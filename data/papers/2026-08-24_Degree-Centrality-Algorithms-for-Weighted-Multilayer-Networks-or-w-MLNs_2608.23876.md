# Degree Centrality Algorithms for Weighted Multilayer Networks (or w-MLNs)

- arXiv ID: `2608.23876v1`
- Authors: Ayomide Ayowole-Obi, Abhishek Santra, Sharma Chakravarthy
- Published: 2026-08-24
- Primary category: `cs.SI`
- Categories: `cs.SI`, `cs.DB`, `cs.DM`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2608.23876v1) | [pdf](https://arxiv.org/pdf/2608.23876v1)

## Abstract

Centrality measures are defined for simple graphs -- directed, undirected, weighted or unweighted. Attributed graphs have to be reduced to simple graphs for computing centrality measures. However, when applications with multiple types of relationships are modeled using multilayer networks (MLNs), simple graph algorithms cannot be directly used. Existing approaches typically analyze MLNs by aggregating layers of an MLN into a single graph, which results in the loss of structural and semantic information. The semantic information loss can be more pronounced particularly, in weighted networks.
  This work focuses on computing degree centrality in weighted homogeneous multilayer networks (HoMLNs) using a decoupling-based framework. The framework performs independent layer-wise analysis on MLNs without reducing them to simple graphs. The decoupling approach allows use of exiting algorithms for each layer and uses minimal information from individual layers for computing degree centrality of HoMLNs. We propose heuristic-based algorithms that strike a balance between accuracy and efficiency.
  The proposed methods are evaluated against ground truth (GT) results obtained using Boolean OR aggregation and naive baselines. Experimental results on both synthetic and real-world HoMLN datasets demonstrate that the heuristics achieve accuracy comparable to the ground truth while significantly improving computational efficiency, thereby establishing the scalability and effectiveness of the HoMLN algorithms developed using the decoupling approach.
