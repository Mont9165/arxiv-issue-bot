# "Will This Data Break My Task?" - Interactive Synthesis of Task-Aware Data Unit Tests

- arXiv ID: `2608.09376v1`
- Authors: Hao Chen, Arnab Phani, Sebastian Schelter
- Published: 2026-08-10
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.09376v1) | [pdf](https://arxiv.org/pdf/2608.09376v1)

## Abstract

Data is a central resource for modern enterprises and institutions, and data errors propagating through data pipelines lead to serious impact in production. Therefore, data validation is essential for ensuring the reliability of downstream applications. This led to the development of data unit tests, executable programs that test data before moving it around through large data pipelines. However, existing frameworks derive data unit tests from observed data alone, ignoring the semantics of the code that consumes the data downstream.
  To this end, we present PrismaDV, a compound AI system that synthesizes task-aware data unit tests for tabular data by jointly analyzing data and downstream task code. PrismaDV decomposes the test generation into multiple LLM-powered steps: data profiling, detection of column accesses, data flow analysis in the task code, and the inference of implicit data assumptions. It subsequently synthesizes code for the data unit test, and maintains an internal ``data-code assumption graph'' that links generated data constraints back to the task's source code.
  We demonstrate PrismaDV through an interactive web-based interface where attendees run the system on five real-world datasets with 60 downstream tasks, synthesize, inspect and refine both natural language assumptions about the data and executable data constraints. The interface allows attendees to navigate the data-code assumption graph, compare task-aware data unit tests against task-agnostic baselines on erroneous data batches, and interactively edit assumptions and data constraints. Furthermore, attendees can observe how a custom prompt optimizer adapts the system to specific datasets over time.
