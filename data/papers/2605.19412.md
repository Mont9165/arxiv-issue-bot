# DRReduce: Enhancing Syntax-Guided Program Reduction with Dependency Reconstruction

- arXiv ID: `2605.19412v1`
- Authors: Qiong Feng, Xiaotian Ma, Yongqiang Tian, Wei Song, Peng Liang
- Published: 2026-05-19
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2605.19412v1) | [pdf](https://arxiv.org/pdf/2605.19412v1)

## Abstract

Program reduction is a technique for simplifying large, failure-inducing programs into minimal reproducible test cases. Language-specific tools such as CReduce achieve strong performance by leveraging deep semantic knowledge of C/C++, but are tightly coupled to a single language family. Language-agnostic reducers such as Perses address this by applying syntax-guided search across any grammar, yet share a fundamental limitation: deleting a node or subtree in isolation often breaks semantic coherence causing the property checker to reject the deletion and forcing the reducer to backtrack, limiting overall reduction effectiveness and efficiency. In this paper, we propose DRReduce, a framework that bridges this gap by augmenting language-agnostic syntactic reduction with a lightweight semantic layer: dependency reconstruction, which repairs program dependencies broken by a deletion in order to preserve the semantic validity of intermediate programs and increase the acceptance rate of the property checker. DRReduce constructs a semantic dependency graph from the input program, performs semantically coherent deletions with dependency reconstruction, and delegates further minimization to a syntax-guided reducer. We implement DRReduce for C and Java and evaluate it on real-world bug-triggering programs. Compared to SOTA syntax-guided reducers, DRReduce achieves average size reductions of 51.9%, 14.9%, and 19.8% over Perses, WDD, and CDD respectively, while completing reduction faster on the majority of programs. Compared to language-specific tools, DRReduce achieves results comparable to CReduce and Latra without any language-specific transformation rules, at 3.3x and 1.2x higher efficiency than CReduce and Latra on average, respectively. An ablation study confirms that dependency reconstruction reduces query invocations by 80.2%, reduction time by 58.7%, and final token count by over 55.1%.
