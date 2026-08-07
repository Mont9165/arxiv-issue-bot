# CodeTeam: An LLM-Powered Multi-Agent Framework for Repository-Level Code Generation

- arXiv ID: `2606.22082v1`
- Authors: Yifei Wang, Ruiyin Li, Peng Liang, Qiong Feng, Zengyang Li, Mojtaba Shahin, Arif Ali Khan
- Published: 2026-06-20
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.22082v1) | [pdf](https://arxiv.org/pdf/2606.22082v1)

## Abstract

Natural language to repository generation (NL2Repo) requires a system to construct an entire software repository from a natural-language requirements document. Compared with function-level code generation, this task demands longer planning horizons, stable interfaces across files, and iterative debugging of cross-file inconsistencies. To address these challenges, we propose CodeTeam, an LLM-based multi-agent framework that separates planning, decision making, and implementation into distinct, coordinated stages. In the planning stage, multiple Architect agents draft competing software design sketches (SDS), optionally grounded by retrieved design references. A CTO agent then evaluates, selects, and normalizes the most promising SDS into a machine-checkable contract that specifies file ownership, public interfaces, and dependency constraints. In the implementation stage, Developer agents generate code under a dependency-aware scheduler with bounded context and lightweight Git-based coordination, while a QA agent runs tests and drives iterative repairs. On the synthesis-based SketchEval benchmark, we explicitly compare CodeTeam's prompt-engineering (PE) and supervised fine-tuning (SFT) variants with the corresponding CodeS variants, where CodeTeam improves the overall SketchBLEU by 4.1 and 2.9 absolute points, respectively. On the execution-based NL2Repo-Bench benchmark, used as an external validation protocol, CodeTeam achieves the highest average test pass rate in both settings (34.6% PE, 42.3% SFT), confirming that the sketch-improvements extend to functional correctness under upstream test suites. Ablation results show that project-specific developer allocation and retrieval-augmented planning each contribute substantially to the SketchBLEU improvement (9.9% and 8.1% relative, respectively). CodeTeam and the experimental results are available at https://github.com/WhitenWhiten/CodeTeam
