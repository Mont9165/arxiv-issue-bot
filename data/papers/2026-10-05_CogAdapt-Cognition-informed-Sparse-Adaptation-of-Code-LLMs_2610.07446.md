# CogAdapt: Cognition-informed Sparse Adaptation of Code LLMs

- arXiv ID: `2610.07446v1`
- Authors: Yueke Zhang, Zihan Fang, Kevin Leach, Yu Huang
- Published: 2026-10-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.07446v1) | [pdf](https://arxiv.org/pdf/2610.07446v1)

## Abstract

Large language models (LLMs) have become increasingly capable of generating code. However, achieving stronger code-generation performance still often relies on costly model adaptation, i.e., fine-tuning pretrained model parameters. Prior studies have shown correspondence between human code processing and neural models' attention or internal computation. Human-aligned learning approaches use cognitive signals to guide training, but typically adapt a large portion of the model, leaving training costs largely unchanged. Human cognitive signals may indicate not only what the model must learn from, but also where adaptation is most useful. We investigate whether human responses during code reading correspond to code-model behavior and can guide selective adaptation without sacrificing performance.
  We present CogAdapt, a cognition-informed framework for task-dependent sparse adaptation of code models. CogAdapt first learns transferable program-level and token-level priors from human Electroencephalography (EEG) and attention data, then combines these priors with the frozen model's response to each coding task to determine how much adaptation to allocate and which transformer blocks should receive updates. During fine-tuning, only the selected blocks are updated, while no new human recordings are required for inference. Across Qwen and GLM, we find consistent correspondence between human reading behavior and Mixture-of-Experts (MoE) computation. CogAdapt achieves the best pass@1 across both LiveCodeBench and BigCodeBench, including gains of 10.86 and 6.29 percentage points over matched regular fine-tuning on LiveCodeBench, while reducing gradient-eligible adaptation parameters by 86.21-87.21%. These results suggest that human comprehension signals can provide useful guidance for making code-model adaptation both more selective and more effective.
