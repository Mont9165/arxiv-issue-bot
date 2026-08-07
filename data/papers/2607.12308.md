# Mystra: Declarative Dynamic Taint Analysis via Shadow Virtual Machine

- arXiv ID: `2607.12308v1`
- Authors: Zhuohao Zhang, Junkun Liu, Rui Yang, Yinzhi Cao, Ziyang Li
- Published: 2026-07-14
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.12308v1) | [pdf](https://arxiv.org/pdf/2607.12308v1)

## Abstract

Dynamic taint analysis (DTA) for interpreted languages like JavaScript and Python requires three capabilities: observing host-runtime operations, maintaining parallel taint states, and defining how taint propagates. Existing systems couple these capabilities within an instrumentation mechanism -- source-rewriting or engine-native -- either incurring high runtime overhead or demanding engine-specific embeddings. There is yet to be a runtime-independent abstraction of a general DTA that separates taint semantics and state transitions from how a host runtime observes and executes them.
  We set out to develop a DTA engine that is extensible, performant, and accurate. To achieve this, we introduce a Shadow Virtual Machine executing alongside host runtimes that tracks multi-level taint, provenance, and cross-invocation context. We design Mystra, a declarative taint specification language with formal operational semantics. Mystra is designed to be language model friendly, and is equipped with validators enabling trustworthy automated synthesis of rules. Mystra is also the first to express higher-order function taint transfer declaratively. Further, Mystra rules are compiled ahead of time to a binary representation and dispatch in constant runtime.
  We implement our vision into a tool named Shar, which contains a shared core engine and instantiations on three runtimes: V8 in both Node.js and Chromium (embedding), SpiderMonkey (engine), and CPython (language). Accuracy wise, on SecBench.js (493 in-scope CVEs across four CWE categories), our V8 instantiation achieves 95.5% recall with zero false positives on patched-version testing. Regarding performance, the runtime overhead of Shar is only 1.85$\times$ over vanilla Node.js on NodeMedic's benchmarks, and is 22.7$\times$ lower than NodeMedic-FINE on identical workloads, all the while producing 33.2% higher recall in its supported categories.
