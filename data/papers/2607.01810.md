# Decoupling Code Complexity from Newcomer Participation: A Causal Study of AI Coding Agent Adoption in OSS

- arXiv ID: `2607.01810v1`
- Authors: Weiwei Xu, Xuanning Cui, Hengzhi Ye, Minghui Zhou
- Published: 2026-07-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.01810v1) | [pdf](https://arxiv.org/pdf/2607.01810v1)

## Abstract

Open-source projects depend on a steady inflow of newcomers. A growing concern is that AI coding agents (tools such as Cursor and Claude Code that write code from natural-language instructions) will crowd them out, by absorbing the simple tasks that beginners start with and by making code harder to read. We give this concern a causal answer. Using GitHub code search we identify 1,888 projects that adopted an agent, signaled by their first commit of a configuration file. We apply difference-in-differences against matched non-adopting controls, restricting the main analysis to the 603 adopters with a genuine pre-adoption period. We find no evidence of crowding-out: across estimators newcomer inflow shows no significant decline after adoption (point estimates run from a small increase to, under the most conservative trend specification, a slight and insignificant dip), onboarding and retention are unchanged, and a sparse, correlational beginner-task measure (good-first-issue labels, which we cannot test for parallel trends) shows no decline. The feared mechanism is real but decoupled: adoption raises per-function code complexity (about +11% on a cognitive metric for Python, a quarter of the prior estimate, and +3 to 4% in cyclomatic terms across all languages), yet in fixed-unit subsets where complexity rose (Python on the cognitive metric, and all languages on the cyclomatic metric), newcomer participation does not decline. These results suggest that, in established open-source projects, adopting an AI coding agent makes code modestly more complex but does not crowd out the human newcomers that a project depends on: the feared trade-off between AI assistance and human participation does not materialize.
