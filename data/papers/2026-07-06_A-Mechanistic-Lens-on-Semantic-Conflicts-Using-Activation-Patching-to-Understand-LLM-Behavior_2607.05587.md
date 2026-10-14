# A Mechanistic Lens on Semantic Conflicts: Using Activation Patching to Understand LLM Behavior

- arXiv ID: `2607.05587v1`
- Authors: Youssef Abdelsalam, Norman Peitek, Anna-Maria Maurer, Marvin Wyrich, Sven Apel
- Published: 2026-07-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.05587v1) | [pdf](https://arxiv.org/pdf/2607.05587v1)

## Abstract

Large language models (LLMs) are increasingly used in software-engineering tasks processing executable code and non-executable semantic cues such as comments or identifiers. These two sources can conflict when semantic cues suggest different program behavior than the code itself. It remains unclear how such semantic conflicts affect LLM behavior and which source dominates their outputs.
  We present the first controlled, mechanistic study of LLM behavior under semantic conflicts. To this end, we construct 45 Python snippet triplets that isolate conflicts by varying either semantic cues or implementation while keeping token-aligned pairs for causal intervention. We evaluate four open-weight LLMs on two tasks (output prediction and unit-test generation) using behavioral performance measures and residual-stream activation patching to identify token-layer states that causally contribute to behavioral differences between aligned and conflicting inputs.
  Our results show that semantic conflicts significantly reduce execution-grounded correctness in both tasks and that all tested LLMs often follow misleading semantic cues. Residual-stream activation patching reveals a consistent pattern for final-output prediction: The changed cue/code region and a small set of intermediate tokens carry most of the recoverable causal signal before aggregation near the output readout. For unit-test generation, this pattern extends beyond the prompt, showing that conflict-related information is recoverable at generated sites before producing expected values. Overall, our findings show that semantic conflicts affect program comprehension and downstream tasks, with relevant information concentrated in a small number of causally active residual-stream states, and demonstrate a framework for mechanistically analyzing how LLMs integrate code-related information under controlled semantic variations.
