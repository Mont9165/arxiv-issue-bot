# Towards Certificate-Driven Software Porting: A Self-Improving Agentic Harness for Scientific Program Optimization

- arXiv ID: `2609.34069v1`
- Authors: Piyush Jha, Aishik Ghosh, Vijay Ganesh
- Published: 2026-09-28
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.34069v1) | [pdf](https://arxiv.org/pdf/2609.34069v1)

## Abstract

The upgrade and rewriting of large scientific codebases has traditionally been a major challenge. While evolutionary search with large language models (LLMs) can port and accelerate legacy code, repair feedback in prompts alone does not prevent subsequent candidates from repeating the same errors. We introduce Certificate-Driven Evolutionary Search (CDES), which extends evolutionary search with enforceable restrictions derived from failed candidates, recorded as certificates of assumptions, checker evidence, and justified restrictions. Its control logic enforces these restrictions through rejection, backtracking, and targeted repair while preserving compatible edits. We apply CDES to CPU-to-GPU translation of two particle-simulation functions from the Geant4 toolkit, evaluated with a harness that goes beyond unit tests to combine formal checks, numerical comparisons, physics checks, and GPU safety tests. Generated implementations achieve 13.78x and 23.54x function-level speedups over CPU code, including data conversion and transfers; for one function, GPU throughput exceeds an expert implementation by 14.9%, reaching 16.1% when complementary components are combined. In an ablation over execution settings, certificate feedback increases the fraction of candidates passing required correctness checks from 55% to 90%.
