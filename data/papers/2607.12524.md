# Open-Source Intelligence for Code Provenance and the Security Patterns that Separate Human and Large-Language-Model Implementations of Common Programming Tasks

- arXiv ID: `2607.12524v1`
- Authors: Mohammadreza Rashidi
- Published: 2026-07-14
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.12524v1) | [pdf](https://arxiv.org/pdf/2607.12524v1)

## Abstract

Developers now draw code from two very different sources, the accumulated human answers on sites such as Stack Overflow and the output of large language models. We ask two questions about that split. First, can the provenance of a code snippet be recovered from the code itself, and second, do the two sources differ in the security patterns they adopt for the same task. Using only open sources, a public gateway of open-weight language models and the public Stack Overflow API, we build a fully reproducible pipeline that collects real implementations of 31 security-sensitive programming tasks, among them OAuth with PKCE, JWT verification, password hashing, and SQL access, from 9 language models and from human answers, and scores every sample with deterministic security and style detectors. On 528 real samples we train a cross-validated classifier that recovers human versus model provenance with 93 percent accuracy against a 78 percent baseline, and a 7-way classifier that attributes a sample to the specific model that wrote it at 48 percent. We then report where the sources diverge on security, which patterns models adopt more often than the human corpus and which they inherit from it. Running the same tasks in Python, JavaScript, Go, and Java, we find the security divergence holds in every language while the provenance boundary is partly language-specific and does not transfer symmetrically between them. A vulnerability repair case study, in which models are handed insecure code and asked to fix it, finds a 77 percent repair rate across 21 seeds and 12 weakness classes, but a recurring partial-fix failure in which the model removes the insecure pattern without adding the correct defense. The pipeline is data driven, so any new task or language is added as a single specification entry, and a fail-closed checker re-derives every number in this paper from the stored data.
