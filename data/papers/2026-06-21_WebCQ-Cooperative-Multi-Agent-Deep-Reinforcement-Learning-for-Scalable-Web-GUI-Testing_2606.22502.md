# WebCQ: Cooperative Multi-Agent Deep Reinforcement Learning for Scalable Web GUI Testing

- arXiv ID: `2606.22502v1`
- Authors: Yujia Fan, Sinan Wang, Zebang Fei, Yao Qin, Huaxuan Li, Yepang Liu
- Published: 2026-06-21
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.22502v1) | [pdf](https://arxiv.org/pdf/2606.22502v1)

## Abstract

Multi-agent reinforcement learning (MARL)-based techniques have shown promise for GUI testing. However, as the complexity of modern GUI software increases, existing MARL-based approaches (e.g., MARG and Fastbot) struggle to scale due to the inherent limitations of their underlying tabular reinforcement learning algorithms. This limits their applicability to large-scale commercial GUI software, especially web applications with vast state spaces and many interactive elements. To fill this gap, we propose WebCQ, a novel MARL-based approach for scalable web GUI testing. WebCQ incorporates QTRAN for multi-agent coordination and a lightweight synchronization mechanism, allowing it to work under asynchronous web testing scenarios. It extracts semantic and exploration features for each UI event to form an action vector. This vector is concatenated with the current state vector and fed into the policy network, enabling DQN-based decision making within a dynamic action space. We evaluated WebCQ on eight large-scale commercial websites. Under the same time budget and agent count, WebCQ explored 33.3% more states and executed 42.2% more unique actions than MARG, while triggering more failures on six of the eight websites under test. It also demonstrated strong scalability, maintaining higher action throughput during 20-hour experiments, and achieving greater performance improvements as the number of agents increased. These results show that WebCQovercomes key limitations of existing MARL-based approaches, providing a scalable and effective solution for enhancing modern web GUI testing.
