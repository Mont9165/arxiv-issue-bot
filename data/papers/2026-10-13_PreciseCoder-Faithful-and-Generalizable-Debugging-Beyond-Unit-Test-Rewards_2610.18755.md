# PreciseCoder: Faithful and Generalizable Debugging Beyond Unit-Test Rewards

- arXiv ID: `2610.18755v1`
- Authors: Yunkai Zhan, Miaosen Chai, Shangshang Wang, Jike Zhong, Yuqing Yang, Deqing Fu, Serina Chang, Wang Bill Zhu
- Published: 2026-10-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2610.18755v1) | [pdf](https://arxiv.org/pdf/2610.18755v1)

## Abstract

Reinforcement learning (RL) from unit tests is the common recipe for post-training code models, but a unit test only asks whether the final program passes. We analyze what this unit-test-only reward teaches a model during debugging and find that, while it raises pass rates, it also teaches the model to edit more and to hallucinate bugs in code that is already correct. We introduce PreciseCoder, a training algorithm that augments the unit-test reward with a signal for semantically verified, localized edits, which correlates with smaller edits and higher pass rates. On 4B, 9B, and 27B models, PreciseCoder reduces the average number of edit lines from 7-15to 3 at a pass rate on par with unit-test-only training. Trained only on single-line bugs, PreciseCoder can generalize to repository-level program repair, where it resolves more issues with smaller patches. Its precision also transfers from weaker to stronger models: given the reasoning trace of a 9B PreciseCoder model, frontier models such as GPT-5.6 Sol and Qwen3.8-Max gain 4.6-12.4 points in edit precision with no additional training. Linguistic analysis of the thinking traces shows that our reward encourages the model to reason about individual lines, name the buggy ones, and form consistent bug hypotheses.
