# LLM-based vs. Search-based Merge Conflict Resolution: An Empirical Study of Competing Paradigms

- arXiv ID: `2605.16646v1`
- Authors: Heleno de Souza Campos Junior, Leonardo Gresta Paulino Murta
- Published: 2026-05-15
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.16646v1) | [pdf](https://arxiv.org/pdf/2605.16646v1)

## Abstract

Context: The resolution of software merge conflicts is being reshaped by two competing paradigms: generative approaches based on Large Language Models (LLMs) and optimization approaches from Search-Based Software Engineering (SBSE). While tools from both paradigms have shown promise, their relative strengths, weaknesses, and trade-offs are not yet well understood.
  Objective: This paper presents the first in-depth empirical study directly comparing these paradigms to identify their capabilities and limitations in real-world scenarios.
  Method: We evaluated MergeGen, a state-of-the-art LLM-based tool, against SBCR, a novel SBSE approach employing a Random Restart Hill Climbing (RRHC) algorithm. The comparison used thousands of real-world conflicts from open-source projects written in Java, C#, JavaScript, and TypeScript.
  Results: Our findings reveal fundamental trade-offs. The LLM paradigm excels at resolving conflicts with imbalanced content by leveraging learned patterns. However, it struggles with non-English content and large inputs, which can lead to truncated or empty resolutions. Conversely, the SBSE paradigm demonstrates superior generalization across datasets and performs best on balanced conflicts, highlighting its potential as a robust, data-independent alternative.
  Conclusions: Neither paradigm is a silver bullet. Our findings highlight context-dependent strengths and motivate the development of hybrid systems that combine the complementary capabilities of LLM and SBSE approaches to create more robust and reliable merge conflict resolution tools.
