# VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably

- arXiv ID: `2611.03575v1`
- Authors: Wei-Lin Chen, Zhepei Wei, Xinyu Zhu, Yu-Min Tseng, Tzu-Han Lin, Yu Meng
- Published: 2026-11-02
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.03575v1) | [pdf](https://arxiv.org/pdf/2611.03575v1)

## Abstract

Large language model (LLM) coding agents increasingly operate with shell access, allowing them to write scripts, move files, alter permissions, and modify system configurations. However, an agent may achieve a user's goal while causing unintended harm, such as deleting unrelated files, weakening access controls, or corrupting data, in response to benign inputs without explicit jailbreaking. This failure mode is particularly important because apparent task success may reassure users that an agent behaved correctly, causing harmful side effects to go unnoticed. We call this harmful success: the agent successfully completes the intended benign task while simultaneously causing unintended harm. Despite its importance, harmful success is difficult to measure because conventional task-success metrics overlook harmful behaviors, while existing safety evaluations are often designed solely to assess harmful outcomes. We introduce VeriHarm, an automatic framework for constructing programmatically verifiable benchmarks that directly measure harmful success. VeriHarm minimally perturbs coding tasks to elicit unintended harmful behavior while maintaining the benignity of the task and preserving the original task objective. It then synthesizes executable harm tests that, together with the original task-correctness tests, evaluate both task accuracy and harmful outcomes. Frontier agents, including GPT-5.6-Sol and Claude-Opus-5, achieve an average task accuracy of 95% on our curated VeriHarm-Bench, yet still struggle to complete tasks safely: their safe success rate, the fraction of tasks completed successfully without triggering the designated harm, averages only 37%. These results suggest that successful task completion can frequently coexist with unintended harm, and that task-success metrics alone may substantially understate the potential safety risks of coding agents.
