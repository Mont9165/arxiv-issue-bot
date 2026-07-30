# Try Again, Don't Look Back: Blind Resampling Outperforms Self-Repair in Small Code Models

- arXiv ID: `2607.26117v1`
- Authors: Yuvraj Verma
- Published: 2026-07-28
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.26117v1) | [pdf](https://arxiv.org/pdf/2607.26117v1)

## Abstract

Self-repair - returning a failed program to the model together with its test output and asking for a correction - is a standard component of code agents, and is almost always evaluated against a baseline that does not retry at all. We argue that this comparison confounds the value of the feedback with the value of the extra attempt. Using a placebo-controlled design on MBPP+ at three model scales (1.5B, 3B, 7B), we compare four matched-budget retry conditions: blind resampling, a content-free failure notice, genuine execution feedback, and feedback augmented with verbal self-reflection. Blind resampling is the strongest condition below 7B, and remains statistically tied with the best condition at 7B, while consuming 2.5-5.5x fewer tokens; conditioning on the model's own failed attempt costs 6.1 points at 1.5B (p=0.006), and the informational content of execution feedback adds nothing measurable over the placebo. We attribute this to anchoring: when shown its previous attempt, a model reproduces a near-identical program in 33-68% of retries, against 2-14% under blind resampling. Two further experiments delimit the effect. Retrieved solutions to other tasks change nothing (bounded to +/-3.5 points), which localizes the harm to self-conditioning rather than context length; and reflection, the only condition that measurably weakens the anchor, remains dominated on cost. Replication rules out two competing explanations: the penalty is unchanged at full precision, and it reproduces on an independent model family. Across six configurations spanning two families and two precisions, its magnitude is predicted by baseline quality alone (r=0.96) - the cost of anchoring is the cost of committing to a bad first attempt.
