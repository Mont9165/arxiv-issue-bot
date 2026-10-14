# SecDrift: Measuring Sector-Conditioned Security Drift in AI-Generated Code

- arXiv ID: `2607.25225v1`
- Authors: Narayanaswami Natraj Bharadwaj, Dhivya Chandramouleeswaran
- Published: 2026-07-28
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.25225v1) | [pdf](https://arxiv.org/pdf/2607.25225v1)

## Abstract

LLMs are increasingly used for code generation in critical infrastructure, yet the security effect of domain-specific prompting is understudied. We present SecDrift, a benchmark measuring sector-conditioned security drift: the change in static-analysis vulnerability rates when prompts are conditioned on industry contexts versus neutral baselines. We evaluate 7 LLMs (6 producing analyzable code) across 8 CISA critical infrastructure sectors and 9 CWE categories with 5 replicates (5,355 evaluations), using a 5-dimension transformation with a matched-baseline condition that holds the task fixed while substituting only domain terminology. Industry prompts naively appear more secure (14.0% vs. 11.4%, -2.7pp), but the gap is not statistically significant (Fisher's exact p = 0.24, Cohen's h = -0.08) and is a composition artifact of two CWE categories: excluding CWE-502 and CWE-22 eliminates and slightly reverses it (+0.4pp, p = 1.00). A mixed-effects logistic regression confirms sector identity is not a moderator and localizes the only detectable condition effect to those two vulnerability types. 0 of 8 sectors show drift distinguishable from baseline, corrected or uncorrected (|h| < 0.15). A placebo on two non-CISA sectors (e-commerce, online education) reproduces the CISA industry rate almost exactly (10.5% vs. 11.4%, p = 0.63): the small pooled pattern reflects generic industry-framing specificity, not critical-infrastructure identity. In contrast, model selection has a large and consistent effect: among full-output models vulnerability rates range from 11.6% to 16.1%, and these differences persist across conditions. Model choice, not prompt framing, is the more reliable security lever. We release the framework, prompts, generated code, findings, human-validation verdicts, and analysis scripts.
