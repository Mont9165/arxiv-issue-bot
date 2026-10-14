# TLA-Prover: Verifiable TLA+ Specification Synthesis via Preference-Optimized Low-Rank Adaptation

- arXiv ID: `2606.06133v1`
- Authors: Eric Spencer, Arslan Bisharat, Brian Ortiz, Khushboo Bhadauria, TaiNing Wang, George K. Thiruvathukal, Konstantin Laufer, Mohammed Abuhamad
- Published: 2026-06-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LG`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2606.06133v1) | [pdf](https://arxiv.org/pdf/2606.06133v1)

## Abstract

TLA+ is a formal specification language for verifying distributed systems and safety-critical protocols. Large language models (LLMs) frequently produce TLA+ specifications that fail the TLC model checker for semantic reasons. Across 25 LLMs, the best public baseline is 26.6% syntactic parse and 8.6% semantic model-check. We present TLA-Prover, a 20-billion-parameter model for TLA+ specification synthesis. Training combines supervised fine-tuning (SFT) on verified examples with repair-based group-relative policy optimization (GRPO). In the GRPO stage, the model learns to fix its own rejected specifications. We also train a direct preference optimization (DPO) variant from the same SFT checkpoint as an ablation. TLC provides the reward signal directly, with no learned reward model. Four tiers grade each output: Bronze (parses), Silver (no warnings), Gold (passes TLC), and Diamond. To reach Diamond, the model's correctness property is automatically altered in a small way; TLC must then detect a violation. If TLC still passes, the property was always-true and contributes nothing; the output fails Diamond. TLA-Prover reaches 9/30 (i.e. pass@1 = 30%) at both Gold and Diamond on a held-out 30-problem benchmark. This is roughly 3.5x the 8.6% untuned baseline. The DPO variant reaches 20% at Diamond. Gold and Diamond coincide at every checkpoint; this prevents the trivial-property failure mode.
