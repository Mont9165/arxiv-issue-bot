# Position: Evaluation Scores Are Perishable Knowledge Claims

- arXiv ID: `2607.26191v1`
- Authors: Sankalp Gilda, Shlok Gilda
- Published: 2026-07-28
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.26191v1) | [pdf](https://arxiv.org/pdf/2607.26191v1)

## Abstract

Evaluation methodologies for language models increasingly combine multiple signals, from automated metrics and LLM-as-judge ratings to human assessments and benchmark suite results. When these signals are aggregated via averaging, evaluation confidence can then substantially exceed the reliability of the weakest signal: a phenomenon we call trust inflation in evaluation. We argue that evaluation scores should be treated as epistemic claims with three properties: formality (human evaluation provides stronger evidence than an automated metric), scope (a benchmark result applies to the tested distribution, not universally), and validity windows (benchmark results expire as contamination accumulates and distributions shift). Several converging research traditions (chain-of-thought analysis, possibilistic logic, and algebraic theory) establish weakest-link aggregation as the conservative endpoint of a parameterized operator family controlled by a single pessimism parameter. Drawing on those traditions, and on concrete lessons from building an evaluation harness for agentic AI, we propose that evaluation results carry explicit metadata (formality tier, scope declaration, and expiration date) to make their epistemic status transparent. We illustrate the cost of mean aggregation on the public HELM leaderboard: across 54 frontier models on ten scenarios, the top-five models ranked by mean score and by weakest-link are completely disjoint.
