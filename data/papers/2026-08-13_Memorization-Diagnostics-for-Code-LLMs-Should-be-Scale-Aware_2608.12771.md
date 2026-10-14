# Memorization Diagnostics for Code LLMs Should be Scale-Aware

- arXiv ID: `2608.12771v1`
- Authors: Prateek Kumar Rajput, Abdoul Aziz Bonkoungou, Alberick Euraste Djiré, Xunzhu Tang, Yewei Song, Iyiola Emmanuel Olatunji, El Hacen Diallo, Jacques Klein, Tegawendé F. Bissyandé
- Published: 2026-08-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.12771v1) | [pdf](https://arxiv.org/pdf/2608.12771v1)

## Abstract

The extent to which large language models for code rely on memorization over genuine understanding remains highly debated. While current literature frequently reports widespread memorization, evaluating the underlying probing techniques across dense architectures reveals a severe breakdown in their utility at scale. Traditional encoder-style probes using perturbations such as synonym fuzzing or dead-code insertion struggle to expose memorization in scaled models, even on known-contaminated benchmarks, and decoder-style probes that rely on log probabilities show similar performance degradation. The specific mode of failure for these probes, particularly why such techniques disrupt smaller models but fail to impact larger ones, motivates us to untangle representation load from memorization rather than treating them as a single phenomenon. By applying invertible mathematical transforms to numeric problems, we isolate these two factors and reveal that scaled encoders successfully absorb substantial representation load while still converging on the correct family of solutions. In practical software engineering, this ability to adapt to varying surface forms is what truly matters for usability and generalizability in LLM and agentic applications. Whether a specific solution was seen during training becomes a much less pressing question because although memorization inflates scores on contaminated benchmarks, factoring out representation load makes it debatable how much we should truly care if a functional answer was originally memorized. Future evaluations must therefore be built around separating these phenomena rather than relying on methodologies that quietly entangle them.
