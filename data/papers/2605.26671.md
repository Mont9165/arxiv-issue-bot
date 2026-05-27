# RT-RkNN: Reverse k Nearest Neighbor Queries as a Graphics Ray Casting Problem

- arXiv ID: `2605.26671v1`
- Authors: Zhengyang Bai, Peng Chen, Mohamed Wahib
- Published: 2026-05-26
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.DC`
- Links: [abs](http://arxiv.org/abs/2605.26671v1) | [pdf](https://arxiv.org/pdf/2605.26671v1)

## Abstract

Reverse k nearest neighbor (RkNN) queries are fundamental in spatial databases, location-based analytics, and recommendation systems. Existing state-of-the-art techniques rely on spatial pruning supported by R-trees and their variants. However, their pruning effectiveness degrades significantly in challenging scenarios where the number of facilities is small, the user population is dense, or the value of k is large. To overcome these limitations, this work reformulates the RkNN query problem in two-dimensional geometric spaces as a graphics ray-casting problem, where users are modeled as rays and facilities are represented as geometric primitives. Based on this formulation, the first algorithm and implementation exploiting dedicated hardware ray-tracing cores on modern GPUs are developed. This novel approach preserves strong filtering performance even for large values of k, dense user populations, and highly sparse facility distributions. Extensive experimental results demonstrate that the proposed method outperforms state-of-the-art algorithms across diverse settings, particularly in scenarios where traditional pruning strategies become inefficient.
