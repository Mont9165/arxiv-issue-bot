# Quality-Assured Fuzz Harness Generation via the Four Principles Framework

- arXiv ID: `2605.21824v1`
- Authors: Ze Sheng, Dmitrijs Trizna, Luigino Camastra, Zhicheng Chen, Qingxiao Xu, Jeff Huang
- Published: 2026-05-20
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.21824v1) | [pdf](https://arxiv.org/pdf/2605.21824v1)

## Abstract

Fuzz testing is the dominant technique for finding memory-safety vulnerabilities in C/C++ software, yet its effectiveness hinges on the quality of fuzz harnesses -- the programs that bridge fuzzers and library APIs. A growing body of tools now automate harness generation, but none systematically ensures the correctness of produced harnesses: logic errors, API misuse, and lifecycle violations go undetected at the source level. As LLM-driven generation scales harness creation, uncontrolled quality turns scale into a liability.
  We present QuartetFuzz, an autonomous harness-generation system that systematically improves correctness throughout the generation process. At its core is the Four Principles framework -- Logic Correctness (P1), API Protocol Compliance (P2), Security Boundary Respect (P3), and Entry Point Adequacy (P4) -- the first source-level definition of harness correctness with mathematical specifications and implementable checks. We operationalize these principles in an autonomous LLM agent that produces harnesses satisfying P1-P4 through a generate-check-fix loop before any fuzzing begins.
  Deployed on 23 open-source projects spanning C/C++, Java, and JavaScript, the system submits 42 bug reports, of which 29 are fixed or confirmed upstream (including 3 CVEs) and only 2 are rejected (4.8% FP rate). During generation, the built-in P1/P2 checks automatically intercepted 58 harness-induced crashes that would otherwise have been false positives. Applied as a quality auditor to 586 existing production harnesses across 70 projects, the system identifies 53 violations (45 confirmed, 35 fixed). We release a dataset of 100 labeled harnesses for reproducible evaluation. Code and dataset are available at https://github.com/OwenSanzas/QuartetFuzz
