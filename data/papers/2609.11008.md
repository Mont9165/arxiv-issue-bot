# DeFiFusion: Combining Transaction Events with Smart Contracts to Detect Price Manipulation Attacks

- arXiv ID: `2609.11008v1`
- Authors: Rui Cao, Shaojing Fan, Liming Fang, Yuchan Liu, Yingying Jiao, Zhenguang Liu
- Published: 2026-09-10
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.11008v1) | [pdf](https://arxiv.org/pdf/2609.11008v1)

## Abstract

Decentralized Finance (DeFi) has emerged as a rapidly growing blockchain-based financial service, where market transaction dynamics and underlying smart contract logic are intricately intertwined. This autonomous interplay, while eliminating centralized intermediaries, significantly expands the vulnerability surface of DeFi protocols to Price Manipulation Attacks (PMAs), which have already inflicted catastrophic financial losses. Despite their gravity, existing detection paradigms suffer from fundamental limitations. Transaction-centric methods lack awareness of contract execution semantics, making them prone to false positives under legitimate market volatility, while static contract analyses ignore real transaction behaviors and frequently report vulnerabilities that are infeasible to exploit in practice. We present DeFiFusion, a dual-modal PMA detection framework that closes this gap by jointly modeling transaction events and smart contract semantics within a unified pipeline. Our core insight is that PMA maliciousness emerges only from the interaction between transaction behaviors and the contract logic they exploit; neither signal suffices in isolation. Accordingly, we derive price-manipulation-aware event encoding for extracting fine-grained temporal and economic features tailored to manipulation patterns. We further introduce LLM-based contract semantic extraction to supply the execution-logic context that prior behavioral methods lack. To fuse these modalities, we propose a Dual-Modal Projection-Fusion Transformer with T5-style relative positional encoding, capturing the cyclic multi-stage execution structures that distinguish PMAs from benign market activity. Extensive experiments demonstrate that DeFiFusion consistently achieves state-of-the-art detection performance, effectively recalling 222 of the 225 PMA cases while maintaining a precision of 96.10%.
