# Failure-Based Testing for Deep Reinforcement Learning Agents

- arXiv ID: `2606.31372v1`
- Authors: Weibin Lin, Jiangtao Meng, Zheng Zheng
- Published: 2026-06-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.31372v1) | [pdf](https://arxiv.org/pdf/2606.31372v1)

## Abstract

Deep Reinforcement Learning (DRL) agents have been widely adopted across diverse domains to address challenging decision-making problems, such as autonomous driving and robotic control. Given that many of these applications are safety- and security-critical, rigorous testing of DRL agents is indispensable. Existing testing methods are typically guided by reward signals to detect failures. However, for well-trained agents, whose performance approaches optimal levels in standard operating conditions, reward signals remain generally high, making current methods ineffective at uncovering critical failures.
  To address these challenges, we propose a novel failure-based method that leverages task-induced failure insights to enhance failure detection capability while reducing the number of tests required. Since DRL agents are inherently designed with human-defined tasks, they provide valuable cues about task difficulty. Intuitively, a DRL agent is more likely to fail when confronted with a more difficult task; therefore, PRT prioritizes these tasks. Building on this foundation, we propose Prior Random Testing, a black-box failure-based testing method that enables targeted prioritization while preserving the diversity of generated test cases. Guided by task-induced failure insights, PRT prioritizes failure-prone regions of the input domain, thereby facilitating efficient failure detection.
  PRT is evaluated on four widely used benchmarks and compared with different state-of-the-art methods including fuzzing, search-based and generative-based methods. PRT ranks among the top performers in terms of both the cost of finding the first failure and the diversity of test cases. Notably, compared to random testing, PRT achieves better diversity and reduces the testing cost by over 50%.
