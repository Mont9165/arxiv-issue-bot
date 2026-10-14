# Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software

- arXiv ID: `2605.30353v1`
- Authors: Nhat-Minh Nguyen
- Published: 2026-05-28
- Primary category: `cs.AI`
- Categories: `cs.AI`, `astro-ph.CO`, `cs.HC`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.30353v1) | [pdf](https://arxiv.org/pdf/2605.30353v1)

## Abstract

Are AI agents tools, co-authors, or researchers? We present a quantified case study ($N=1$): a physicist supervising an AI coding agent (Claude Code, Sonnet and Opus models) over 12 work days and 57 sessions to build CLAX-PT, a differentiable one-loop perturbation theory module in JAX. We documented and classified 15 supervision events by intervention level.
  The agent resolved ten autonomously by iterating against oracle tests. Two more by the physicist's domain knowledge. The three it could not -- all evaded oracle detection -- share a common property: the agent treated symptom reduction as root-cause resolution. It spent 33 of the 57 sessions adjusting coefficients within a code architecture that could not represent the target physics, and could not re-evaluate its CLASS-PT branch choice even when prompted to reconsider; only an injected physics concept (anisotropic BAO damping) triggered the redesign. Separately, the agent committed a calibrated correction that passed all oracle tests but corresponded to no quantity in the theory, predicting wrong values at any other cosmology.
  The fudge factor was caught and replaced within the same session. Three supervision practices proved critical for catching what oracle tests missed: testing at diverse parameter points beyond the fiducial calibration; shared changelogs that surfaced stalled exploration across sessions; and an explicit rule against unphysical numerical patches. In this case, supervision design, not model capability, determined whether the agent's output was trustworthy. Closing the gap would require agents that propose architectural alternatives rather than optimize within a given structure, and distinguish predictive adequacy from explanatory correctness -- capabilities not exhibited here, not obviously addressed by scaling alone. [Abridged.]
