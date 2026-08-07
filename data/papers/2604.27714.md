# How Code Representation Shapes False-Positive Dynamics in Cross-Language LLM Vulnerability Detection

- arXiv ID: `2604.27714v1`
- Authors: Maofei Chen, Laifu Wang, Yue Qin, Yuan Wang, Bo Wu, Dongxin Liu
- Published: 2026-04-30
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.27714v1) | [pdf](https://arxiv.org/pdf/2604.27714v1)

## Abstract

How code representation format shapes false positive behaviour in cross-language LLM vulnerability detection remains poorly understood. We systematically vary training intensity and code representation format, comparing raw source text with pruned Abstract Syntax Trees at both training time and inference time, across two 8B-parameter LLMs (Qwen3-8B and Llama 3.1-8B-Instruct) fine-tuned on C/C++ data from the NIST Juliet Test Suite (v1.3) and evaluated on Java (OWASP Benchmark v1.2) and Python (BenchmarkPython v0.1).
  Cross-language FPR reflects the joint effect of training-time and inference-time representation, not either alone. Text fine-tuning drives FPR upward monotonically (Qwen3-8B: 0.763 zero-shot, 0.866 pilot, 1.000 full-scale) while F1 remains stable (0.637-0.688), masking the collapse. We argue surface-cue memorisation is the primary mechanism: text fine-tuning encodes C/C++-specific API names and syntactic idioms as vulnerability triggers that fire indiscriminately on target-language code. A cross-representation probe, applying text-trained weights to AST-encoded input without retraining, isolates this: Qwen3-8B FPR drops from 0.866 to 0.583, and 37.2% of false positives revert to true negatives under AST input alone. Direct AST fine-tuning does not preserve the benefit (FPR at least 0.970), as flat linearisation introduces structural surface cues of its own. The pattern replicates across both model families. On BenchmarkPython the AST probe yields FPR=0.554, within 2.9 percentage points of the Java result, despite maximal surface-syntax differences, substantially weakening a domain-shift explanation. These findings motivate a pre-deployment consistency gate, running alerts through both text and AST paths, as a retraining-free filter for false-positive-sensitive settings, at the cost of reduced recall.
