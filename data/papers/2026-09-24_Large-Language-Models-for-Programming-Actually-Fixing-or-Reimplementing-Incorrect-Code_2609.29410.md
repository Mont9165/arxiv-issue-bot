# Large Language Models for Programming: Actually Fixing or Reimplementing Incorrect Code?

- arXiv ID: `2609.29410v1`
- Authors: Alexandru Stefan Stoica, Traian Rebedea, Marian Cristian Mihaescu
- Published: 2026-09-24
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.29410v1) | [pdf](https://arxiv.org/pdf/2609.29410v1)

## Abstract

Recent studies have shown that Large Language Models can effectively solve problems and fix bugs in diverse programming environments, including competitive programming. Existing approaches primarily evaluate LLM performance in problem solving or bug fixing independently, but do not explore the relationship between these two capabilities. This work focuses on determining how much the LLM deviates from a buggy solution to fix the bug compared to a human-written patch, and if there is a bias towards generating entirely new solutions. We construct a dataset with all the submissions ($\sim$ 3000) from a couple of users from Codeforces, and we match each buggy submission with its corresponding human fix. By using the similarity between the buggy solution and the human fix as a baseline, we evaluate the quality of LLM-generated bug fixes on 3 OpenAI GPT models (gpt-5-nano, gpt-5-mini, gpt-5.1). We check if the generated solutions solve the problem by using the Codeforces-R1 dataset, an openly available dataset that has tests generated with the DeepSeek-R1 model. Our findings suggest that LLMs tend to modify more lines than necessary compared to human fixes and, in some cases, generate entirely new solutions. We also observe that LLMs solve more problems correctly when allowed to generate solutions from scratch rather than patch buggy submissions, even when those submissions are close to the human patch. This has important implications for the design of AI-assisted programming tools, particularly in supporting user debugging processes and promoting incremental problem-solving strategies rather than solution replacement.
