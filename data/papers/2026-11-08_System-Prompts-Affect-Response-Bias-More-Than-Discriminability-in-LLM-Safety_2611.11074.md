# System Prompts Affect Response Bias More Than Discriminability in LLM Safety

- arXiv ID: `2611.11074v1`
- Authors: Mohan W. Gupta, Sandy Tanwisuth
- Published: 2026-11-08
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.11074v1) | [pdf](https://arxiv.org/pdf/2611.11074v1)

## Abstract

Large language model safety evaluations often focus on a compliance-refusal tradeoff: models should refuse unsafe requests without refusing safe ones. We argue that this misses a broader form of prompt-conditioned task selection, where the same request can elicit different behaviors depending on the system prompt. We investigate this using a controlled evaluation crossing eight safety-task prompt families with three clarity levels across HarmBench, XSTest, and IHEval. Holding benchmark items fixed, we evaluate 13 models and use signal detection theory to distinguish two possibilities: whether models become better at telling safe from unsafe requests (discriminability), or simply more willing to refuse (response criterion). We find substantial differences in discriminability across models, but system prompts primarily shift the willingness to refuse, with smaller and less consistent effects on discriminability. Increasing prompt clarity makes models more willing to refuse without reliably improving their ability to distinguish safe from unsafe requests. Beyond refusal, prompt families also shift responses among six distinct behavioral policies, including clarification and safe help. Together, these findings show that system prompts primarily change how models respond to safety-relevant requests rather than consistently improving their ability to distinguish safe from unsafe ones.
