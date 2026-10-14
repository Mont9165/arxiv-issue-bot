# The Librarian Who Refused to Code: Model-Dependent Identity Enactment in LLM Code Generation

- arXiv ID: `2607.17420v1`
- Authors: Shayell Aharon Salomon, Noam Israel, Ido Safruti, Amir Shaked
- Published: 2026-07-19
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.17420v1) | [pdf](https://arxiv.org/pdf/2607.17420v1)

## Abstract

Biographical personas are widely used in system prompts, but their effects on code generation are rarely evaluated under controlled, pre-registered conditions. We tested four prompt conditions (no persona, two engineer personas, and a research-librarian persona), 12 code-generation tasks, two frontier models, and five runs per cell (480 completions). Persona effects differed between the two tested models. Under the pre-registered mixed-effects analysis, the condition-by-model interaction was significant for provider-reported output tokens; a post-hoc visible-character measure showed the same qualitative pattern. Six GPT-5.5 completions were length-capped and are reported separately. On Claude Opus, the minimalist engineer persona reduced visible output by 30% (33% in provider tokens) without improving correctness, while the thorough engineer persona increased output without a correctness gain. In an exploratory post-hoc analysis, the librarian persona elicited in-character disclaimers in 55 of 60 Opus responses and 12 genuine no-code responses, lowering mean correctness from 0.92 to 0.67. GPT-5.5 produced neither behavior in its 59 non-truncated responses. These results are consistent with personas acting as Model-Dependent behavioral-policy biases rather than universal quality interventions. We release raw completions, derived scores, analysis artifacts, a pre-registration document, and an execution gate log; end-to-end test-based rescoring requires an unreleased task harness.
