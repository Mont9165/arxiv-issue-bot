# Verus-SpecGym: An Agentic Environment for Evaluating Specification Autoformalization

- arXiv ID: `2605.26457v1`
- Authors: Anmol Agarwal, Natalie Neamtu, Pranjal Aggarwal, Seungone Kim, Jannis Limperg, Cedric Flamant, Kanna Shimizu, Bryan Parno, Sean Welleck
- Published: 2026-05-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2605.26457v1) | [pdf](https://arxiv.org/pdf/2605.26457v1)

## Abstract

AI coding agents are increasingly used to write real-world software, but ensuring that their outputs are correct remains a fundamental challenge. Formal verification offers a promising path: an agent generates code together with a machine-checked proof, guaranteeing that the code satisfies a formal specification. However, there is no guarantee that the formal spec itself matches the user's intent. In this work, we study specification autoformalization: whether LLM agents can translate informal programming problems into faithful formal specifications. We introduce Verus-SpecBench, a benchmark of 581 spec-writing tasks derived from Codeforces problems targeting Verus, a verifier for Rust, and Verus-SpecGym, an agentic environment in which models interact with Verus, bash, & the filesystem to develop these specs. The central challenge is evaluation: expert-written reference specs are expensive to write, & LLM judges can miss subtle mistakes. We address this by (a) extending Verus's exec_spec mechanism so that generated specs can be executed as Rust code, & (b) testing them against official Codeforces tests & adversarial cases extracted from Codeforces "hacks", which are edge cases written by competitors to break incorrect solutions. On Verus-SpecBench, the strongest model, Gemini 3.1 Pro, solves 77.8% of tasks, other frontier models solve 51.1--57.8% & OSS models reach only 21.5--25.5%. Our analysis of failure modes shows that model-generated specs can omit important input assumptions, accept incorrect outputs, & reject valid ones. We also find that LLM-as-a-judge evaluation misses 26% of the failures our evaluator catches. Overall, our results suggest that spec autoformalization is within reach for frontier agents but remains brittle even on problems where they can already generate correct code. The code, data, & logs can be found at https://github.com/formal-verif-is-cool/verus-spec-gym
