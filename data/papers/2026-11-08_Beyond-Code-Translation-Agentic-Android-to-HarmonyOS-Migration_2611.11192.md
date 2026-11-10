# Beyond Code Translation: Agentic Android-to-HarmonyOS Migration

- arXiv ID: `2611.11192v1`
- Authors: Yinghang Ma, Wuyang Dai, Song Wang, Filipe Cogo, Zhen Ming,  Jiang
- Published: 2026-11-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.11192v1) | [pdf](https://arxiv.org/pdf/2611.11192v1)

## Abstract

Migrating Android applications to HarmonyOS is an important yet challenging software engineering task. Existing large language model (LLM)-based migration approaches primarily translate code at the method or file level, overlooking project-wide dependencies and workflow coordination. Moreover, ArkTS, the primary language for HarmonyOS, is relatively low-resource, and migrated applications often lack sufficient tests for reliable verification, making end-to-end migration error-prone. We present A2HTrans, an agentic framework for end-to-end Android-to-HarmonyOS application migration. Rather than performing isolated code translation, A2HTrans decomposes applications into functionality-aware migration tasks, prioritizes them through dependency analysis, and orchestrates translation, validation, and iterative repair within a unified execution workflow. To improve migration reliability, A2HTrans employs a tool-augmented verification strategy that combines compiler-based syntax checking with LLM-based semantic validation and automated repair. We evaluate A2HTrans on 14 Android applications spanning diverse sizes and domains using Claude-Sonnet-4.6 as the underlying migration model. Compared with Claude Code, A2HTrans preserves 8.3% more functional completeness, improves behavioral correctness by 8.0%, and reduces migration time by 28.8%. These results demonstrate that structured agentic execution substantially improves the reliability and efficiency of project-level cross-platform software migration.
