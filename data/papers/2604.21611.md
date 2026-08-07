# Process Supervision via Verbal Critique Improves Reasoning in Large Language Models

- arXiv ID: `2604.21611v1`
- Authors: Hao-Yuan Chen
- Published: 2026-04-23
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.21611v1) | [pdf](https://arxiv.org/pdf/2604.21611v1)

## Abstract

Inference-time scaling for LLM reasoning has focused on three axes: chain depth, sample breadth, and learned step-scorers (PRMs). We introduce a fourth axis, granularity of external verbal supervision, via Verbal Process Supervision (VPS), a training-free framework that uses structured natural-language critique from a stronger supervisor to guide an iterative generate-critique-refine loop up to a round budget R. Across GPQA Diamond, AIME 2025, and LiveCodeBench V6 (covering both closed and open models), VPS yields three key results. First, on GPQA Diamond, GPT-5.4 (High) | GPT-5.4 (Low) reaches 94.9% at R=4, surpassing the 94.1% state of the art without gradient updates. Second, on AIME 2025, VPS enables strong weak-actor rescue, boosting scores from 11.7-26.7% to 63.3-90.0% (up to +63.3 points). Third, at matched compute, VPS outperforms Reflexion by +8.5 to +12.1 points and Self-Consistency@5 by +5.0 pp (GPQA) and +8.3 pp (LiveCodeBench), isolating critique granularity as the key driver. Performance scales with the supervisor-actor capability gap (Pearson r=0.90) and degrades when errors are not linguistically expressible (e.g., code synthesis), motivating hybrid verbal-executable methods. These results establish critique granularity as a new axis of inference-time scaling.
