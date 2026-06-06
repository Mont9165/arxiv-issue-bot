# Scaffold, Not Vocabulary? A Controlled, Two-Tier, Pre-Registered Study of a Popperian Code-Generation Skill

- arXiv ID: `2606.06454v1`
- Authors: Mehmet Iscan
- Published: 2026-06-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2606.06454v1) | [pdf](https://arxiv.org/pdf/2606.06454v1)

## Abstract

Large language models increasingly write, review, and judge code, and a fast-growing practice equips them with prompt 'skills' that ask the model to reason like a scientist. A prominent example tells the model to act as a Popperian falsificationist, and such skills are reported to improve generated code. But these gains are almost always read off an LLM-as-a-judge, an instrument with documented positional, self-preference, and stylistic biases. We ask: if it appears to help, is the gain from the skill's Popperian content, or from the structure any scaffold imposes? We pre-register a two-tier ablation with three controls: a length-matched placebo, a labels-only scaffold that keeps the Popperian headers but strips the procedure, and an execution oracle (HumanEval+ unit tests), plus a vocabulary-halo sentinel and a same-model self-judge audit. On a frontier model (Claude Sonnet 4.6, N=163) all conditions sit near the benchmark ceiling and do not separate, so the pre-registered +5-point improvement is not supported (a ceiling-limited non-detection). On a small model (Qwen2.5-Coder-0.5B, N=164) structured arms lift best-of-eight correctness by 20-22 points, but the full skill shows no separable benefit over a labels-only scaffold (aggregate F@8=L@8 vs V@8=34.8%), and the placebo trails by only 2.4 points. A 0.5B self-judge applying the Popperian rubric does not beat random selection and concentrates 60% of its picks on one index. In the two settings tested, the skill's Popperian procedural content adds no separable execution-correctness benefit beyond a labels-only scaffold, so the gains track scaffold structure. We contribute a calibrated negative result and a reusable disambiguation protocol; the finding bounds an engineering claim about one prompt-skill family and is not an evaluation of Popperian methodology in general.
