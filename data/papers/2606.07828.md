# Jas: AI-Paired Engineering as a Revival of N-Version Programming

- arXiv ID: `2606.07828v1`
- Authors: Jason Hickey
- Published: 2026-06-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.07828v1) | [pdf](https://arxiv.org/pdf/2606.07828v1)

## Abstract

I report a case study in AI-paired software engineering: five working ports of a vector illustration application across Rust, Swift, OCaml, Python, and browser-based platforms, built by a single developer in approximately 120 evening hours. The methodology pairs AI-assisted implementation with two safeguards -- a precise executable YAML specification serving as the single source of truth, and parallel implementations functioning as a built-in differential-testing layer. The five ports share a 23{,}000-line specification; per-port native code ranges from 0 to roughly 95{,}000 lines, reflecting the specification's escape hatch. I argue that AI-paired engineering, conditional on these two safeguards, makes feasible scope of work that conventionally requires multiple developer-years, and frame the methodology as a revival of N-version programming, a 1980s approach abandoned on cost grounds that AI changes. The paper reports concrete artifacts and honest limitations of the single-developer case study.
