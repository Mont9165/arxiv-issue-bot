# Agentic Synthesis against Counterexample-Supplemented Sketches

- arXiv ID: `2607.15854v1`
- Authors: Muness Castle, Eric Rubeck
- Published: 2026-07-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.15854v1) | [pdf](https://arxiv.org/pdf/2607.15854v1)

## Abstract

Coding agents can fix a failing example without preserving the domain rule that made it fail, so later generations can repeat the same plausible mistake. We present agentic synthesis against counterexample-supplemented sketches, a repository-native method for systems whose governing policy is discovered during implementation. A human starts with a partial, code-shaped sketch, and a coding agent generates the first implementation. When a concrete failure exposes missing or mistaken policy, an operator explicitly approves the corrected behavior and rule. The agent then revises the sketch and repairs or regenerates code and prompt surfaces for that one counterexample. The full archive preserves provenance; a selected regression set gates each revision before the next candidate is revealed; and periodic clean regeneration tests whether the evolved sketch, rather than prompt history or accumulated examples, carries the learned policy.
  We demonstrate the method with CatSynth, a synthetic browser application and captured coding-agent experiment. In one open-world run with GPT-5.4-mini, 8 of 14 frozen candidate cases became counterexamples. The rebuild controls inherited that promotion schedule, and all three paths passed the 8 accepted cases. Rebuilding from the evolved sketch passed 19 of 21 withheld cases, compared with 15 of 21 when rebuilding from the initial sketch and replaying all accepted examples. Retaining code across counterexamples required 9 Developer calls and 719 lines of cumulative artifact churn, versus 15 calls and 2,394 lines for replay-all, and passed 18 of 21 withheld cases. These results provide inspectable evidence that the evolved sketch carried reviewed policy and that retaining code reduced rework in this run; with one model and one reveal order, they do not establish general superiority or correctness beyond the encoded checks.
