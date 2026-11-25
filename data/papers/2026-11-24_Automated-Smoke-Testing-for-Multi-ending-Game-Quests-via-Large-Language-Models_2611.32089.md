# Automated Smoke Testing for Multi-ending Game Quests via Large Language Models

- arXiv ID: `2611.32089v1`
- Authors: Jinyu Cai, Mingyue Zhang, Nianyu Li, Jinglue Xu, Tianshui Li, Jialong Li, Hitoshi Iba, Kenji Tei
- Published: 2026-11-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.32089v1) | [pdf](https://arxiv.org/pdf/2611.32089v1)

## Abstract

Modern game quests are increasingly trending toward high freedom and multiple endings, making their design and testing more complex. Smoke testing in games aims to rapidly validate quest functionality, but existing automated testing approaches face critical limitations when handling quests with branching narratives, and multiple possible endings. These challenges result in insufficient exploration of endings, redundant action sequences, and prohibitively high interaction costs. To address these challenges, we propose EndWeaver, an automated smoke testing framework specifically designed for multi-ending game tasks. EndWeaver leverages LLMs to interpret quest descriptions and game environments, generating high-level methods to guide global exploration, complemented by the generated primitive task sequences for fine-grained planning. By combining this multi-level planning structure with the dynamic construction of state-transition graphs, EndWeaver ensures comprehensive coverage of all possible endings and enables efficient testing. We evaluated EndWeaver on four game environments---Mini RPG, Overcooked Plus, Minecraft, and PySC2 against baseline methods. In all environments, EndWeaver achieved stable quest completion with high reliability, significantly outperforming the baselines. In terms of testing cost, EndWeaver required only a few thousand steps, while baseline methods required millions of steps, all while ensuring comprehensive coverage of all possible quest endings. Ablation studies further demonstrated the critical contributions of each framework component, validating the effectiveness and robustness of our approach.
