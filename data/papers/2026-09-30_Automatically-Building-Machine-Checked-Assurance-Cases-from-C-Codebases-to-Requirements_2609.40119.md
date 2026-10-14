# Automatically Building Machine-Checked Assurance Cases from C Codebases to Requirements

- arXiv ID: `2609.40119v1`
- Authors: Haokun Li, Zhongyi Wang, Guanyan Li, Xiao Yi, Shengchao Qin, Jianwei Yin, Mingshuai Chen
- Published: 2026-09-30
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.40119v1) | [pdf](https://arxiv.org/pdf/2609.40119v1)

## Abstract

Large language models (LLMs) have shown promise in automating interactive theorem proving, yet verification of real-world C codebases requires more than discharging individual proof goals. The task involves jointly constructing expressive function specifications and their proofs, and ensuring that library interfaces compose along intended call sequences even without a designated client. This paper presents CCV, an LLM-assisted framework for building machine-checked assurance cases: structured, auditable artifacts supporting the claim that a C codebase meets its intended requirements. To model intended cross-interface use in open libraries, CCV constructs an interface protocol that exposes permitted call sequences and resource assumptions for review, with a conditional safety guarantee under verified contracts and caller obligations. CCV coordinates two complementary phases: (i) requirement-guided analysis and bottom-up construction of candidate specifications and protocols; and (ii) modular proof construction with feedback that revises the specifications and proofs. Implemented using VST in Rocq, CCV verifies memory safety and leak freedom for all 299 function definitions across six C benchmarks, including industrial cryptographic components, with less than one person-day of reported human effort per benchmark. The guarantees depend on disclosed contracts and assumptions; human review supplies the conformance judgments connecting the formal artifacts to the intended requirements.
