# SmellBench: Evaluating LLM Agents on Architectural Code Smell Repair

- arXiv ID: `2605.07001v1`
- Authors: Ion George Dinu, Marian Cristian Mihăescu, Traian Rebedea
- Published: 2026-05-07
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2605.07001v1) | [pdf](https://arxiv.org/pdf/2605.07001v1)

## Abstract

Architectural code smells erode software maintainability and are costly to repair manually, yet unlike localized bugs, they require cross-module reasoning about design intent that challenges both developers and automated tools. While large language model agents excel at bug fixing and code-level refactoring, their ability to repair architectural code smells remains unexplored. We present the first empirical evaluation of LLM agents on architectural code smell repair. We contribute SmellBench, a task orchestration framework that incorporates smell-type-specific optimized prompts and supports iterative multi-step execution, together with a scoring methodology that separately evaluates repair effectiveness, false positive identification, and net codebase impact. We evaluate 11 agent configurations from four model families (GPT, Claude, Gemini, Mistral) on 65 hard-severity architectural smells detected by PyExamine in the Python project scikit-learn, validated against expert judgments. Expert validation reveals that 63.1% of detected smells are false positives, while the best agent achieves a 47.7% resolution rate. Agents identify false positives with up to $κ= 0.94$ expert agreement, but repair aggressiveness and net codebase quality are inversely related: the most aggressive agent introduces 140 new smells. These findings expose a gap between current LLM capabilities in localized code transformations and the architectural understanding needed for cross-module refactoring. SmellBench provides reusable infrastructure for tracking progress on this underexplored dimension of automated software engineering. We release our code and data at https://doi.org/10.5281/zenodo.19247588.
