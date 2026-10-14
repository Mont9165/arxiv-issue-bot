# Prompt Structure Redistributes, Not Reduces: An Empirical Analysis of Security-Weaknesses in LLM-Generated Python Code

- arXiv ID: `2608.24857v1`
- Authors: Maitreyee Das Urmi, Jessica Pourleyli, Fabio Santos, Glaucia Melo
- Published: 2026-08-25
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.24857v1) | [pdf](https://arxiv.org/pdf/2608.24857v1)

## Abstract

Large Language Models (LLMs) increasingly generate code from natural-language prompts, making prompt engineering a key mechanism for shaping the security of generated software. Structured and security-oriented prompts are widely used to encourage safer code, yet their effects extend beyond whether detected weaknesses are simply present or absent. Using 424 security-sensitive Python tasks, we generate solutions with GPT-4o and LLaMA 3.1-8B under five prompt variants that progressively add structural and security guidance, and evaluate them with Bandit and CodeQL along two axes: generation compliance and security weakness prevalence, severity, and CWE distributions. Structured prompting substantially reduces refusals (e.g., GPT-4o invalid outputs drop from 338 of 424 to 37-52), enabling large-scale analysis, but security-oriented refinements do not consistently reduce overall weakness prevalence. For GPT-4o, stronger prompts primarily redistribute risk: high-severity findings fall (20.8% to 13.6%) while low-severity findings rise (32% to 43.5%); LLaMA shows weaker, less consistent shifts. We also observe security-driven semantic drift, where stricter prompts silently remove or rewrite explicitly requested unsafe constructs. Overall, prompt structure improves compliance but is an unreliable substitute for robust security controls in LLM-assisted development.
