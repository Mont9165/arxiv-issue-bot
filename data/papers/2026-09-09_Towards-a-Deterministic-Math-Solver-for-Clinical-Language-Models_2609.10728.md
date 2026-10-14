# Towards a Deterministic Math Solver for Clinical Language Models

- arXiv ID: `2609.10728v1`
- Authors: Felipe Ocampo Osorio, Sebastián Andrés Cajas Ordoñez, Maximin Lange, Rafi Al Attrach, Sahil Kapadia, Zakaria Laouabdia Sellami, Angelo Antonio Talio, Leo Anthony Celi
- Published: 2026-09-09
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.10728v1) | [pdf](https://arxiv.org/pdf/2609.10728v1)

## Abstract

Large language models are unreliable at arithmetic, which is a problem for clinical calculators where a single numerical error changes the recommendation. The standard response is to hardcode each calculator as a validated function, one at a time. We test an alternative: the model does not calculate. Instead, it writes case-specific Python that a restricted local executor runs as a deterministic solver, and the model's task reduces to deciding how to use it. We evaluate this Program-Solve interface on MedCalc-Bench Verified (1,100 cases, 55 calculators) against direct model arithmetic and a hand-written 22-calculator library, using Qwen2.5-7B and Qwen2.5-32B-AWQ, after auditing the benchmark's formulas against current clinical guidelines and flagging 16 of 55 with version, use or coefficient concerns. With formulas and gold variables supplied and both routes reading the whole note, handing off to the solver is not a reliable advantage at 7B (75.31% against 72.02%, a paired +3.29 points with a 95% calculator-cluster interval of [-3.49, 10.38]) but is one at 32B (90.53% against 83.47%, +7.05 [0.47, 14.60], clear of zero). The hand-written library is exact on its 440 supported cases but abstains elsewhere (40.0% overall). Adding an executor thus helps some open-weight models more than others even under matched formula, variable and note access, and is not a substitute for verified formulas or reliable variable extraction either way.
