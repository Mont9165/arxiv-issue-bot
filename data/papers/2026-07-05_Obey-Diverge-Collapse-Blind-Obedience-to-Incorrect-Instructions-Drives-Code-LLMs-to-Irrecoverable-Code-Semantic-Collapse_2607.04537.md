# Obey, Diverge, Collapse: Blind Obedience to Incorrect Instructions Drives Code LLMs to Irrecoverable Code Semantic Collapse

- arXiv ID: `2607.04537v1`
- Authors: Raj Jaiswal, Anany Singh Divy, Savar Bhasin, Adi Bajpai, Tanuja Ganu, Rajiv Ratn Shah
- Published: 2026-07-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.04537v1) | [pdf](https://arxiv.org/pdf/2607.04537v1)

## Abstract

Code language models are now trusted collaborators in production workflows for debugging, refactoring, and iterative repair, and every benchmark that evaluates them assumes the instructions they act on are correct. We study what happens when that assumption breaks. We evaluate code language models across four experiments designed to assess whether models resist or obey incorrect instructions in single-pass and iterative repair settings, using the RunBugRun dataset of algorithmic Python problems with deterministic test cases. Our findings reveal a striking behavioral pattern: models correctly identify an incorrect instruction as wrong, then follow it anyway. This compliance unknowingly introduces errors beyond the original bug, and the corrupted code state cannot be recovered through subsequent self-guided iterative repair, which fails to converge across passes. We term this Blind Obedience, characterize the Ghost (Unknown) Errors it introduces, quantify the proportion of cases where semantic corruption proves irrecoverable, and show that extended reasoning cannot reverse it. These findings surface behavioral properties invisible to pass-rate evaluation, with direct consequences for code language models deployed in production settings.
