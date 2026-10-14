# What Stops a Small Language Model From Driving a Database Agent

- arXiv ID: `2609.21341v1`
- Authors: Cevheri Bozoglan, Yusuf Gundogdu, Abdullah Kaya, Koray Sirin
- Published: 2026-09-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.21341v1) | [pdf](https://arxiv.org/pdf/2609.21341v1)

## Abstract

Small open-weight language models are assumed to fail at agentic database work because they lack the reasoning capacity for it. We test that against a production system. Over eleven days we drove the agent mode of an open-source SQL client with 39 open-weight models served locally and one hosted control, across six task surfaces: 8,199 runs, 110,711 ledger events, 14,008 refused tool calls. Of the 2,100 model-attributed agent-mode losses, 1,590, or 75.7%, came from runs that had invoked at least one tool. That majority is what survives resampling models rather than runs: it holds in 99.7% of clustered resamples and in 15 of the 22 models with at least twenty losses. Within it, transport, a run that used the tools and never got a deliverable through, is the largest class at 36.2% and capability, a run that invoked no tool at all, the smallest at 17.3%; we report that ordering as a property of this corpus rather than a general finding, since clustered by model it holds in only 74.5% of resamples. Transport failures decompose into a few mechanical argument shapes. Production ledgers record refusal codes and never the model's arguments, so these were invisible for ten days; capturing them exposed five server defects, one of which demanded a field on one tool, forbade it on the sibling that composed it, then failed the run for its absence. Five server changes, touching no model, prompt or sampling setting, moved six models by 6 to 21 cells out of 30. We also report a confound we believe affects published local-model benchmarks, ours included: with no context cap, one 7.1 GB model was admitted at its full 262,144-token window and held 51 GB on a 64 GB machine, producing runs indistinguishable in any ordinary log from a model timing out. The corpus, the scorer and a verifier that regenerates every figure are released.
