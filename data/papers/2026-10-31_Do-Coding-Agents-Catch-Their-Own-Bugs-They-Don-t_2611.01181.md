# Do Coding Agents Catch Their Own Bugs? (They Don't.)

- arXiv ID: `2611.01181v1`
- Authors: Shaswat Patel, Michel Liao, Peter Henderson, He He, Valerie Chen
- Published: 2026-10-31
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.01181v1) | [pdf](https://arxiv.org/pdf/2611.01181v1)

## Abstract

In software development, engineers need to foresee and fix potential problems with their code that are not explicitly specified in requirements---such as pre-emptively considering vulnerabilities or other bugs from a code change. But current benchmarks often do not measure these future-looking consequences. We introduce $\textbf{Foresight-SWE}$, a benchmark for measuring whether coding agents can anticipate and address unstated problems during software engineering tasks. Foresight-SWE consists of 212 samples spanning 4 languages and 35 popular open-source repositories. Each sample contains two pull requests (PRs), the second of which resolves defects the first one introduced. To measure whether agents exhibit foresight, we define the $\textbf{foresight resolve rate (FRR)}$ as the fraction of instances where an agent fully resolves the original task while also avoiding the defect identified by a later PR. We evaluate eleven large language models and find that FRR ranges from only 6.13% to 24.53%, indicating that models largely fail to address problems introduced by the first PR change. This raises important questions about how models are trained and aligned in coding contexts, as well as how code review tools should be improved for more fail-safe coding. Foresight-SWE shifts evaluations in this direction.
