# Harness Engineering for Software Engineering via Modular Executable Dev-Primitives

- arXiv ID: `2610.07832v1`
- Authors: Haibo Jin, Xinjie Li, Peng Kuang, Haohan Wang
- Published: 2026-10-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`, `cs.MA`
- Links: [abs](http://arxiv.org/abs/2610.07832v1) | [pdf](https://arxiv.org/pdf/2610.07832v1)

## Abstract

Large language models (LLMs) equipped with terminal access have demonstrated strong capabilities in automating software engineering tasks. However, existing agents remain brittle on long-horizon workflows, where they must repeatedly reconstruct program state scattered across source files, configurations, tests, dependencies, and runtime behavior, leading to increasingly long interaction histories, context explosion, and semantic drift. Large repositories further complicate the identification of task-relevant components. To address these challenges, we introduce \textbf{Dev-Primitives} (\emph{Development Primitives}), a modular and executable abstraction that transforms repository components from passive software artifacts into active participants in software engineering. Each Dev-Primitive pairs a repository artifact with a resident LLM, which gives the artifact an agent-native interface grounded in its own implementation and dependencies, enabling natural-language reasoning, inter-component communication, and localized self-modification. Building on Dev-Primitives, we propose \textbf{HERMES}, a Harness Engineering framework for software engineeRing via Modular Executable Dev-PrimitiveS, which instantiates these primitives at repository scale through a dependency-aware dynamic activation mechanism and a bug diagnosis mechanism that maps execution evidence back to the components that must be revised. Extensive experiments on four software engineering benchmarks demonstrate that HERMES outperforms matched baseline harnesses by 12.4\% on average. Moreover, when paired with strong activation and diagnosis models, HERMES, even with Qwen3-8B Dev-Primitives, remains within 4.5\% of the homogeneous GPT-5.6 Sol configuration across all four benchmarks, while reducing inference cost by 26.2\% on Terminal-Bench 4.0, highlighting the importance of harness design in software engineering agents.
