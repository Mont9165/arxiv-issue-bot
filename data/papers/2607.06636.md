# Specification Grounding Drives Test Effectiveness for LLM Code

- arXiv ID: `2607.06636v1`
- Authors: Amin Haeri, Mahdi Ghelichi
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.06636v1) | [pdf](https://arxiv.org/pdf/2607.06636v1)

## Abstract

Large language models frequently generate code that appears correct on typical inputs yet fails on edge cases, invalid inputs, and other specification-defined corner conditions. A popular fix has the model write its own tests and repair until they pass, but the source of the gain is unclear: does it come from the tests merely existing, or from their grounding in a specification of what the code should do? We isolate this factor. Holding the tester, test budget, and repair loop fixed, we change a single prompt line that controls whether the tester receives the spec as a checklist of rules. The baseline is strong: it is already told to probe invalid inputs and edge cases. Grounding the tests in the spec produces correct code +38 percentage points more often than this baseline across three Claude tiers (Haiku 4.5, Sonnet 4.6, Opus 4.8), and +36 points on a held-out set. Grounding, not test quantity, is the primary driver: doubling the test budget barely helps, and combining eight independent ungrounded suites plateaus far below grounding. An ablation isolates the spec's content, not its format: given the spec as a plain paragraph the tester recovers 27 of 30 bugs, but asked to plan tests without the spec it recovers only 2 of 30. The effect survives stronger baselines: a property-based generator catches 28 of 30 bugs but invents out-of-spec requirements, and an AlphaCodium-style loop only matches the baseline. It replicates across vendors (GPT-5.3-codex +28, Gemini 3.5 Flash +19), with a task-level sign test over 18 tasks significant at p=0.002. Grounding improves both sensitivity and precision: it catches more real bugs and wrongly rejects far less correct code, cutting the false-alarm rate from 33% (68% against a Python standard-library oracle) to 0%. On well-specified algorithmic problems it neither helps nor hurts.
