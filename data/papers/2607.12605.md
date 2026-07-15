# Multi-Perspective Agentic Program Repair via Code Property Graphs and Temporal Execution Graphs

- arXiv ID: `2607.12605v1`
- Authors: Zhili Huang, Ling Xu, Hongyu Zhang
- Published: 2026-07-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.12605v1) | [pdf](https://arxiv.org/pdf/2607.12605v1)

## Abstract

Large language models (LLMs) have improved automated program repair (APR), but two limitations remain. First, raw execution traces are often too large and repetitive to serve as effective model context. Second, repeated patch sampling may produce different implementations without yielding distinct root-cause hypotheses or repair strategies. We present CT-Repair, an agentic APR framework representing static and dynamic evidence as queryable Code Property Graph (CPG) and Temporal Execution Graph (TEG). CT-Repair applies a three-stage filtering pipeline to construct compact TEGs. Three finite-state-machine-guided agents analyze each bug from static, dynamic, and hybrid perspectives and independently produce evidence-grounded repair strategies. A strategy-guided generation procedure instantiates these strategies as candidate patches and uses validation feedback to refine the most promising strategy.
  We evaluate CT-Repair on 854 Java bugs from Defects4J v3.0. In the mixed-model configuration, CT-Repair correctly repairs 489 bugs. Under a controlled GPT-5.4-mini configuration, it repairs 388 bugs, 19 and 30 more than ReinFix and RepairAgent, respectively. The union of the three evidence perspectives repairs 99 more bugs than the strongest individual perspective. The filtering pipeline also compacts runtime evidence, with execution filtering narrowing the candidate method scope by 94.85% on average and behavior filtering further reducing retained runtime records by 55.97%. These results show that structured runtime evidence and multi-perspective reasoning can improve repair effectiveness without relying solely on a larger patch-generation budget.
