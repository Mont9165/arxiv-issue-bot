# Is Three the Magic Number? An Empirical Evaluation of LLM-Based Repair Loops

- arXiv ID: `2607.05197v1`
- Authors: Tobias Kiecker, Eik Reichmann, Hosung Kang, Gabin An, Lars Grunske
- Published: 2026-07-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.05197v1) | [pdf](https://arxiv.org/pdf/2607.05197v1)

## Abstract

Iterative repair loops have become a core design pattern in LLM-based software engineering systems. These workflows repeatedly generate, validate, and repair artifacts using feedback such as compiler errors or test failures. Despite their widespread use, the impact of repair-loop iteration limits remains poorly understood, as most prior work adopts fixed, often arbitrary, repair budgets. We study repair-loop effectiveness across multiple software engineering tasks, including code generation, test generation, and code translation. Across several representative workflows, datasets, and contemporary low-cost LLMs, we observe a consistent pattern of diminishing returns: the first three to four repair iterations account for most achievable gains, while later iterations contribute only marginal improvements. We further find that repair behavior is influenced more strongly by workflow orchestration and feedback design than by the underlying model itself. These results suggest that repair budgets should be treated as an explicit experimental variable, as they directly affect evaluation outcomes, computational cost, runtime, and reproducibility in LLM-based software engineering research.
