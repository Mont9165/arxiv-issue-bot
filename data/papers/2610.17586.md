# High-Throughput LLM-Based Compression and What It Takes: A Systems Study of Inference Engines and Entropy Coding Optimizations

- arXiv ID: `2610.17586v1`
- Authors: David Adams, Luisa Neubauer, Ping-Lin Kuo, Mihail Stoian, Thomas Rückstieß, Josif Grabocka, Renata Borovica-Gajic, Andreas Kipf
- Published: 2026-10-13
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.17586v1) | [pdf](https://arxiv.org/pdf/2610.17586v1)

## Abstract

Large language models are attractive text compressors because next-token probabilities can be converted into code lengths. In practice, however, the main bottleneck is often not modeling quality but systems cost: a compressor must obtain logits quickly enough to compete with strong classical baselines.
  This paper examines systems optimizations for LLM-based compression, including multistream pipelined arithmetic coding and target-interval capture, and evaluates their trade-offs across inference engines, configurations and datasets. We evaluate LLM-based text compression on three different inference engines: Transformers, vLLM, and TensorRT-LLM. Notably, we obtain a speedup of 18.84x compared to prior work's Transformers implementation and a maximum recorded inference speed of 181 kilobytes per second at a compression ratio of 7.17, when running on an NVIDIA A100.
