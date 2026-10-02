# Continuous Process-Level Evaluation for Evolving Enterprise AI Agent Skills

- arXiv ID: `2610.01833v1`
- Authors: Ngoc Phuoc An Vo, Aarya Doshi, Vadim Sheinin
- Published: 2026-10-01
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.01833v1) | [pdf](https://arxiv.org/pdf/2610.01833v1)

## Abstract

Enterprise AI agent skills evolve as tool APIs, models, and specifications change, yet final-output evaluation can miss process-level behavioral drift. We present a continuous evaluation framework combining outcome-level and process-level checks, applied to Revenue and Productivity variants of a Business Value Determination skill in an enterprise Value Aware Resiliency system. The framework independently computes per-run ground truth, materializes reusable template tests, and evaluates tool selection, arguments, execution order, and database integrity through programmatic checks and a narrowly scoped LLM judge. We evaluate 240 trials across two skills, two specification variants, two agent harnesses, and three models. Of 175 trials passing all applicable final numerical checks, 162 (92.6 percent; Wilson 95 percent CI: 87.7-95.6 percent) contained another evaluator-detected deviation. Under a broader seven-check final-state definition, 151 of 164 passing runs (92.1 percent; 95 percent CI: 86.9-95.3 percent) still violated a trajectory check. Dependency attribution reduced a mean of 6.34 failed checks per run to 2.65 roots. Specification sensitivity varied by model and harness, with exploratory bootstrap interaction intervals excluding zero for all three Revenue comparisons and one of three Productivity comparisons. Runtime-resolved templates provided reusable regression coverage across the evaluated configurations; longitudinal validation under actual API evolution remains future work.
