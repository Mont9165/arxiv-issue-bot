# The Case for Synthesized Data Compression

- arXiv ID: `2610.09913v1`
- Authors: Ivan Iachnyk, Mihail Stoian, Luisa Neubauer, Ryan Marcus, Andreas Kipf
- Published: 2026-10-07
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.09913v1) | [pdf](https://arxiv.org/pdf/2610.09913v1)

## Abstract

Compression is a fundamental tool in data management. Today's compression schemes are generally designed by hand to apply to many different types of data (e.g., run length encoding or arithmetic encoding), leading to a zoo of general-purpose algorithms which work well for many datasets, but may not be optimal for any specific dataset. Inspired by recent advancements in agentic coding, we propose synthesizing custom-tailored data compression algorithms on a per-dataset basis. Unlike prior work using agents to synthesize database components, a data-specific compression algorithm can be fully verified at construction time, alleviating most correctness concerns. Modern file formats, like AnyBlox and F3, allow including the synthesized code alongside the data itself. Experimentally, we show that our synthesis agent can expand the compression-factor/decompression-speed Pareto front, outperforming general-purpose methods by nearly $2\times$ in compression factor.
