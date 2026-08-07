# Symbolon: Symbolic Execution by Learning Code Transformation

- arXiv ID: `2606.29108v1`
- Authors: Jie Zhu, Penghui Li, Zhongxuan Li, Chihao Shen, Ziyang Li, Yizheng Chen, Kexin Pei
- Published: 2026-06-27
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.PL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.29108v1) | [pdf](https://arxiv.org/pdf/2606.29108v1)

## Abstract

Symbolic execution is a powerful program analysis technique with broad applications, such as vulnerability detection, security testing, and malware analysis. However, this technique is known to suffer from scalability issues, e.g., path explosion, complex constraints, due to certain structural and semantic patterns commonly presented in real-world programs. Existing approaches attempt to escape these patterns by transforming programs into new representations to reduce the execution cost. Unfortunately, these transformations are often too rigid to exploit diverse local program semantics and sometimes rely on compiler optimizations designed for concrete execution that may misalign with the goals of symbolic execution.
  We present Symbolon, a framework that automatically learns diverse code transformations and applies them context-sensitively to improve symbolic execution. Our key insight is to formulate transformation discovery as a search problem over program representations. To make the search practical, Symbolon learns transformations cheaply offline on small programs, distills them into a reusable library of agent skills, and uses an agent to instantiate these skills on repo-level targets. Our evaluation shows that Symbolon substantially improves the symbolic execution engine KLEE across 16 search strategies on 32 real-world programs, increasing line coverage by 3.69x on average while reducing peak memory and per-query solver time by 29.2x and 123x, respectively. When applied to the latest Linux kernel, Symbolon uncovers 21 previously unknown bugs, all of which have been reported to the kernel maintainers.
