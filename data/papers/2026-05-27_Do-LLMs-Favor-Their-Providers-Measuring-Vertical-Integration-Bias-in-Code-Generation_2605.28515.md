# Do LLMs Favor Their Providers? Measuring Vertical Integration Bias in Code Generation

- arXiv ID: `2605.28515v1`
- Authors: Melih Catal, Alex Wolf, Tiago Ferreiro Matos, Pooja Rani, Harald Gall
- Published: 2026-05-27
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.28515v1) | [pdf](https://arxiv.org/pdf/2605.28515v1)

## Abstract

Large Language Models (LLMs) have become an integral part of software development, especially with the advent of agentic capabilities. Yet, many frontier LLMs are affiliated with specific providers. This raises the question of whether generated code favors the provider's own ecosystem over comparable alternatives, potentially constraining developers' choices and increasing dependence on a single provider. We define this behavior as Vertical Integration Bias (VIB) and introduce \textsc{VIBench}, a benchmark for measuring VIB in direct and agentic code generation across $20$ provider-selectable software-integration scenarios. Evaluating $10$ frontier provider-affiliated models against $3$ non-affiliated controls, we find positive VIB in direct generation, with six of ten affiliated models showing statistically significant effects up to $+18.8$ percentage points (pp). Agentic workflows further amplify VIB, reaching $+39.2$ pp. Moreover, early affiliated-ecosystem choices in agentic workflows can persist into conceptually decoupled downstream files, with persistence as high as $90.3\%$. These findings underscore the need to measure and account for VIB in code generation, especially as agentic capabilities become more prevalent.
