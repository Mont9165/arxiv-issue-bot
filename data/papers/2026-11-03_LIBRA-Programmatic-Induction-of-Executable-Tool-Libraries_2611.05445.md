# LIBRA: Programmatic Induction of Executable Tool Libraries

- arXiv ID: `2611.05445v1`
- Authors: Zekai Li, Zhenke Liu, Yonghao Li, Junhan Liu, Xulong Xiao, Jiapeng Zhang
- Published: 2026-11-03
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2611.05445v1) | [pdf](https://arxiv.org/pdf/2611.05445v1)

## Abstract

Large language model agents increasingly retrieve tools from large catalogs, yet most retrievers rank each tool independently by request similarity. For multi tool tasks, this recovers the goal matching tool while omitting prerequisite tools required by the workflow.We introduce LIBRA, a framework for Library Induction by Runtime Assembly that turns a flat tool catalog into an executable tool library. An LLM proposes per tool contracts of candidate invocations, reusable outputs and state changes, and success conditions; LIBRA then tests these compositions in a sandbox and retains the relations supported at runtime. Constructed before user queries, the library requires no dependency annotations, tool use trajectories, or task specific training, and supports both one-shot and agentic retrieval. On AppWorld, BFCL, and SciToolEval, LIBRA improves one-shot Recall and NDCG over the same dense retriever by 7.9 and 3.7 percentage points on average. Within ToolReAGt, it yields corresponding gains of 4.5 and 2.9 points after ten retrieval iterations.
