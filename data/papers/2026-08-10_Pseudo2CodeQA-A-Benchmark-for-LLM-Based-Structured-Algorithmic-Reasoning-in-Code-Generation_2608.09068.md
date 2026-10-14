# Pseudo2CodeQA: A Benchmark for LLM-Based Structured Algorithmic Reasoning in Code Generation

- arXiv ID: `2608.09068v1`
- Authors: Shadikur Rahman, Umme Ayman Koana, Syed Muhammad Danish
- Published: 2026-08-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.09068v1) | [pdf](https://arxiv.org/pdf/2608.09068v1)

## Abstract

Large Language Models (LLMs) have achieved impressive performance in natural language-to-code generation; however, their ability to follow structured algorithmic reasoning remains insufficiently understood. We introduce Pseudo2Code, a benchmark designed to systematically evaluate the impact of structured pseudocode on code generation quality and algorithmic faithfulness. The benchmark consists of 300 manually validated real-world programming tasks spanning multiple domains and three difficulty levels (Easy, Medium, and Hard). Each task contains a problem description, structured pseudocode, reference implementation, and executable test suite. To ensure benchmark reliability, we adopt a dual-stage human validation protocol and release fully executable benchmark instances. Beyond the benchmark, we propose the Pseudo2Code Agentic Framework, a multi-stage pipeline that leverages pseudocode as an explicit intermediate reasoning representation for code generation. We evaluate both commercial and open-source language models using a rubric-based evaluation framework that measures correctness, completeness, relevance, clarity, reasoning quality, and pseudocode adherence, complemented by execution-based testing. Experimental results demonstrate that the proposed Pseudo2Code Agentic Pipeline consistently outperforms strong commercial and open-source baselines, achieving an overall score of 4.78 compared to 4.31 for the strongest baseline model. Furthermore, a human evaluation study involving 100 benchmark tasks shows strong agreement between human judgments and automated assessments. Our findings provide empirical evidence that structured pseudocode improves functional correctness, reasoning quality, and algorithmic faithfulness in code generation. We release Pseudo2Code to support future research on structured reasoning, interpretable code generation, and reliable AI-assisted software development.
