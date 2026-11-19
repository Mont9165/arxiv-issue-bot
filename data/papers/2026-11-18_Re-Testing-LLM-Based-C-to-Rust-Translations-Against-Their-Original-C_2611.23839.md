# Re-Testing LLM-Based C-to-Rust Translations Against Their Original C

- arXiv ID: `2611.23839v1`
- Authors: Muhammad Hassnain
- Published: 2026-11-18
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.23839v1) | [pdf](https://arxiv.org/pdf/2611.23839v1)

## Abstract

Most C-to-Rust translators use large language models (LLMs), and each reports a success rate from its own correctness check. We survey 34 C-to-Rust translators that use LLMs. Only one reports testing its check, and eleven release the original C and their Rust in runnable form. We re-test all eleven. We run the C and the Rust on generated inputs, compare every output, and count a divergence only where the C has no undefined behavior. All eleven release defective translations: we find 160 defects, 93 of them outright errors on ordinary inputs. Their own checks accepted 86 defective translations. For 81 of them, the released check never compared the programs on an input that exposes the defect. For three of the other five, it ran one but compared only part of the output. A success rate is only as good as its check. Before counting a translation as a success, authors should compare every output with the C's on inputs the repair loop never saw, check that a verifier reaches its assertion, release exactly what the check accepted, and report how they tested the check.
