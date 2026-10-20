# Pattern-Driven Evaluation of LLM Code Optimization: Isolating Compiler-Transcendent Semantic Reasoning

- arXiv ID: `2610.24835v1`
- Authors: Wesley Lu, Runzhou Liu, Hongru Du, Xinyao Yi
- Published: 2026-10-17
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.24835v1) | [pdf](https://arxiv.org/pdf/2610.24835v1)

## Abstract

Existing evaluations of LLM-based code optimization primarily measure end-to-end speedup, obscuring whether a model actually performs the intended optimization. For compiled languages, this is especially problematic: observed gains may reflect transformations already recoverable by modern optimizing compilers rather than optimization behavior attributable to the model itself. We present PatternBench, a benchmark for studying compiler-transcendent optimization, i.e., performance improvements that remain after aggressive compiler optimization. PatternBench targets residual optimization opportunities across seven classes of transformations and pairs runtime evaluation with an AST-based optimization faithfulness analysis that verifies whether the intended optimization is realized in the generated program. Experiments with frontier, open-weight, and fine-tuned models show that runtime speedup alone provides an incomplete account of optimization capability. Optimization faithfulness is strongly associated with realized speedup, and fine-tuning improves both faithfulness and optimization effectiveness. These results suggest that evaluation of LLM-based code optimization should measure not only performance outcomes, but also whether the target transformation was successfully executed.
