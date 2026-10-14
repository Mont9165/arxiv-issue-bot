# CogScale: Scalable Benchmark for Sequence Processing

- arXiv ID: `2605.19758v1`
- Authors: Yannis Bendi-Ouis, Romain de Coudenhove, Xavier Hinaut
- Published: 2026-05-19
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`, `stat.ML`
- Links: [abs](http://arxiv.org/abs/2605.19758v1) | [pdf](https://arxiv.org/pdf/2605.19758v1)

## Abstract

The ability to maintain and manipulate information over time is a fundamental aspect of living beings and Artificial Intelligence. While modern models have achieved remarkable success in tasks like natural language processing, evaluating the capacity of novel architectures to process sequential information remains computationally expensive and time-consuming. Testing a new architecture often requires scaling up to massive datasets and models, leading to vast computational costs and slow iteration cycles. In this paper, we propose CogScale, a benchmark of 14 scalable synthetic tasks designed to isolate and evaluate specific cognitive and memory abilities at different parametrizable scales. By providing a standardized, lightweight framework, CogScale allows researchers to rapidly validate architectural innovations before committing to large-scale training. To establish a solid baseline, we evaluate seven distinct architectures: Gated Recurrent Unit (GRU), Long Short-Term Memory (LSTM), xLSTM, Echo State Network (ESN), Mamba, Transformer Decoder, and Transformer Encoder-Decoder. These evaluations are conducted under strict parameter budgets (1k, 10k, and 100k) and across different difficulty levels and scales. Our results show that while classical RNNs and Echo State Networks excel at basic retention within strict parameter budgets, only attention mechanisms and modern state-space models consistently maintain high performance as reasoning complexity and task difficulty scale.
