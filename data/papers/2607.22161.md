# HarnessLLM: Rust Verification Harness Generation with Large Language Models

- arXiv ID: `2607.22161v1`
- Authors: Minghua Wang, Yuwei Liu, Lin Huang
- Published: 2026-07-24
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2607.22161v1) | [pdf](https://arxiv.org/pdf/2607.22161v1)

## Abstract

Rust's ownership model and type system offer strong memory safety guarantees, but unsafe code and runtime panics still present significant risks. Formal verification is essential to ensure memory safety, but developing verification harnesses remains a challenging and manual task. Although large language models (LLMs) have shown strong performance in various code analysis tasks, directly applying them to harness generation often results in inaccurate API invocations, inefficient nondeterministic data generation, and fabricated fixes.
  In this paper, we present HarnessLLM, an automated workflow that leverages LLMs to generate verification harnesses for Rust code directly from existing test suites. HarnessLLM automatically extracts calling scenarios from test cases, generates nondeterministic arguments based on dependency analysis, and incrementally synthesizes harnesses. It then iteratively refines the harnesses, preserving critical code regions and reporting fabricated types or functions to LLMs for correction. In our evaluation on 9 real-world Rust codebases, HarnessLLM extracted 294 calling scenarios from 494 test cases with 94.66% precision and generated harnesses for all scenarios in an average of 145 seconds each. It outperformed the existing approach, Autoharness, which succeeded on only 41% of those scenarios. Finally, 6 real-world memory safety bugs were detected using the generated harnesses, demonstrating the practical utility of our approach in verification. To our knowledge, this is the first work to use LLMs for generating harnesses aimed at memory safety verification in real-world Rust projects.
