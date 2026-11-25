# Efficient Semantic ORDER BY via Transitivity-Aware LLM Batch Sorting

- arXiv ID: `2611.32073v1`
- Authors: Akinkunle Akintayo Akinola, Arijit Khan
- Published: 2026-11-24
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.32073v1) | [pdf](https://arxiv.org/pdf/2611.32073v1)

## Abstract

Large language models (LLMs) enable declarative semantic sorting through LLM-ORDER BY operators that rank tuples according to natural-language criteria over unstructured data. Executing such operators efficiently is challenging because LLM comparisons are expensive, stochastic, and sometimes inconsistent. Pairwise approaches require many costly calls. Listwise approaches such as external merge sort rank several items per call, but they follow a fixed merge schedule and keep no record of earlier answers: each merge call re-asks orderings that previous calls have already revealed, directly or by transitivity. We present Transitive Batched Sort (TBS), a transitivity-aware physical operator for semantic sorting that records every revealed preference in a global acyclic preference graph and issues a listwise request only for items whose relative order is not yet implied. To scale, TBS stores only directly observed preferences and answers transitivity queries through a memory-efficient reachability index; to handle noisy LLM outputs, it validates responses and rejects cycle-inducing updates. We evaluate TBS on six benchmarks spanning structured sorting, product price ranking, passage ranking, and personalized recommendation with four LLMs. TBS reduces API calls by 12-20x relative to pairwise quicksort and, at the same batch size, uses 1.1-1.6x fewer calls and 1.3-5.3x lower cost than listwise merge sort while achieving competitive or higher ranking quality across most benchmarks; on Amazon it scales to one million products. These results show that reusing previously inferred preference relations, rather than re-querying them, is an effective foundation for scalable semantic ORDER BY operators.
