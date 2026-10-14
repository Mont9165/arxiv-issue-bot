# Neuro-Symbolic Reasoning for Vulnerability Detection

- arXiv ID: `2607.03963v1`
- Authors: Yanjie Zhao, Hongjie Chen, Li Lu, Zhou Yang, Xiao Cheng, Haoyu Wang
- Published: 2026-07-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.03963v1) | [pdf](https://arxiv.org/pdf/2607.03963v1)

## Abstract

Ask a large language model (LLM) whether a pointer dereference is safe, and it can often produce a plausible justification for ``yes''. The difficulty is that a fluent justification is not a proof. This gap is precisely where automated vulnerability detection lives: deciding, for a given operation in source code, whether a memory safety defect such as a null dereference, use-after-free, or double free can actually occur. We trace the unreliability of LLM-based vulnerability detection to a mechanism, the premature discharge of safety obligations, and argue that the remedy is not better prompting but a separation of roles: the component that interprets the code must not also be the one that decides a safety obligation is met.
  In this paper, we present LeanGuard, a neuro-symbolic framework that assigns each act to the side equipped for it. On the neural side, an LLM serves strictly as a semantic filter over candidate facts extracted from the abstract syntax tree (AST): it prunes spurious facts and keeps the real ones, but never discharges an obligation or decides the verdict on its own. On the symbolic side, the surviving facts are compiled into a verification model in Lean 4 (a formal proof assistant whose kernel accepts a conclusion only when it is formally proved), where every dangerous operation must be matched by a guard that provably covers it in scope; absent such a guard, the obligation stays open rather than being argued away. Because a function rarely arrives with full context, this symbolic model is necessarily partial: an unproved obligation is not yet a defect. An evidence-aware adjudicator therefore weighs the symbolic and neural verdicts by the quality of each. We instantiate the framework on five CWE classes to ask how far this division of labor can be pushed.
