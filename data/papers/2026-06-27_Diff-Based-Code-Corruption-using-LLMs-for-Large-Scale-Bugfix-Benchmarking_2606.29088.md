# Diff-Based Code Corruption using LLMs for Large-Scale Bugfix Benchmarking

- arXiv ID: `2606.29088v1`
- Authors: Balázs Szalontai, Ábel Szauter, Balázs Márton, Péter Verebics, Balázs Pintér, Tibor Gregorics
- Published: 2026-06-27
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.29088v1) | [pdf](https://arxiv.org/pdf/2606.29088v1)

## Abstract

There are various benchmarks to evaluate bugfixing capabilities of Large Language Models. However, most widespread benchmarks do not fully reflect real-world bugfixing practices. They are small, weakening statistical reliability, and the buggy programs are often similar to one another, potentially distorting evaluation results. The range of bug types can also be narrow, failing to capture a representative range of bugs. To address these issues, we introduce MegaBugFix, a large-scale bugfixing benchmark containing 12,629 buggy Python programs synthesized from correct ones by a Large Language Model. Bug injections were generated as diffs representing code changes. Through this approach, we were able to avoid common pitfalls of LLM-based mutation techniques like injecting overly simplistic bugs or failing to modify the input program. We evaluated 13 open-weight models on MegaBugFix and baseline benchmarks, finding consistently lower performance on MegaBugFix. This reveals that our benchmark presents more challenging bugs and exposes model failures that may remain hidden when evaluating on existing benchmarks. The benchmark and fine-tuned model used for bug injection are available at hf.co/collections/szalontaib/megabugfix.
