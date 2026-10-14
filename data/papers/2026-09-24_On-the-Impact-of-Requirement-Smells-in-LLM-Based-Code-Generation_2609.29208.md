# On the Impact of Requirement Smells in LLM-Based Code Generation

- arXiv ID: `2609.29208v1`
- Authors: Hugo Villamizar, Jannik Fischbach, Mert Şahin, Julian Frattini, Alessio Ferrari, Alexander Korn, Andreas Vogelsang, Daniel Mendez
- Published: 2026-09-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.29208v1) | [pdf](https://arxiv.org/pdf/2609.29208v1)

## Abstract

Software requirements are typically incorporated into prompts used in LLM-assisted software development. Recent work has shown that requirement smells can affect automated traceability between requirements and code, but empirical evidence on their effects in code generation remains limited. To address this gap, we build upon a prior study on automated traceability by reusing its dataset and requirement smell taxonomy, while extending it to evaluate the functional correctness of LLM-generated code. Using a benchmark consisting of requirements and corresponding system tests for four applications, we progressively introduced semantic, syntactic, and lexical smells into otherwise clear requirements and analyzed their influence on generated implementations. Our results suggest that increasing \textit{smell density} was generally associated with lower test-suite-based functional correctness, although non-smelly requirements could still produce faulty code. We also found that different smell categories had similar effects. These findings provide additional empirical evidence of the importance of requirement quality in LLM-assisted code generation, while showing that high-quality requirements alone do not guarantee correctness, as these depends on several factors, including the LLM. Compared with previous work, our results suggest that the impact of requirement smells depends on the software engineering task: whereas their effects on traceability were modest, code generation appears more sensitive. Overall, this work motivates further investigation into task-dependent quality effects in LLM-assisted software engineering.
