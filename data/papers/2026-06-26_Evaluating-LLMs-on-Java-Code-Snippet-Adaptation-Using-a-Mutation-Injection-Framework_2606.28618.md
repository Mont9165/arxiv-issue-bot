# Evaluating LLMs on Java Code Snippet Adaptation Using a Mutation-Injection Framework

- arXiv ID: `2606.28618v1`
- Authors: Ali Aman, Muhammad Asaduzzaman, Shaowei Wang, Chanchal K. Roy
- Published: 2026-06-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.28618v1) | [pdf](https://arxiv.org/pdf/2606.28618v1)

## Abstract

Background: Developers frequently reuse code by copying fragments and adapting them to fit new contexts. Existing benchmarks for evaluating large language models (LLMs) on code adaptation either rely on explicit step-by-step instructions, cover only narrow change types such as variable wiring, or operate exclusively at function-level granularity. It remains unknown how well LLMs can adapt code fragments without explicit edit guidance when the required changes are varied and controlled.
  Objective: We investigate instruction-free code snippet adaptation in which an LLM must adapt a code fragment to fit its target context without any explicit edit guidance. We study three dimensions: which adaptation types are hardest (RQ1), how performance scales with adaptation complexity (RQ2), and how much surrounding context the model needs (RQ3).
  Method: We will construct a dataset of Java code fragments from open-source repositories with strong test coverage and apply a taxonomy of adaptation operators, derived from empirical findings on how developers adapt copied code, using a mutation-injection framework. Working at the code fragment level and controlling the injected changes lets us know exactly what adaptations the model must perform. The unmutated fragment serves as a plausible reference for the changes the model needs to make. LLMs will be evaluated on instruction-free adaptation tasks across three context granularity levels. Correctness will be measured primarily via test-suite re-insertion, complemented by mutation-level inspection.
