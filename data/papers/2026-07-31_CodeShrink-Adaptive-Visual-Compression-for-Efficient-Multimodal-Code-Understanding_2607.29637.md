# CodeShrink: Adaptive Visual Compression for Efficient Multimodal Code Understanding

- arXiv ID: `2607.29637v1`
- Authors: Wenxin Tang, Jingyu Xiao, Zhenyu Liu, Zipeng Xie, Junliang Liu, Wang Luo, Yuan Jiang, Yintong Huo, Michael Lyu
- Published: 2026-07-31
- Primary category: `cs.CV`
- Categories: `cs.CV`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.29637v1) | [pdf](https://arxiv.org/pdf/2607.29637v1)

## Abstract

Rendering source code as images offers a promising way to reduce the input costs of Multimodal Large Language Models (MLLMs). Adjusting image resolution can trade visual token cost against content fidelity. However, resolution scaling alone overlooks two sources of inefficiency: blank regions created by line breaks and indentation, and code regions irrelevant to the current instruction. Moreover, the best compression setting varies across inputs, tasks, and models, limiting fixed-ratio strategies. We propose CodeShrink, an adaptive visual compression framework with three components. Blank-Free Rendering replaces whitespace-dependent layouts with compact layouts and explicit structural markers, removing layout-induced tokens. Adaptive Compression Configuration uses a lightweight agent trained with reinforcement learning to predict a per-input setting that balances token efficiency and readability. Dominant Token Selection jointly analyzes the instruction and code image to prune task-irrelevant visual tokens during inference. We evaluate CodeShrink on code question answering, clone detection, and code completion. CodeShrink reduces visual token use by up to 71.2\% while matching or exceeding uncompressed text-only inputs, and consistently outperforms text-based and visual compression baselines across all three tasks. These results show that combining layout compaction, adaptive configuration, and instruction-aware pruning can make multimodal code understanding more efficient. Our code is available at https://github.com/vinsontang1/CodeShrink.
