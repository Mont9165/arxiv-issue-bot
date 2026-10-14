# ALTSTEER: Selective Safety Steering for Moving Beyond Hard Refusals to Constructive Alternatives

- arXiv ID: `2608.30197v1`
- Authors: Hoejoon Kwon, Byeonggeuk Lim, Kahyeon Kim, YoungBin Kim
- Published: 2026-08-31
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.30197v1) | [pdf](https://arxiv.org/pdf/2608.30197v1)

## Abstract

Safety alignment is essential for deploying large language models, requiring systems to prevent harmful compliance while preserving helpfulness on benign requests. Activation steering offers a training-free inference-time approach to safety control, but effective safety steering requires addressing two coupled questions: when to intervene and how generation should be shaped after intervention. However, existing safety steering methods remain limited along both dimensions, as their triggering mechanisms can be unstable across domains and refusal-oriented steering often yields rigid refusals rather than constructive safe guidance. To address these limitations, we propose ALTSTEER, an inference-time framework that couples selective intervention with refusal-anchored constructive redirection within a single inference pass. ALTSTEER uses an internal refusal-relevant signal to decide when to steer, and applies staged steering to shift generation from refusal-oriented control toward constructive alternatives. Evaluations on Llama-3.1 and Qwen2.5 show that ALTSTEER preserves benign utility while improving constructive safe-completion behavior, especially on models that otherwise tend to produce short refusals for harmful requests.
