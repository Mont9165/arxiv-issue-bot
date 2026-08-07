# In-IDE Toolkit for Developers of AI-Based Features

- arXiv ID: `2605.14612v1`
- Authors: Yaroslav Sokolov, Yury Khudyakov, Lenar Sharipov, Andrei Gasparian, Parth Tiwary, Artem Trofimov
- Published: 2026-05-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.14612v1) | [pdf](https://arxiv.org/pdf/2605.14612v1)

## Abstract

AI-enabled features built on LLMs and agentic workflows are difficult to test, debug, and reproduce, especially for product-focused software engineers without a machine learning background. We present the AI Toolkit plugin for JetBrains IDEs, which brings tracing and evaluation directly into the Run/Debug loop. A mixed methods study with practitioners presents three consistent needs: (1) make evaluation regular and repeatable, (2) expose traces at the moment of execution, and (3) minimize setup and context switching. Guided by these needs, the AI Toolkit introduces an IDE-native workflow: run-triggered trace capture; immediate, hierarchical inspection; one-click "Add to Dataset" from traces; and unit-test-like evaluations with pluggable metrics. The first release in PyCharm shows promising early signals - strong conversion when promoted at Run, sustained usage among those who capture traces, and low churn - suggesting that IDE-native observability lowers activation energy and helps developers adopt disciplined practices. We detail the design and implementation of the AI Agents Debugger and AI Evaluation, report initial adoption telemetry, and outline next steps to broaden framework coverage and scale evaluations. Together, these results indicate that integrating AI observability and evaluation into everyday IDE workflows can make modern AI development accessible to non-ML specialists while preserving software-engineering practices.
