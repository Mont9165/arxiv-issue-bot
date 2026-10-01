# Automated Prefetching for Object Spatial Programming Using Temporal Trace Graphs

- arXiv ID: `2609.38439v1`
- Authors: Baichuan Li, Jayanaka Dantanarayana, Savini Kashmira, Lingjia Tang, Jason Mars
- Published: 2026-09-29
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2609.38439v1) | [pdf](https://arxiv.org/pdf/2609.38439v1)

## Abstract

Dependent database accesses can serialize application--database round trips on a request's critical path. Planning across traversal steps requires knowing both which relationships a computation may follow and how discovered objects become subsequent execution contexts. We identify a programming-model contract that exposes this information through inspectable access paths and explicit traversal continuation. We demonstrate this contract in Object-Spatial Programming (OSP), where walkers traverse a typed object graph and execute node-type-specific code. We introduce the Temporal Trace Graph (TTG), a bounded, request-specific graph of candidate objects and traversal-derived transitions. At walker spawn, the TTG Builder composes statically extracted access and continuation rules over the live graph from the request's starting node. An asynchronous prefetcher loads planned objects while the walker executes. We implement TTG in Jac/PostgreSQL and evaluate four applications covering linear, multi-hop, recursive, and value-dependent traversals. TTG improves end-to-end latency in three applications, achieving up to 2.99x speedup over the stock runtime. Comparisons with manually staged prefetching characterize the benefits and costs of automatic cross-step planning. The evaluation also shows that planning overhead can exceed avoided demand latency and that value-dependent control can introduce bounded overfetch.
