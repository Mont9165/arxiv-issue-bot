# Teaching Code LLMs to Reason with Intermediate Formal Specifications

- arXiv ID: `2607.04232v1`
- Authors: Minh Le-Anh, Cuong Chi Le, Tien N. Nguyen
- Published: 2026-07-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2607.04232v1) | [pdf](https://arxiv.org/pdf/2607.04232v1)

## Abstract

Unlike natural-language specifications, executable formal specifications provide machine-checkable constraints for verifying, debugging, and repairing code. However, writing such specifications is labor-intensive, and existing LLM-based methods mainly infer whole-program pre/postconditions, missing the intermediate semantic commitments that programmers rely on when reasoning about an algorithm. Our study further shows that prompting current CodeLLMs often produces executable assertions that are syntactically invalid, trivial, or too weak to reject behavior-changing faults. In this paper, we study executable checkpoint specification generation, where assertions are inserted at meaningful internal program points to describe expected intermediate states. We introduce SpecCoder, a verification-guided CodeLLM training framework that learns from validated reference programs, behavior-changing mutants, and multi-turn specification-refinement traces. SpecCoder selects specifications that hold on correct executions while rejecting faulty executions, turning specifications from passive annotations into executable evidence. To evaluate this setting, we introduce HumanExec, a benchmark built from recent Codeforces competitive programming problems with test suites, reference solutions, and human buggy submissions, supporting three tasks: specification generation, program correctness checking, and program repair. Experiments on HumanExec show that SpecCoder substantially improves checkpoint-specification quality over base CodeLLMs. Across Qwen2.5-Coder models, SpecCoder improves inline-specification correctness by up to 55.8%, completeness by up to 358.1%, and executable assertion validity by up to 26.6%. These gains further translate to downstream correctness reasoning and repair, showing that executable checkpoints provide fine-grained evidence for reliable verification.
