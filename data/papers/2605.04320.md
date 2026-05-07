# Reproduction Test Generation for Java SWE Issues

- arXiv ID: `2605.04320v1`
- Authors: Toufique Ahmed, Jatin Ganhotra, Avraham Shinnar, Martin Hirzel
- Published: 2026-05-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.04320v1) | [pdf](https://arxiv.org/pdf/2605.04320v1)

## Abstract

Given an issue on a software repository, a reproduction test confirms its presence in the code before it gets fixed and its absence after. Reproduction tests provide crucial execution-based feedback for diagnosis and validation during software development. Unfortunately, they are usually missing. Therefore, recent work has introduced both benchmarks and a thriving literature on solutions for reproduction test generation from issues. However, that work has focused on Python and neglected other languages such as Java, which is important for enterprise software. This paper introduces both a benchmark and a solution for Java repository-level reproduction test generation. The benchmark, TDD-Bench-Java, is the first to model this problem and comprises 250 instances sourced from popular open-source repositories. The solution, e-Otter++ for Java, adapts a state-of-the-art reproduction test generator for Python to yield high performance on Java. To evaluate in an industry setting, besides empirical results with TDD-Bench-Java, this paper also presents results with a contamination-free proprietary dataset. Overall, we hope that this paper contributes to bringing better diagnosis and validation to Java software development.
