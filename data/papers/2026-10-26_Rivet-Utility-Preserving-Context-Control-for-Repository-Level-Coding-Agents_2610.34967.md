# Rivet: Utility-Preserving Context Control for Repository-Level Coding Agents

- arXiv ID: `2610.34967v1`
- Authors: Ruwei Pan, Linhao Wu, Yakun Zhang, Zixiong Yang, Lu Zhang, Hongyu Zhang
- Published: 2026-10-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.34967v1) | [pdf](https://arxiv.org/pdf/2610.34967v1)

## Abstract

Repository-level code generation asks an agent to implement a task requirement inside an existing repository. To produce code that works in the repository, the agent needs repository evidence, such as target locations, helper definitions, caller usages, and configuration constraints, which determine how the code should be located, integrated, and executed. Because the context budget cannot hold the entire repository, existing retrieval, compression, and structure-aware methods select context by task similarity, context length, or structural proximity, but these criteria do not directly measure whether the selected context contains this evidence. As a result, the selected context can appear relevant to the task yet miss the evidence that the implementation depends on. We call this failure mode context utility dilution. In this paper, we propose Rivet, a context control framework that preserves repository evidence for coding agents under a fixed context budget. Rivet, first uses Signal Grounding to select task-related code anchors by fusing lexical, semantic, and structural signals. Utility Linking then expands these anchors through dependency, usage, and configuration relations to collect repository evidence. Finally, Budget Shaping packs the evidence by priority and, when the budget is tight, reduces snippets to signatures or summaries before dropping them. We evaluate Rivet, on two executable repository-level benchmarks, DevEval and RepoExec, with four backbone models, two context budgets (4K and 8K tokens), and eight baselines. Rivet, achieves the highest Pass@1 in all 16 settings and improves over the strongest baseline by 3.73--5.15 percentage points on average. Moreover, GPT-5-mini with Rivet, outperforms GPT-5 without Rivet,on both benchmarks while reducing inference cost by 73.3%--84.5%.
