# Snyk VulnBench JS 1.0: Can LLMs Find the Same Bugs Twice?

- arXiv ID: `2606.15762v1`
- Authors: Liran Tal, Johannes Kloos, Arsenii Rudich, Stephen Thoemmes, Manoj Nair
- Published: 2026-06-14
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.15762v1) | [pdf](https://arxiv.org/pdf/2606.15762v1)

## Abstract

We ran 300 repeated vulnerability-finding scans to measure how repeatable agentic large language model (LLM) security review is on the same JavaScript code, prompt, and benchmark harness. The headline result is that LLM security findings were unevenly repeatable: reference-matched findings were stable, but extra model reports varied heavily from run to run. Across 250 model runs, 80 of 161 unique unmatched findings appeared in only one of five identical repetitions, while only 22 appeared in all five. By contrast, when Claude matched a Snyk Code reference finding, the behavior was much more stable: 134 of 158 unique reference-matched findings appeared in all five repetitions. The benchmark also shows complementarity. Models consistently found familiar, high-signal exploit shapes, and in one case surfaced a likely Snyk Code product gap. Snyk Code static application security testing (SAST) was deterministic and better at systematically enumerating repeated data-flow sinks. The results support combining agentic LLM review with deterministic SAST rather than treating either technique as a replacement for the other.
