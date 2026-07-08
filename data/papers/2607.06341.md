# Harnessing Code Agents for Automatic Software Verification

- arXiv ID: `2607.06341v1`
- Authors: Shuangxiang Kan, Shuanglong Kan, Sebastian Ertel
- Published: 2026-07-07
- Primary category: `cs.FL`
- Categories: `cs.FL`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.06341v1) | [pdf](https://arxiv.org/pdf/2607.06341v1)

## Abstract

Formal verification offers the strongest guarantee of software correctness, but it does not scale: the proofs demanded by interactive theorem provers such as Coq require enormous expert effort. Large language models (LLMs) promise to generate these proofs automatically, yet existing approaches wire a fixed, human-designed proof strategy into the system and constrain the model to follow it (retrieving premises and predicting tactics one step at a time, or splitting goals by divide-and-conquer), and still prove only a fraction of their target theorems.
  We show that imposing such a strategy is unnecessary and limiting. Handing the whole lemma to a general LLM code agent (for example, Claude Code), free to choose its own approach, and wrapping it in a verification harness is both simpler and more effective, achieving full coverage: every targeted lemma proved, with no failures and no Coq expert intervention. The agent writes the proofs under feedback and hard constraints from the harness that keep each one sound (accepted only when the prover's kernel closes it), complete (no obligation left unproved or silently dropped), and terminating (no divergent tactics).
  We evaluate this harness plus code agent along three dimensions. (1) Core logic: on Iris, the state-of-the-art separation logic for concurrent and memory-manipulating programs, Aria proves all 4,257 lemmas of the four core modules and the 217 lemmas verifying Rust's standard libraries built on it, fully automatically. (2) Comparison with prior LLM provers: on reglang, where prior provers manage barely one in eight, Aria proves all 318. (3) Generality: on iris-lean, the unfinished Lean 4 port of Iris, it proves 72 not-yet-ported lemmas, showing the approach is not specific to Coq. A state-of-the-art model (Claude Opus 4.7) can write proofs for verified software development fully and automatically.
