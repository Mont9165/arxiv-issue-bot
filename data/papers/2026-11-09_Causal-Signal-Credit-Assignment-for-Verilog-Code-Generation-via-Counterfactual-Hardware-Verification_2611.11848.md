# Causal Signal Credit Assignment for Verilog Code Generation via Counterfactual Hardware Verification

- arXiv ID: `2611.11848v1`
- Authors: Yali Du, Ming Li
- Published: 2026-11-09
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.11848v1) | [pdf](https://arxiv.org/pdf/2611.11848v1)

## Abstract

Large language models have improved Verilog generation, yet functional correctness remains difficult to optimize because simulation commonly provides a coarse module-level pass/fail outcome. Such feedback discards useful evidence from partially correct RTL modules and cannot determine whether a source statement is functionally responsible for an observed output behavior. We present a new method named Causal Signal Credit Assignment (CSCA), which is a counterfactual preference-optimization framework for Verilog generation. CSCA first performs continuous signal-level behavioral verification on sampled candidate modules. It then locates output-driving assignment spans and applies five interventions while holding the remaining module and testbench fixed. The resulting changes in signal-level errors are combined with behavioral agreement to form a continuous statement credit, which is mapped to response-token weights for strict weighted direct preference optimization. This enables CSCA to learn from locally supported statements without uniformly reinforcing an otherwise incorrect response. Built on Icarus Verilog and a CodeV-derived corpus, CSCA is evaluated on VerilogEval~2.0 and RTLLM~v2.0, including both code completion and specification-to-RTL tasks. With a Qwen2.5-Coder-7B-Instruct backbone, CSCA leads the evaluated 7B-scale models and remains comparable to the much larger GPT-5.4-mini on the reported Verilog-generation benchmarks.
