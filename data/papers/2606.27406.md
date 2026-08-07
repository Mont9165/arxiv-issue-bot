# Towards Evaluation of Implicit Software World Models in Coding LLMs

- arXiv ID: `2606.27406v1`
- Authors: Egor Bogomolov, Yaroslav Zharov
- Published: 2026-06-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.27406v1) | [pdf](https://arxiv.org/pdf/2606.27406v1)

## Abstract

Software engineering, whether performed by humans or by AI agents, requires reasoning about how software behaves. We call the internal model that supports such reasoning the software world model, and view current code-execution benchmarks as covering one well-studied slice of it -- control flow. In this paper, we take a step toward a broader evaluation by shifting the observable axis to execution resources: alongside test outcome and exception class, we predict peak memory, wall-clock time, and ranked profiler outputs at method and line granularity. We use SWE-bench Verified as the source of data to hold the test close to real-world software engineering tasks. All tested models, frontier ones included, show modest performance and brittle behaviour, suggesting a notable lack of understanding of how software is executed, as opposed to how its source code is written.
