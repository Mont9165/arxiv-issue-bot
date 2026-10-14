# Evaluating Fuzz Testing for Reinforcement Learning Agents

- arXiv ID: `2607.24577v1`
- Authors: Zhibin Kang, Hanmo You, Dong Wang, Haiming Zheng, Junjie Chen
- Published: 2026-07-27
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.24577v1) | [pdf](https://arxiv.org/pdf/2607.24577v1)

## Abstract

Reinforcement Learning (RL) agents are increasingly deployed in safety-critical domains such as robotics, autonomous driving, and drone control, where unexpected behaviors may lead to severe real-world consequences. Fuzz testing has recently emerged as a promising method for exploring the vast state spaces of RL agents and exposing crashes. Although numerous RL fuzzing methods have been proposed, existing studies often differ in evaluation settings, baselines, and metrics, making it difficult to draw reliable conclusions about their relative effectiveness and practical usefulness. To address this gap, we present the first comprehensive empirical study that systematically evaluates RL fuzzing methods from four complementary perspectives: effectiveness, diversity, efficiency, and practical utility. We benchmark five state-of-the-art methods alongside random testing under unified configurations across three environments of increasing complexity (MountainCar, BipedalWalker, and CARLA), and further assess the downstream usefulness of detected crashes for agent robustness improvement and safety monitoring. Our results reveal several key insights. For instance,throughput-oriented methods like MDPFuzz demonstrate superior effectiveness and efficiency in crash discovery, while methods explicitly designed to encourage exploration like SeqDivFuzz excel at uncovering diverse crash behaviors. We also show that fuzzing-generated crashes can meaningfully improve agent robustness and enable accurate safety monitoring with strong cross-method generalization. Beyond these empirical findings, we distill actionable guidance for both researchers and practitioners, highlighting the benefits of combining complementary fuzzing strategies and adopting multi-level diversity analysis to achieve more comprehensive and practical RL testing.
