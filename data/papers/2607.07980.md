# 3100 Opinions on Code Review in an AI World: Building Causal Theory from Practitioner Discourse

- arXiv ID: `2607.07980v1`
- Authors: Shyam Agarwal, Courtney Miller, Christian Kästner, Bogdan Vasilescu
- Published: 2026-07-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.07980v1) | [pdf](https://arxiv.org/pdf/2607.07980v1)

## Abstract

Coding agents now author entire pull requests, and practitioners sharply disagree about what this does to code review: whether it becomes the bottleneck, whether human review is still necessary, and whether it quietly erodes the understanding that it once built. Repository-mining studies measure surface trends but seldom explain the mechanisms beneath them, and the trends themselves prove unstable. A motivating observational analysis of public GITHUB activity finds that agent-authored pull requests are reviewed less often, merged several times faster, and discussed less than human-authored ones, yet the direction of these trends flips under different but equally defensible analysis choices, so the traces establish what is changing without explaining why. To recover the mechanisms, we synthesize practitioner discourse at scale into an explanatory theory: we collect 38,709 grey-literature documents (engineering blogs and Reddit threads), filter to those substantively about code review, and code a stratified random sample of 3,100 with an LLM-assisted pipeline, from which we build a causal model of 26 constructs and 67 relationships (64 directed, 3 contested). Its organizing claim is that review is the control point through which a coding agent's effect on software is decided, and that AI does not fix the sign of that effect: the team sets it, through the expertise its humans bring and how it structures the review process. The theory makes the competing positions explicit and turns "AI is changing code review" into falsifiable propositions with named constructs and moderators. As a secondary contribution, we offer the underlying LLM-assisted, grey-literature theory-building method as a scalable template for software-engineering research, with a public implementation.
