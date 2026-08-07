# Beyond Execution: Static-Analysis Rewards and Hint-Conditioned Diffusion RL for Code Generation

- arXiv ID: `2605.17174v1`
- Authors: Shuyin Ouyang, Zhaozhi Qian, Faroq AL-Tam, Muhammad AL-Qurishi, Jie M. Zhang
- Published: 2026-05-16
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.17174v1) | [pdf](https://arxiv.org/pdf/2605.17174v1)

## Abstract

Reinforcement Learning (RL) is an important paradigm for aligning Diffusion Language Models (DLMs) toward functional correctness in code generation. However, these models often encounter a ``capability cliff'' on complex tasks, where execution-based semantic rewards become too low to provide a viable learning signal. In this paper, we present a systematic empirical study of RL post-training for diffusion-based code generation along three axes: reward design, hint-conditioned sampling, and task difficulty. We investigate the effectiveness of execution-free rewards as alternatives to traditional unit-test execution, the role of training-time hint-conditioned diffusion sampling in mitigating exploration bottlenecks, and the impact of these design choices varies across tasks with different difficulty levels. Across HumanEval, MBPP, and LiveCodeBench, we find that static checking is the strongest overall standalone execution-free reward in our setting, especially improving DiffuCoder from 53.9 to 67.1 on HumanEval and from 14.9 to 15.5 on LiveCodeBench while reducing rollout time by 9.4\%. We further find that moderate AST-based hinting is most useful on harder benchmarks, while the best reward design depends strongly on task difficulty: similarity-based rewards are more effective on easier subsets, whereas static checking is more reliable on harder subsets where execution rewards are low. These findings suggest that reward design and training guidance substantially affect diffusion RL performance in our evaluated code-generation setting.
