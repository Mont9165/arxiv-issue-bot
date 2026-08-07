# Large Databases Need Small, Open-Weight Language Models

- arXiv ID: `2606.31808v1`
- Authors: Parker Glenn, Alfy Samuel
- Published: 2026-06-30
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.31808v1) | [pdf](https://arxiv.org/pdf/2606.31808v1)

## Abstract

Language model systems built around proprietary APIs often operate on a token-based cost model. This becomes prohibitively expensive in the context of large databases, where LM-enhanced relational operators can incur costs exceeding $10,000 for a single set of experiments, hindering thorough research and practical deployment. In this paper, we demonstrate that quantized, open-weight models running locally on just 16GB of VRAM can match or exceed the accuracy of closed-source counterparts at lower latency and a fraction of the price, challenging the prevailing assumption that closed-source LM APIs are necessary for effective LM-database integration. We present and analyze the key system optimizations required to efficiently deploy these open-weight models within an LM-DB system. By integrating these local models into the BlendSQL v0.1.0 framework, we demonstrate a 390x reduction in overall costs and 3.8x reduction in latency compared to a proprietary LM API. We make our code available at https://github.com/CapitalOne-Research/play-by-the-type-rules/tree/main/sembench.
