# Tool Retrievers Are Underestimated: Annotation Expansion Reveals True Capability

- arXiv ID: `2609.08327v1`
- Authors: Yanyu Zhu, Chenheng Zhang, Shaoshen Chen, Hoilam Pao, Yufei zhang, Jiajun Chai, Dongnian Wang, Zhaoyu Hu, Guojun Yin, Wei Lin, Hai-Tao Zheng
- Published: 2026-09-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2609.08327v1) | [pdf](https://arxiv.org/pdf/2609.08327v1)

## Abstract

In open-world scenarios with massive and evolving tool repositories, tool-augmented large language models rely on a retriever to surface relevant tools for a given query. Because such repositories often contain many tools that implement the same functionality, a single query can often be resolved by several distinct but functionally equivalent tool combinations, making the natural query-to-tool mapping inherently one-to-many. However, existing tool retrieval benchmarks annotate each query with a single relevant tool combination, collapsing this one-to-many mapping into a rigid one-to-one annotation and causing valid retrieved tools to be misjudged as failures. To address this, we propose ToolEX (Tool Equivalent eXpansion), a framework that automatically discovers and annotates the tool combinations functionally equivalent to the labeled ones. Applied to the 7,360-query Tool-DE benchmark, ToolEX finds that 67.9% of sub-queries admit equivalent alternatives, expanding the singular ground truth to an average of 5.3 valid combinations per query. Using the expanded benchmark ToolEQ, we re-evaluate eight base retrievers and two fine-tuned variants; metrics on ToolEQ rise substantially over Tool-DE, showing that one-to-one annotation systematically underestimates retrievers and that 30--47% of the reported fine-tuning gain is an evaluation artifact rather than genuine improvement. Applying the same pipeline to skill retrieval on SkillRet further confirms that the one-to-one problem extends beyond tool retrieval.
