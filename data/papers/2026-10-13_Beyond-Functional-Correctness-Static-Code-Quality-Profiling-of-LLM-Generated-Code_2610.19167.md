# Beyond Functional Correctness: Static Code Quality Profiling of LLM-Generated Code

- arXiv ID: `2610.19167v1`
- Authors: Jue Huang, Tarek Mahmud, Meiru Che, Guowei Yang
- Published: 2026-10-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.19167v1) | [pdf](https://arxiv.org/pdf/2610.19167v1)

## Abstract

Large language models (LLMs) are increasingly used for code generation, yet most evaluations still focus on whether generated code passes benchmark test suites. Functional correctness alone, however, provides only a limited view of quality: benchmark tests are often incomplete, and passing them does not guarantee that code is maintainable, reliable, or well-structured. This paper {presents a large-scale static quality profiling of} LLM-generated Python code, with a focus on maintainability and reliability. Using 65{,}663 programs from 73 models in LiveCodeBench, we evaluate generated code with established static analysis tools, including Pylint, Radon, and SonarQube. Our results show systematic differences across models that are not captured by correctness alone, with maintainability emerging as the clearest source of variation. We further find that correctness often comes with structural trade-offs rather than uniformly simpler solutions. Overall, our findings motivate evaluation frameworks that assess LLM-generated code beyond pass rates alone.
