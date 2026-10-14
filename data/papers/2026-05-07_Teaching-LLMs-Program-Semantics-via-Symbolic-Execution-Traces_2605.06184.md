# Teaching LLMs Program Semantics via Symbolic Execution Traces

- arXiv ID: `2605.06184v1`
- Authors: Jonas Bayer, Stefan Zetzsche, Olivier Bouissou, Remi Delmas, Michael Tautschnig, Soonho Kong
- Published: 2026-05-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2605.06184v1) | [pdf](https://arxiv.org/pdf/2605.06184v1)

## Abstract

We introduce an evaluation framework of 500 C verification tasks across five property types (memory safety, overflow, termination, reachability, data races) built on SV-COMP 2025, and evaluate 14 models across six families. We find that high overall accuracy masks a critical weakness: while most models reliably confirm properties hold, violation detection varies widely and degrades sharply with program length. To close this gap, we train on formal verification artifacts: running the Soteria symbolic execution engine on generic open-source C code and using the resulting traces for continued pretraining of Qwen3-8B. Just ${\sim}$3,000 bug traces combined with chain-of-thought reasoning at inference time improve violation detection by over 17 percentage points, producing one of the most balanced accuracy profiles among evaluated models. On violation detection, the trained 8B model outperforms the 4$\times$ larger Qwen3-32B without thinking and approaches it in overall accuracy. The interaction between trace training and chain-of-thought is superadditive: neither alone provides meaningful gains, but their combination does. Improvements transfer across all five property types, including ones the training traces do not target. Our 28 configurations confirm the gains stem from trace semantics, not code volume, and that trace curation and format matter.
