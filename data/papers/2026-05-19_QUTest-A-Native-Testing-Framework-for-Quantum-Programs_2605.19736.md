# QUTest: A Native Testing Framework for Quantum Programs

- arXiv ID: `2605.19736v1`
- Authors: José Campos
- Published: 2026-05-19
- Primary category: `quant-ph`
- Categories: `quant-ph`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.19736v1) | [pdf](https://arxiv.org/pdf/2605.19736v1)

## Abstract

Quantum programs are often shared as OpenQASM 3 circuits, but tests are still written in host languages such as Python with Qiskit. We present QUTest, a native framework in which both programs and tests are standard .qasm files. Tests follow the Arrange / Act / Assert pattern, while configuration, runtime requirements, and assertions are encoded as pragma comments (//%), preserving compatibility with existing OpenQASM tools. QUTest provides 12 assertion types spanning deterministic, statistical, quantum-state, and structural checks, plus a linter and an environment-aware mode for running the same test across selected runtime versions in isolated environments. Its CLI supports automatic test discovery, runtime compatibility checks, and XML reports for continuous integration. We describe the pragma language, implementation, and a planned evaluation using coverage and mutation testing.
  QUTest is available at https://github.com/QBugs/qutest.
  Video demo: https://youtu.be/FvgvsiAXuW0.
