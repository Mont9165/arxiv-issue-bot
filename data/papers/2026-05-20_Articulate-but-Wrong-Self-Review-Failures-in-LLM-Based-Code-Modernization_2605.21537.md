# Articulate but Wrong: Self-Review Failures in LLM-Based Code Modernization

- arXiv ID: `2605.21537v1`
- Authors: Gokul Chandra Purnachandra Reddy, Aditya Lolla, Harsha Sanku
- Published: 2026-05-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.21537v1) | [pdf](https://arxiv.org/pdf/2605.21537v1)

## Abstract

Large language model (LLM) agents are increasingly used to migrate legacy code to modern stacks. We ask a deceptively simple question: when an LLM modernizes legacy code, can the same model be relied upon to recognize when its own output silently changes observable behavior? We run 1,980 real modernization calls across 11 production LLMs from 7 distinct families on a balanced 60-snippet legacy-Python-2 corpus, evaluate every output with a type-strict behavioral oracle, and then ask each model to judge whether its own output preserves behavior. We report four findings. (1) Semantic-preservation drift is prevalent and sharply separable from a cleanly-controlled baseline: semantic-trap snippets drift in 39.7% of attempts versus 7.0% on benign-control code that requires no real modernization (+32.7 percentage points; n=660 each). (2) Drift concentrates on specific snippets that fail across models: pairwise model agreement on which snippets are hard is high (mean Pearson r=0.52), and a small core of numeric-semantics snippets fails for nearly every model and every prompt phrasing. (3) Self-review by the producing model is not a reliable safety net: across all semantic drift cases, 31.7% are silently endorsed by the same model that produced them (83/262), and the per-model self-miss rate is strongly bimodal -- ranging from 0% on five models to 100% on one widely deployed model -- with several models explicitly articulating the very Py2/Py3 semantic distinction that broke their output, then declaring behavior preserved. (4) Drift rate is non-monotone in model capability and price: per-model rates range 5.6%-46.7% and do not track model capability cleanly, indicating the failure is task-structural rather than driven by model scale. All code, prompts, the 60-snippet corpus, the behavioral oracle, the output extractor, and the raw model outputs are released.
