# An Empirical Study on Improving LLM-Based Issue Classification through Domain-Informed Analysis

- arXiv ID: `2611.13470v1`
- Authors: Anubhav Gupta, Tanner Wright, Gema Rodríguez-Pérez
- Published: 2026-11-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.13470v1) | [pdf](https://arxiv.org/pdf/2611.13470v1)

## Abstract

Issue reports that describe Intrinsic Bugs, Extrinsic Bugs, and Not a Bug cases often use similar language, but they might point to different causes and require different maintenance actions. This makes three-way issue classification difficult for Large Language Models (LLMs), particularly when prompt-based refinements begin to plateau. We study whether domain-informed analysis of LLM outputs can improve classification beyond prompt modification alone. Using 428 manually labeled issue reports, we evaluate six LLMs across 18 prompt configurations and analyze 7,704 model-generated rationales to identify recurring failure patterns in how models justify predictions, use evidence, and handle conflicting information. We translate these findings into a multi-stage pipeline that separates bug validity from bug origin. The pipeline improves macro F1 and Extrinsic Bug recall for five of the six models. The strongest pipeline configuration reaches 0.827 accuracy and 0.757 Extrinsic Bug recall, improving over the best-accuracy prompt-only baseline by +1.2 and +7.5 pp, respectively. The decomposition further reveals that bug origin classification is more reliable than validity, indicating that the bug-validity decision accounts for most of the remaining error. These results show that expert failure analysis can support more reliable LLM-based software engineering classifiers.
