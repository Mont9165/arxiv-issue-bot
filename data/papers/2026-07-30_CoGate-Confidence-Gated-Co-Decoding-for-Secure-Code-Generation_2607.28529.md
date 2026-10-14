# CoGate: Confidence-Gated Co-Decoding for Secure Code Generation

- arXiv ID: `2607.28529v1`
- Authors: Minghao Hu, Lannan Luo, Allen Roush, Phillip Howard
- Published: 2026-07-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.28529v1) | [pdf](https://arxiv.org/pdf/2607.28529v1)

## Abstract

Large language models are widely used for code generation, but they can also produce insecure programs due to patterns learned from their pretraining data. Decoding-time steering has become an important solution to this problem: a small expert model is combined with the target model at each step to generate more secure code, which is referred to as co-decoding. However, the acceptance rule for existing co-decoding approaches does not consider the expert model's confidence. When the security expert is unconfident due to unseen patterns or out-of-distribution (OOD) contexts, its guidance can therefore be misleading. To address the challenge, we propose CoGate, a confidence-gated co-decoding approach that controls the expert's influence on the co-decoding process based on its confidence. We implement our approach and evaluate it across multiple LLM backends (CodeGen, DeepSeek-Coder, Qwen-Coder, StarCoder) on several code generation benchmarks (HumanEval, security suite, and CWEval). Our approach outperforms existing co-decoding methods (CoSec+) across multiple benchmarks, achieving up to a 12.6% gain of Func-Sec@10 on CWEval.
