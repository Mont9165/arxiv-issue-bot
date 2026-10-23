# Typed Template Fuzzing

- arXiv ID: `2610.31342v1`
- Authors: Lu Maltsis, Dominik Winterer
- Published: 2026-10-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2610.31342v1) | [pdf](https://arxiv.org/pdf/2610.31342v1)

## Abstract

Fuzzing software with complex inputs has been a longstanding challenge. Traditionally, fuzzers either programmatically encode language constraints, requiring significant engineering effort, or rely on users to declare grammars and constraints. Recent LLM-based fuzzers address these drawbacks but introduce new issues. Some use LLMs for test generation, sacrificing throughput and producing invalid inputs when the LLM makes mistakes. Others rely on language-specific parsers, static analysis, and AST manipulation libraries. We introduce Typed Template Fuzzing (TTF), a lightweight LLM-based fuzzing methodology. The key idea is to use LLMs in a preprocessing step to transform seeds into typed templates. The typed templates then enable semantically aware, mutation-based fuzzing without language-specific parsers, type checkers, or further LLM queries during fuzzing. By exploiting the correspondence between seeds and templates, TTF can moreover repair LLM mistakes. We have implemented TTF in our tool Typos, which we evaluate across 21 input languages, including C, C++, Go, Rust, SystemVerilog, Scala, and Java, as well as libraries such as PyTorch and Qiskit. In a six-month fuzzing campaign, we reported 135 bugs, 128 of which were previously unknown. Perhaps most notably, on average 96% of Typos's mutants are valid, coming close to the validity rates of domain-specific fuzzers. Our evaluation further shows Typos's benefits over the state of the art.
