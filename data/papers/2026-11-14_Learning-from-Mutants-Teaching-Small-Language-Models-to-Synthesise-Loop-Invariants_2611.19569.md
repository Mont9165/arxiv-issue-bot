# Learning from Mutants: Teaching Small Language Models to Synthesise Loop Invariants

- arXiv ID: `2611.19569v1`
- Authors: Daragh King, Vasileios Koutavas
- Published: 2026-11-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.19569v1) | [pdf](https://arxiv.org/pdf/2611.19569v1)

## Abstract

Large language models (LLMs) have proven promising for synthesising loop invariants, a long-standing obstacle to automated program verification. Yet, frontier LLMs are typically accessible only through third-party APIs, hampering reproducibility and local deployment. Small language models (SLMs) sidestep these obstacles but require task-specific fine-tuning, for which high-quality training data is needed. We present a failure-driven data curation method for fine-tuning language models to synthesise loop invariants. Inspired by mutation testing, our approach applies semantic mutation operators to ground-truth invariants, producing semantic mutants that induce verification failure. Each mutant is paired with verifier feedback and its ground-truth counterpart, yielding training examples for feedback-guided invariant refinement. Whereas the vast space of mutants is a long-standing burden in mutation testing, it becomes an asset when generating training data, multiplying the examples obtainable from a fixed set of verified programs. We implement our approach for Dafny, augmenting an existing synthetic dataset of verified programs, and introduce a framework that iteratively refines candidate invariants using verifier feedback. On 472 DafnyBench programs, our best-performing fine-tuned Gemma-4-E4B configuration verifies 50.8% of programs zero-shot, compared to 8.1% for the base model, a 6.3$\times$ improvement. Higher-order mutants prove more effective as training data than first-order mutants, and adding mutation-based examples to direct synthesis examples, in which invariants are removed rather than mutated, improves performance under iterative refinement. Our approach also transfers to Qwen3.5-4B, whose zero-shot verification rate rises from 9.3% to 53.6%.
