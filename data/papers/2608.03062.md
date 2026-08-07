# TraceCAD: Trace-Guided Repair for Agentic CAD Generation

- arXiv ID: `2608.03062v1`
- Authors: Fengxiao Fan, Jingzhe Ni, Fan Sang, Xiaolong Yin, Yu Liu, Ruofeng Tong, Min Tang, Peng Du
- Published: 2026-08-04
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.GR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.03062v1) | [pdf](https://arxiv.org/pdf/2608.03062v1)

## Abstract

LLM-based CAD agents produce executable parametric programs, but their correction loops may lose evidence about satisfied requirements, faulty operations, and prior repairs. We introduce TraceCAD, a recovery layer that links requested features, modeling steps, failure evidence, and candidate outcomes as persistent state. TraceCAD diagnoses likely faulty operations, searches bounded edits in their dependency regions, validates candidates through execution and preservation checks, and retains successful and failed repair outcomes in reusable skill memory. On DeepCAD-derived benchmarks with 200-model ablations and a 1K-model comparison, TraceCAD achieves competitive geometric quality in terms of IoU, Chamfer distance, and Hausdorff distance. Removing persistent state nearly halves recovery score; removing localized search more than doubles geometric regression and doubles code-agent invocations. Initializing the skill store on disjoint training models further reduces retries, token cost, and latency. These results demonstrate that persistent, localized, and reusable recovery improves final CAD quality and repair reliability.
