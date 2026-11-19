# Reducing Inference Cost of Coding Agents with Timeout Cascades

- arXiv ID: `2611.24324v1`
- Authors: Boxi Zhou, German Sviridov, Dmitrii Ustiugov, Haris Javaid
- Published: 2026-11-18
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.24324v1) | [pdf](https://arxiv.org/pdf/2611.24324v1)

## Abstract

AI coding agents have become one of the most popular applications of large language models. Yet, agentic AI comes at the cost of a tremendous amount of GPU compute resources, which limits its profitability and its viability at scale. In this paper, we investigate whether smaller, cheaper models can cut this cost without sacrificing accuracy.
  We evaluate 36 popular large and small open-weight models released since 2024 on a software engineering benchmark, and find that recent small models are closing the accuracy gap compared to their large counterparts. We investigate the structure of this gap and find that the gap is highly concentrated around hard tasks that small language models fail to solve while achieving remarkably good accuracy for easy and medium complexity tasks. Following this observation, we show that by utilizing a hybrid inference strategy that tries a small model first and escalates to a large one only when needed, we can achieve up to 33% reduction in total GPU-hour costs and 16.4% on all tasks from SWE-bench Verified, without sacrificing accuracy. Strikingly, this simple cascade nearly matches an oracle-style task router, highlighting a practical path for deploying cost-aware coding agents in production without complex learned task routers and with minimal engineering complexity.
