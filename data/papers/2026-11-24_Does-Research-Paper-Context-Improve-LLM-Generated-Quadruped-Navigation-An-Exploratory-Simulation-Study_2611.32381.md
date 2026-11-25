# Does Research-Paper Context Improve LLM-Generated Quadruped Navigation? An Exploratory Simulation Study

- arXiv ID: `2611.32381v1`
- Authors: Barnabas Juhasz, Rolf Pfister
- Published: 2026-11-24
- Primary category: `cs.RO`
- Categories: `cs.RO`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.32381v1) | [pdf](https://arxiv.org/pdf/2611.32381v1)

## Abstract

Large language models can write competent robot navigation code, but not only does the research on the topic advance, a model may also, due to the volume of findings, fail to recall relevant findings and apply them to the task at hand. In this work, we test whether providing particular research papers as context improves the LLM-written navigation code for the Go2 quadruped, with the LLM (Claude Opus 5) and locomotion policy frozen. Specifically, we compare the navigation controllers the LLM writes when provided with and without particular papers across three settings: behavior trees, navigators edited from a shared base, and controllers written from scratch. When a maze's shortest route is blocked mid-episode, 2 of 8 controllers written with the context of an incremental-replanning paper complete all four trips under Isaac Sim physics, against 7 of 8 without it (two-sided Fisher's exact test, p = 0.041). This difference appears only under physics: in an idealized kinematic simulator, the controllers written with and without the paper are indistinguishable. We hypothesize that an LLM provided research papers as context tends to overweight both their content and their goals -- in this case, the efficiency of incremental replanning -- negatively affecting the fulfillment of the main task and leading to less robust code.
