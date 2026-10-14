# Evidence Absence Is Not Evidence Insufficiency: Diagnosing NEI Construction Artifacts in Fact Verification

- arXiv ID: `2605.26663v1`
- Authors: Jingxi Qiu, Zeyu Han, Cheng Huang
- Published: 2026-05-26
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.IR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.26663v1) | [pdf](https://arxiv.org/pdf/2605.26663v1)

## Abstract

Evidence absence is not evidence insufficiency, but fact verification benchmarks can make them observationally similar. The Not Enough Information (NEI) label is often operationalized through different evidence conditions, and that choice silently determines what a verifier learns and what its score can hide. We introduce NEI-CAP, a construction-aware diagnostic protocol for insufficient-evidence evaluation. Each NEI example carries the construction family that produced it; NEI-CAP audits shortcut cues, validates hard cases through human adjudication, and tests whether competence transfers across constructions. We instantiate the protocol in SciFact-style scientific verification, with FEVER and HoVer as bounded external controls. Across these settings, NEI competence does not transfer reliably: models trained on shortcut-prone constructions fail to recognize semantically related insufficient evidence, and mixed-construction training narrows but does not close the gap. Fixed-claim diagnostics further show that the evidence condition shifts confidence in the reference Support/Refute label, not only NEI recall, so an aggregate NEI score can hide which problem a model has actually solved.
