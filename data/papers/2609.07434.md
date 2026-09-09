# CIT-CAD: Constraint Intent Tree-based CAD Code Generation and Verification

- arXiv ID: `2609.07434v1`
- Authors: Yali Du, Hui Sun, San-Zhuo Xi, Ming Li
- Published: 2026-09-07
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.07434v1) | [pdf](https://arxiv.org/pdf/2609.07434v1)

## Abstract

Natural-language Computer-Aided Design (CAD) code generation aims to turn design intent into executable and editable parametric programs. Large language models (LLMs) make this goal increasingly practical, but useful systems must preserve the construction process behind the rendered geometry. Existing benchmarks and methods mostly focus on how closely the generated CAD model matches the reference geometry, often using metrics such as Intersection over Union (IoU). Such metrics can miss errors in part decomposition, construction hierarchy, Boolean operations, sketch structure, and geometric relations. This gap calls for a representation that makes design intent explicit and lets a system check generated code against that intent. We propose CIT-CAD, a framework that infers a Constraint Intent Tree (CIT) from the input description to represent the intended entities, hierarchy, operations, and relations. The tree has two roles: it guides CAD code generation and defines expected constraints for verification. The framework extracts actual constraints from the generated program, compares them with the expected constraints, and uses mismatches to localize and repair design violations. Experiments show that the framework improves CAD generation performance, with larger gains on more complex multi-entity designs. By turning design intent into an explicit and checkable object, this work is the first attempt to move text-to-CAD generation beyond rendered-geometry matching toward construction-aware synthesis, verification, and repair.
