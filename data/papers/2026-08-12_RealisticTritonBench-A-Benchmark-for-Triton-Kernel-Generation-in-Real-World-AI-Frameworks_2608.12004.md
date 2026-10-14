# RealisticTritonBench: A Benchmark for Triton-Kernel Generation in Real-World AI Frameworks

- arXiv ID: `2608.12004v1`
- Authors: Jinjun Huang, Zhongzhen Wen, Tongtong Xu, Meng Yan, Xin Xia, Zhongxin Liu
- Published: 2026-08-12
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.12004v1) | [pdf](https://arxiv.org/pdf/2608.12004v1)

## Abstract

In modern AI frameworks, GPU kernels are key to overall system performance. Combining usability, portability, and near-handwritten CUDA performance, Triton is widely adopted for implementing GPU kernels. Recent advances show the potential of large language models (LLMs) to automatically generate Triton kernels, reducing the manual effort required from expert kernel developers. Several benchmarks evaluate LLM-generated Triton kernels. However, they suffer from three key limitations: (1) they restrict tasks to PyTorch-to-Triton translation, failing to reflect the diversity and complexity of real-world Triton tasks; (2) they evaluate only individual-kernel performance rather than end-to-end performance, the core criterion for real-world deployment in AI frameworks; and (3) they rely on manually written evaluation scripts for individual kernels, which may contain flaws that models can exploit to bypass correctness checks and obtain inflated scores. To address these limitations, we introduce RealisticTritonBench, the first benchmark to derive Triton kernel generation tasks from real-world pull requests in popular AI frameworks, enabling realistic, production-like evaluation. RealisticTritonBench systematically extracts PRs that modify Triton kernels from popular open-source AI frameworks and transforms them into generation tasks with concrete engineering contexts. Each task takes a natural language requirement as input and requires a corresponding Triton kernel implementation, with a complete and reproducible evaluation environment. Unlike prior benchmarks focused on isolated kernel performance, RealisticTritonBench integrates generated kernels into their original frameworks and evaluates them using end-to-end tests, enabling a more faithful assessment. We evaluate leading LLMs on RealisticTritonBench and find that they still struggle with real-world Triton kernel generation tasks.
