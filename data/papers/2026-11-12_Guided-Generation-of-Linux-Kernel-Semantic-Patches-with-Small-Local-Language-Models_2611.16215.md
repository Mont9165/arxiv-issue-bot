# Guided Generation of Linux Kernel Semantic Patches with Small Local Language Models

- arXiv ID: `2611.16215v1`
- Authors: Mohanned Ahmed
- Published: 2026-11-12
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.16215v1) | [pdf](https://arxiv.org/pdf/2611.16215v1)

## Abstract

When a Linux kernel API changes, hundreds of drivers are converted by hand over months, and the earlier conversions are reviewed examples for the later ones. We ask whether small open language models running on a laptop can turn such examples into Coccinelle semantic patches, the rules kernel maintainers already use for tree-wide changes. We adapt guided code generation to this task: the training examples are decomposed by script into a tree of change variants, the model writes one small rule per variant under feedback from applying it to the examples, deterministic components repair SmPL syntax and generalise driver-specific names, rules are composed greedily, and a compile critic repairs or rejects a rule whose output does not build. We evaluate on a pre-registered test set of 7 migrations whose new APIs appeared after the training cutoffs of all three models (Qwen2.5-Coder 7B, Llama 3.1 8B, Gemma 3 4B), with 122 held-out driver conversions, counting a conversion as solved only if the rule's output matches the human fix and compiles. With the framework, Qwen2.5-Coder solves 35.3 conversions on average over three seeds (range 32-41), against 1.0 when prompted directly; Spinfer solves 41 and a frontier LLM agent 66. The local model solves fewer conversions than Spinfer but its rules are the most precise on the test set (0.74 of the files they change are solved, against 0.55 for Spinfer and 0.70 for the frontier agent), and the compile critic removes every output that matches the human fix but does not build. The two general-purpose models stay weak even with guidance (at most 12 solved). All code, prompts, model responses and results are released.
