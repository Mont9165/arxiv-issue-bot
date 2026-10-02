# Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming

- arXiv ID: `2610.00863v1`
- Authors: Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, Michael Liut
- Published: 2026-10-01
- Primary category: `cs.CY`
- Categories: `cs.CY`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.00863v1) | [pdf](https://arxiv.org/pdf/2610.00863v1)

## Abstract

Large language models can generate plausible solutions to programming assignments, making it tempting to detect their use by matching student code against a reference bank of generated solutions. Yet similar code can also arise when an assignment admits only a few natural implementations, which leaves open what a match actually shows.
  We investigate generated-reference matching using 29,970 student submissions from ten Python labs offered in 2021, 2023, and 2025, together with 90,000 solution attempts generated retrospectively by three frontier LLMs. We validate the generated solutions using hidden instructor tests, compare code with MOSS after excluding the starter code, and examine the exact abstract syntax tree (AST) forms of selected functions.
  The models usually produced correct solutions and, across most assignments, converged on similar implementations. Student submissions matched the generated references more often in later cohorts, including among submissions that passed every hidden test. On tightly specified functions, the models converged on a few exact abstract-syntax-tree forms, and the number of distinct student forms also declined across cohorts, whereas open-ended functions remained diverse in both sources. Most reported overlaps were short, making the minimum match length an important choice when reviewing students' code.
  Finally, we discuss how instructors can build a reference bank of generated solutions before releasing an assignment to identify tasks on which generated solutions converge, decide how much review a match warrants, and redesign tasks to elicit tests, reasoning, and intermediate work. These findings support tracking population-level changes in submitted code, while attributing AI use to an individual submission would require additional evidence about how it was produced, such as prompts, revisions, intermediate code, and student disclosures.
