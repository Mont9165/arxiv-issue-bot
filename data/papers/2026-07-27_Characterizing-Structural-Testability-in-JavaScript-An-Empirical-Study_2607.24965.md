# Characterizing Structural Testability in JavaScript: An Empirical Study

- arXiv ID: `2607.24965v1`
- Authors: Shahrzad Mirzaei, Saba Alimadadi
- Published: 2026-07-27
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.24965v1) | [pdf](https://arxiv.org/pdf/2607.24965v1)

## Abstract

Software testability has long been recognized as a software quality attribute that influences testing effort and effectiveness. While prior work has extensively studied testability in object-oriented and concurrent software, comparatively little is known about structural testability in modern JavaScript systems. JavaScript applications rely on asynchronous execution, event-driven control flow, closures, and dynamic interactions that are not explicitly captured by existing testability frameworks. This paper presents a large-scale empirical study of structural testability in JavaScript. We operationalize structural testability as a seven-dimensional construct capturing controllability, observability, branching complexity, asynchronous coordination, event-driven behaviour, encapsulation, and side-effect intensity. These dimensions are derived from AST-based static analysis and aggregated into a Composite Testability Score (CTS) for comparative analysis across functions, files, and projects. We apply this framework to 30 open-source JavaScript projects spanning diverse domains and sizes. Our analysis characterizes the distribution of structural testability, identifies recurring structural archetypes among low-CTS functions, and examines associations between project characteristics and testability. We find that structurally-challenging functions are concentrated within a relatively small subset of files and arise through multiple recurring structural configurations rather than a single dominant pattern. These findings provide new insight into structural testability in JavaScript and establish a foundation for future research on testing effort, automated test generation, testability-aware refactoring, and software quality assessment.
