# Integrating High-Level Requirements to Low-Level Tests with Machine-Readable V&V Specifications

- arXiv ID: `2607.17686v1`
- Authors: Mansur Arief, Nur Ahmad Khatim, Ali Akarma, Ahmad Alfan Alfian Irfan
- Published: 2026-07-20
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.17686v1) | [pdf](https://arxiv.org/pdf/2607.17686v1)

## Abstract

Modern software teams have mature tools for low-level testing, such as pytest, JUnit, and Jest, which make it inexpensive to write unit tests and run them on every commit. Systems engineering, in parallel, has developed rigorous principles for design verification and validation (V&V), which has worked very well across engineering discipline to align user expecations and requirements with developers' deliverables. In practice, however, the two rarely connect, and the link between users' high-level requirements and the low-level tests that machines actually run is maintained by hand, if at all. This gap is increasingly costly for AI-enabled and cyber-physical systems, for which regulators now ask for traceable evidence that high-level requirements are met, while raw test results provide little of the structure such evidence requires. We introduce VNVSpec, an open-source framework that makes V&V specifications machine-readable and executable. With this framework, users state high-level requirements directly or import them from catalogs derived from published standards. Then, the framework checks requirement quality, supports decomposition into module-level requirements with explicit metrics and acceptance criteria, links these requirements to test results through a traceability graph, and compiles the collected evidence into verdicts and audit-ready reports. We evaluate the framework by self-application, in which it is continuously assessed in CI against its own specification of 36 requirements verified by 449 tests, completed within limited time which scales linearly and thus can handle up to 10,000 requirements. We also discuss how the framework extends to testing black-box AI models and AI coding agents. The framework, its full test suite, the catalogs, and the benchmark scripts are available at https://github.com/ai-vnv/vnvspec.
