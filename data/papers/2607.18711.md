# LLM-Based Invariant Testing for Software Functional Bugs

- arXiv ID: `2607.18711v1`
- Authors: Ruogu Yang, Yifeng He, Yundi Xu, Yuqing Wei, Hao Chen
- Published: 2026-07-21
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.18711v1) | [pdf](https://arxiv.org/pdf/2607.18711v1)

## Abstract

Manually writing unit tests to uncover functional bugs in software libraries is not only time-consuming but also requires a deep understanding of the intended semantics of the APIs. Heuristic-based test generation methods suffer from low usability because they cannot reason about program semantics or interpret source code and documentation as humans do. Traditional fuzzing techniques like OSS-Fuzz often rely on crashes to detect bugs, but functional bugs do not always cause crashes. To overcome these limitations, we present LISA, a novel LLM-based invariant testing framework for software functional bugs. LISA iteratively generates API sequences and program invariants guided by API n-gram feedback, achieving higher bug-detection rates and competitive code coverage compared with both fuzzing and prior LLM-based test generation approaches, and reporting each finding as a high-confidence bug candidate for developer confirmation.
