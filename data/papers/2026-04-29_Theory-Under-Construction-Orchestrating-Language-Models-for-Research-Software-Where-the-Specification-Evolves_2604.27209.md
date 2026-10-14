# Theory Under Construction: Orchestrating Language Models for Research Software Where the Specification Evolves

- arXiv ID: `2604.27209v1`
- Authors: Halley Young, Nikolaj Björner
- Published: 2026-04-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.27209v1) | [pdf](https://arxiv.org/pdf/2604.27209v1)

## Abstract

Large language models can now generate substantial code and draft research text, but research-software projects require more than either artifact alone. The mathematical thesis, executable system, benchmark surface, and public claims must mature together, yet often drift apart. We identify two LM-specific failure modes: hallucination accumulation, in which claims exceed what code or theory supports and unsupported assertions propagate across sessions; and desynchronization, in which code, theory, or the model's own world model fall out of alignment.
  We propose Comet-H, an iterative prompt automaton that orchestrates ideation, implementation, evaluation, grounding, and paper-writing as coupled coordinates of a single workspace state. At each step, a controller selects the next prompt by scoring it against what the workspace currently lacks, carries unfinished follow-up work forward with a half-life, and re-checks the paper and README against the code and benchmarks whenever documentation changes. We frame prompt selection as a small contextual bandit problem over prompt families, with prompts as arms, workspace deficits as context, and a hand-weighted linear score. This transparent scorer, paired with a fading record of unfinished work, bounds long-horizon follow-ups, requires no learned policy, and makes each prompt choice legible from the workspace.
  We created a portfolio of 46 research-software repositories across two dozen domains. We study A3 in depth, a Python static-analysis tool built entirely within the loop, which reaches (F1 = 0.768) on a 90-case benchmark, compared with a next-best baseline of 0.364. Across approximately 400 commits, we find that audit-and-contraction passes dominate the later phases of every successful trajectory.
