# ContractBench: Can LLM Agents Preserve Observation Contracts?

- arXiv ID: `2605.17281v1`
- Authors: Jicheng Wang, Yifeng He, Zili Wang, Hanwen Xing, Arkaprava De, Hao Chen
- Published: 2026-05-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.17281v1) | [pdf](https://arxiv.org/pdf/2605.17281v1)

## Abstract

Tool-augmented LLM agents call APIs whose intermediate outputs, such as presigned URLs, session tokens, and OAuth state parameters, are observation contracts: artifacts whose later use is constrained by the external system that produced them. We show that observation contract compliance (preserving the temporal validity and byte-level integrity) is an emergent, regression-prone capability: it is neither guaranteed by general tool-use ability nor consistently improved by larger or newer models. To measure this, we introduce ContractBench, a benchmark of 33 dual-axis tasks that probe two orthogonal failure modes no existing benchmark evaluates: validity failures (using an artifact after expiry) and integrity failures (corrupting an artifact's bytes through the observation-to-action pipeline). Our evaluation is deterministic and programmatic, with a virtual clock controlling time and SHA-256 hashes verifying byte integrity. We assign each outcome a failure label drawn from real-world API specifications. We evaluate 38 models and report four findings: (i) no evaluated model clears 80%, with Claude-Opus-4.6 leading at 77.8%, revealing that current frontier models still fail to comply with observation contracts; (ii) a sharp within-family capability cliff in Qwen 3.5 between 4B (0%) and 9B (56.6%), smoothing to 70.7% at 397B-A17B: what emerges across the cliff is mid-trajectory restraint, not tool-call competence; (iii) non-monotonic scaling across the GPT-5 family: agentic post-training can erode compliance through sycophancy-driven regression; (iv) our failure taxonomy works as an actionable in-context reward signal, yielding +7.1 pp on 42 paired GPT-5.1 failures.
