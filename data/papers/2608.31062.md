# The Exclusion Ratchet: False-Positive Suppression Accumulates and Persists in Detection Rule Repositories

- arXiv ID: `2608.31062v1`
- Authors: Sudaroli Dhananjeyan, Kumaran U
- Published: 2026-08-31
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.31062v1) | [pdf](https://arxiv.org/pdf/2608.31062v1)

## Abstract

When a rule produces too many false alarms an analyst adds an exclusion, and the rule thereafter declines to alert in that circumstance. Each such decision is locally reasonable; what becomes of them collectively is not known. Recent longitudinal work established that curation does not converge, but measured restoration time only for revisions that were later reverted -- a measure silent about narrowing that is never undone. We measure that. Across nine years and 8,234 revisions of the SigmaHQ corpus we detect suppression semantically -- growth in the set of predicates held under negation without compensating growth in coverage -- and validate it against blinded hand labelling (precision 0.828, recall 0.911). The test is deterministic: nothing is learned from the data, and the definitions are released as code. Exclusions were added 1,642 times and withdrawn 304, a ratio of 5.4 to 1 that rises to 13 to 1 at the level of the individual rule. Thirty-one per cent of the narrowing is invisible to structural comparison, which existing structural accounts therefore undercount. Estimated by Kaplan-Meier, 86.7 per cent of exclusions remain in force three years on, and persistence is independent of whether the rule is the only coverage for its ATT&CK technique (p = 0.49). Of path-valued exclusions, 64.1 per cent can be satisfied by an unprivileged process that chooses a filename. Narrowing accumulates, is rarely revisited, and is not triaged by consequence. We give a criterion for deciding which exclusions to examine first.
