# CuEVM: Scaling Smart Contract Execution on GPUs

- arXiv ID: `2611.14916v1`
- Authors: Nhut-Minh Ho, Tien Tuan Anh Dinh, Quang Trung Ta, Fredrik Svantes, Xiaokui Xiao, Beng Chin Ooi
- Published: 2026-11-11
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.CR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.14916v1) | [pdf](https://arxiv.org/pdf/2611.14916v1)

## Abstract

Smart contracts on Ethereum blockchain process transactions worth billions of US dollars daily. They run on top of Ethereum Virtual Machine (EVM) which executes transactions sequentially. This execution model creates a performance bottleneck, especially for new blockchain workloads with large numbers of transactions, such as security testing. We present CuEVM, a GPU-native and semantically complete EVM execution engine that treats transaction execution as a massively parallel data processing problem. It employs novel data structures and GPU-aware scheduling to accelerate execution. Unlike prior works that transpile the contract and rely on a host CPU for many operations, CuEVM supports complete EVM semantics natively on the GPU. It passes 100% of the Ethereum VMTests and 96.2% of the full execution-test suite. On a single commodity GPU, CuEVM executes over 8 million ERC-20 transfers per second, outperforming existing baselines by up to two orders of magnitude. We build a smart contract fuzzer, called CuEVM-fuzz, on top of CuEVM. The fuzzer achieves over a million end-to-end executions per second, up to 23x and 4.8x higher than the state-of-the-art CPU-based and GPU-based baselines, respectively.
