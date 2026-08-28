# NeuronFuzz: Safety Neuron Guided Fuzzing for LLM Safety Evaluation

- arXiv ID: `2608.26222v1`
- Authors: Zhiyuan Xu, Muhammad Firhard Roslan, Joseph Gardiner, Sana Belguith, Lichao Wu
- Published: 2026-08-26
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.26222v1) | [pdf](https://arxiv.org/pdf/2608.26222v1)

## Abstract

Safety evaluation is critical for assessing whether aligned Large Language Models (LLMs) remain robust against jailbreak attacks. Existing automated testing methods, however, largely rely on response-level feedback: each candidate prompt typically requires generating a target-model response to evaluate its attack effectiveness. This process is expensive and, more importantly, provides only sparse guidance on strongly aligned models, where most candidates are rejected with the same failure outcome.
  This paper presents NeuronFuzz, a white-box fuzzing framework that exploits internal safety neurons as continuous execution feedback for LLM safety evaluation. A SafetyOracle converts safety-neuron activations into a continuous safety alarm score that serves as feedback for fuzzing and can be obtained during prefill, eliminating response generation from the fuzzing loop. To construct the SafetyOracle, NeuronFuzz uses template-invariant harmful and benign inputs and stability-aware selection to identify a compact set of safety neurons whose activations capture harmful-intent recognition. Moreover, since the safety alarm score is differentiable, NeuronFuzz uses its gradients to identify safety-sensitive template positions and a masked language model to generate fluent, context-compatible mutations while preserving original harmful payload and avoiding additional optimization variables. We evaluate NeuronFuzz across 21 text and multimodal models. Across five white-box source models, it achieves a 76-100% jailbreak discovery rate, outperforming baselines by up to 48 percentage points. Its optimized templates further transfer zero-shot to open-weight and six proprietary target models, achieving average ASR and top-5 ensemble ASR (EASR) of 69.6%/92.6% and 44.1%/60.0%, respectively.
