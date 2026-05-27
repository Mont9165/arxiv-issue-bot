# FuzzPilot: Plateau-Triggered Recipe Validation for Structured Text Fuzzing

- arXiv ID: `2605.26539v1`
- Authors: Zhiyi Yao
- Published: 2026-05-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2605.26539v1) | [pdf](https://arxiv.org/pdf/2605.26539v1)

## Abstract

FuzzPilot is a controller for AFL++ that moves expensive reasoning out of the mutation hot path. When coverage plateaus, it snapshots the corpus, prepares candidate mutation recipes, evaluates them in short isolated AFL++ micro-campaigns, and promotes only recipes with positive validation reward. Recipes are JSON data, not generated code: a native custom mutator consumes operator weights, byte ranges, corpus-selection rules, and dictionary tokens. Candidate recipes can come from local rules or from a language-model agent, with Ghidra-derived constants and decompiled context as target hints. This preprint reports a deliberately narrow cJSON evaluation. We compare vanilla AFL++ and the full FuzzPilot agent over five 14,400 s repetitions per arm. cJSON is saturated: baseline AFL++ reaches the exposed 269-edge ceiling at a median of about 2,500 s. The experiments therefore do not show that language-model proposals improve coverage or generalize beyond cJSON. Within this scope, FuzzPilot preserves throughput (median execs_per_sec about 1.06x baseline), shows a descriptively shorter median plateau (1,384 s versus 2,532 s), but the difference is not statistically significant at N=5 (Mann-Whitney p=0.42). The validation gate evaluated 20 model-proposed recipes and promoted none because all rewards were zero. The observed plateau reduction is more likely due to controller snapshot and restart machinery than to the model or recipe mutator. This version is best read as an auditable implementation report and baseline for ongoing non-saturated-target evaluation.
