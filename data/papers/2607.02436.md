# Reasoning effort, not tool access, buys first-try reliability in agentic code generation: an observational study

- arXiv ID: `2607.02436v1`
- Authors: Achint Mehta
- Published: 2026-07-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.02436v1) | [pdf](https://arxiv.org/pdf/2607.02436v1)

## Abstract

Agentic coding assistants are increasingly given extra capabilities, such as browser based testing tools and design oriented system prompts, on the assumption that more capability yields better software. This study tested that assumption directly. Ninety independent agent runs built the same application, a real time retrospective board, from one detailed specification, each scored on a fixed 14 criterion functional rubric (42 point maximum) and a visual quality review. The runs spanned several model generations, two agent harnesses, two reasoning effort levels, a testing tool, and two design oriented prompts. Capability tier dominated: frontier models clustered near the ceiling while a low cost local model fell to 24 to 37 points. A criterion level analysis revealed what run totals conceal. Container deployment was the dominant defect, failing first try in 44 percent of runs, with its failure rate shifting sharply across model generations while mean totals moved less than a point. The testing tool raised cost by 42 to 68 percent without improving functional score or reliability, even on interface visible criteria. Raising reasoning effort from High to xHigh lifted first try perfect runs from 28 percent to 89 percent and cut corrective prompts about five fold, for 9 to 29 percent more cost. A design oriented prompt raised visual quality, 4.5 versus 3.0 on a 5 point scale, without lifting function, and a one paragraph paraphrase of its directive reproduced the entire lift. The practical lesson is to match the fix to the failure: most first run failures came from weak reasoning, which a stronger model or more effort prevents, not from visible flaws a checking tool would catch.
