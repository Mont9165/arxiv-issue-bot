# CLEAR: Causal Context-Based Agentic Reasoning for Vulnerability Detection

- arXiv ID: `2608.03134v1`
- Authors: Sungju Yun, Sijune Hwang, Yeonjoon Lee, Kyungtae Kang, Sungbin Park
- Published: 2026-08-04
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.03134v1) | [pdf](https://arxiv.org/pdf/2608.03134v1)

## Abstract

Detecting source code vulnerabilities is increasingly difficult as modern security flaws are rooted in complex causal dependencies between execution flows, control conditions, and program states. Despite recent advances in Large Language Models (LLMs) and multi-agent frameworks, existing approaches primarily address superficial similarities between benign and vulnerable functions while failing to capture the complex causal dependencies inherent in security flaws. To address these limitations, we propose Causal Context-based Agentic Reasoning (CLEAR), a novel multi-agent vulnerability detection framework integrated with a causal knowledge graph. CLEAR systematically constructs a Vulnerability Causal Knowledge Graph (VCKG) that models the causal chains between entrypoints, preconditions, root causes, and fix intents across vulnerability instances. Leveraging this structured knowledge, four specialized agents, including the Collector, Claim, Critic, and Judge, collaboratively verify vulnerability hypotheses through retrieved causal contexts. Experimental results on C/C++ and Java vulnerability benchmarks demonstrate that CLEAR improves Pair-Correct (P-C) performance by 130.7% and 71.56% over state-of-the-art approaches, demonstrating the effectiveness of causal knowledge graph-guided reasoning for automated vulnerability detection.
