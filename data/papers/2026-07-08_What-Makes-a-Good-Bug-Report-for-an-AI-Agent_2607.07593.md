# What Makes a Good Bug Report for an AI Agent?

- arXiv ID: `2607.07593v1`
- Authors: Lara Khatib, Noble Saji Mathews, Meiyappan Nagappan, Pengyu Nie, Thomas Zimmermann
- Published: 2026-07-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.07593v1) | [pdf](https://arxiv.org/pdf/2607.07593v1)

## Abstract

Automated program repair (APR) agents are transitioning from research benchmarks to developer workflows, yet they still begin with bug reports written for human developers. While decades of research have established what makes a good bug report for humans (e.g., steps to reproduce, stack traces), it remains unclear whether these features transfer to LLM-based agents. We study this question in two analyses. First, we use statistical modeling to examine associations between 27 bug-report features and repair success across 433 SWE-bench Verified issues attempted by 87 repair agents. We find that fix suggestions, reproduction scripts, repository source code, and localization info are associated with higher resolution likelihood, while longer reports are associated with lower odds. Second, we conduct controlled ablations across 2 models and 17 problem-statement mutations on SWE-bench Pro, varying the information available to an agent while holding the underlying task fixed. We remove or isolate selected bug-report content, delete fault-localization cues, and test structural changes that flatten lists or remove section headers. We find that both models depend on localization cues and expected behavior, and that structural changes alone can reduce solve rates, even without removing any content. The two models diverge in how they handle missing information: Qwen searches more widely and can exhaust its turn budget, while Gemma commits to a plausible interpretation early and patches on it. Our findings indicate that a good bug report for an agent overlaps with, but is not identical to, a good report for a human: agents benefit most from concrete, executable, and well-localized information, whereas some qualities long emphasized for human readers, such as natural language steps to reproduce and readable descriptions, contribute little or even correlate with lower success.
