# Correct Verdicts, Flawed Reasoning: Structured Auditing of LLM-based Vulnerability Reasoning

- arXiv ID: `2610.06366v1`
- Authors: Boyue Caroline Hu, Kaivalya Ahir, Ronghao Ni, Limin Jia
- Published: 2026-10-05
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.06366v1) | [pdf](https://arxiv.org/pdf/2610.06366v1)

## Abstract

Large Language Models (LLMs) are increasingly deployed for automated software vulnerability analysis. Binary classification alone is insufficient; practitioners need explanations to triage bugs and engineer patches. Standard practice relies on Chain-of-Thought (CoT) prompting, but free-form reasoning allows models to obscure logical leaps, hallucinated execution steps, and internal inconsistencies behind plausible prose. Our manual audit reveals that approximately 60% of correct vulnerability verdicts are accompanied by fabricated or unverifiable claims, and free-form explanations allow reasoning errors to evade LLM-as-a-judge evaluation.
  We present Vulnerability Explanation Reasoning Auditor (VERA), an automated framework for auditing LLM vulnerability reasoning. Rather than accepting free-form text, VERA asks models to output a Structured Reasoning Record (SRR) encoding tracked pointers, memory operations, and state transitions in machine-readable fields. A multi-stage judge audits each SRR against eight reasoning failure modes using deterministic checks, with LLM calls reserved for semantic interpretation. The standardized SRR schema also enables automated mutation testing to benchmark judges at scale without human annotation. Our evaluation shows reasoning flaws occur in correct verdicts just as frequently as incorrect ones, and VERA exposes 87% of reasoning errors that free-form LLM-as-judge systematically miss.
