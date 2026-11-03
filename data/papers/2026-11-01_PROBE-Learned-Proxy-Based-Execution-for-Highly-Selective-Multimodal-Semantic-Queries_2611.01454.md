# PROBE: Learned Proxy-Based Execution for Highly Selective Multimodal Semantic Queries

- arXiv ID: `2611.01454v1`
- Authors: Haikai Zhao, Haisheng Fu, Zhengjie Miao, Zhenman Fang
- Published: 2026-11-01
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.01454v1) | [pdf](https://arxiv.org/pdf/2611.01454v1)

## Abstract

Large language models (LLMs) enable semantic queries over unstructured data, but invoking an LLM on every row is prohibitively expensive. Proxy-based execution can reduce this ple with the LLM and training a lightweight proxyto label the remaining rows. Nevertheless, in practical scenarios where semantic queries are highly selective, it remainschallenging to identify representative samples foLM budget and to achieve accurate predictions overthe remaining data using the proxy. We present PROBE, a learned proxy-based execution framework for highly selective multimodal semantic queries. PROBE uses selectivity-adaptive sampling to discover rare polightweight proxy on the acquired labels. It thenrefines proxy predictions through residual correction and homogeneity smoothing over a similarity graph. To address sampling bias, PROBE jointly calibrates refined scores usiarate calibration sample, then selectively routescandidates to the LLM by optimizing the tradeoff between estimated F1 and evaluation cost. On queries from SemBench and LRO-Bench with positive rates as low as 2.17x10^-5 budget yields a geometric-mean F1 of 0.762,compared with 0.797 for exhaustive LLM evaluation, at a geometric-mean speedup of 4.87x and a maximum speedup of 9.3x.
