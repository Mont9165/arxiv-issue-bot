# Vulnerability Detection in AArch64 Machine Code Using a Digital Twin

- arXiv ID: `2608.02125v1`
- Authors: Oleksandr Mostovyi, Denys Symonov
- Published: 2026-08-03
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.02125v1) | [pdf](https://arxiv.org/pdf/2608.02125v1)

## Abstract

This paper proposes an explainable digital twin for vulnerability detection in AArch64 machine code without access to source code. The digital twin reproduces the concrete execution of a program and preserves the state of registers, processor flags, memory, and live allocated blocks. Each instruction is transformed into a trace event containing the instruction name, operand values, and the post-instruction state. Vulnerabilities are represented as symbolic rules in Kleene algebra with tests: each rule specifies an event sequence and predicates over the machine state. This approach enables the detection of not only isolated unsafe instructions but also multi-step execution patterns. The rules are compiled into finite automata that scan the trace without using an SMT solver. The experimental evaluation covers three CWE classes: integer overflow (CWE-190), null pointer dereference (CWE-476), and heap buffer overflow (CWE-122). The system detected all three predefined vulnerabilities and produced no report on the safe trace. Each detection result includes the triggered rule, the trace position, and the concrete state values, thereby providing a reproducible explanation.
