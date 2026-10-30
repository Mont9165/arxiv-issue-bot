# Beyond Passing Tests: A Systematic Review and Controlled Re-evaluation of Techniques for Improving the Quality of LLM-Generated Code

- arXiv ID: `2610.38977v1`
- Authors: Prashank Kadam
- Published: 2026-10-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2610.38977v1) | [pdf](https://arxiv.org/pdf/2610.38977v1)

## Abstract

Large language models pass most functional-correctness benchmarks, but passing tests says little about whether their code is readable, efficient or secure. Many techniques claim to improve these qualities, yet their evidence is scattered, usually covers one quality dimension and is rarely compared at an equal compute budget. We contribute a systematic review and a controlled re-evaluation. A systematic literature review of 628 primary studies (July 2021 to October 2026), with disclosed, author-reviewed LLM assistance, organizes the techniques by stage, signal source and quality target. Most studies measure only the dimension they target, gains often come with unchanged or unreported correctness, single automated quality signals are gamed, and compute, variance and contamination are rarely reported. A controlled re-evaluation runs ten techniques on four models at matched budgets on correctness, maintainability, efficiency and security benchmarks, extends it to thirteen current models and repository-level tasks, and compares 66 highlighted techniques head-to-head on Gemma 4 31B. At one call, quality prompting raises analyzer issue counts and leaves complexity and judge scores almost unchanged. At matched budgets, best-of-n sampling with an analyzer-weighted ranker matches or beats prompting, planning, self-refinement, a reviewer agent and retrieval on measures the ranker does not optimize, while an analyzer feedback loop and fine-tuning beat it only on analyzer issue counts. Large correctness losses on HumanEval+, a likely contaminated benchmark near its ceiling, do not appear on contests held after the models' training cutoffs. In the head-to-head, 1 of 66 techniques beats best-of-n on its primary target beyond the 95% interval, a rate consistent with chance. Gains should be reported against a budget-matched sampling baseline and on measures independent of the technique's own signal.
