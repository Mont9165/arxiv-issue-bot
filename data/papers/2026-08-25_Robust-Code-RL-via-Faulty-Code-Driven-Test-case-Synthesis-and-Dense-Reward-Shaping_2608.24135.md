# Robust Code RL via Faulty-Code-Driven Test case Synthesis and Dense Reward Shaping

- arXiv ID: `2608.24135v1`
- Authors: Yiwen Zhang, Xiaodong Yan, Zhenyu Huang, Deng Zhao, Liang Jiang, Qing Cui, Zujie Wen, Zhiqiang Zhang, Jun Zhou
- Published: 2026-08-25
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.24135v1) | [pdf](https://arxiv.org/pdf/2608.24135v1)

## Abstract

Reinforcement learning from verifiable rewards (RLVR) has emerged as a pivotal technique for enhancing the code generation capabilities of Large Language Models (LLMs). However, the efficacy of RLVR in coding implementations is fundamentally limited by the comprehensiveness of test cases, because insufficient test coverage in code validation often causes false positives, further leading to reward hacking and policy degradation. To mitigate the reward bias stemming from the suboptimal quality of current automated generation methods, we propose the RobustTests framework, which introduces a faulty-code-driven test case synthesis strategy that leverages "near correct" faulty codes to guide the model in precisely capturing latent logical discrepancies and further integrates validator agents with behavioral feature clustering to facilitate the granular filtering of invalid and redundant test cases. To address false negatives caused by inherent hallucination noise in synthetic test cases, RobustTests also incorporates a stepwise dense reward function based on pass rates, bolstering training robustness through fine-grained feedback. By employing this pipeline, we construct a high-quality dataset that augmented the test cases in CodeContests, encompassing a broader spectrum of faulty code scenarios and significantly enhances diagnostic utility. Experimental results demonstrate that, by leveraging a moderately challenging subset of problems from CodeContests for training, RL fine-tuning of Qwen3-32B via RobustTests achieves an absolute 3% performance gain on the LiveCodeBench benchmark compared to baseline methods, confirming the effectiveness of the RobustTests framework in advancing the code generation proficiency of LLMs.
