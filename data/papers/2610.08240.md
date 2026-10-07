# Newer and Bigger, but Safer? A Longitudinal Study of the Functionality-Security Gap in LLM-Generated Code

- arXiv ID: `2610.08240v1`
- Authors: Thiago Santos de Moura, Fynn Matuschek, Flavio Toffalini, Yannic Noller
- Published: 2026-10-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2610.08240v1) | [pdf](https://arxiv.org/pdf/2610.08240v1)

## Abstract

Large Language Models (LLMs) are widely used to generate code. Although their functional plausibility keeps improving, the generated code often contains security vulnerabilities. The functionality-security gap captures code that passes functional tests but fails security tests. A recent longitudinal study of three model families concluded that LLMs become smarter but not safer, with the only considered open-weight family stagnating. Whether this holds for other (open-weight) families and particularly for compact models remains open. We present a longitudinal study of the gap across 32 LLMs from seven model families (five open-weight), covering three successive releases per family in flagship and compact variants. Using CWEval with 119 tasks in five programming languages and 31 CWEs, we compare trajectories across families, model sizes, and languages. Newer models do become safer in absolute terms, although no family closes the gap. Unlike prior work, we find that openness does not separate the families: every considered open-weight family narrows the gap significantly, while Gemini 3.1 Pro keeps a gap as wide as the one reported for Llama. Compact models usually produce less secure code than their flagship counterparts, with notable exceptions (e.g., Gemini 3.7 Flash). At the CWE level, we confirm persistent weaknesses such as log injection (CWE-117) and HTTP response splitting (CWE-113) and regressions in the newest proprietary models on memory and integer weaknesses, and show that the same CWE carries very different risk across languages. From these results, we derive implications for LLM vendors, researchers, and developers. In particular, developers should assume neither that upgrades improve security nor that proprietary models are more secure; they should rerun security checks after each model change and provide secure APIs in the model's context.
