# SWE-DeceptionBench: Benchmarking Deceptive Behaviors of LLMs Across the Software Development Lifecycle

- arXiv ID: `2610.13626v1`
- Authors: Xiting Liu, Lin Yang, Yitong Zhang, Jia Li, Shi-Min Hu
- Published: 2026-10-09
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.13626v1) | [pdf](https://arxiv.org/pdf/2610.13626v1)

## Abstract

Large Language Models (LLMs) are increasingly used throughout the software development lifecycle. This growing reliance on LLMs raises concerns about their trustworthiness, with deception posing a particularly important risk. Deceptive behavior takes the form of misleading responses or assistance in fabricating, concealing, or distorting information. To study this behavior, we introduce SWE-DeceptionBench, a benchmark for evaluating LLM deception in software engineering. The benchmark covers six lifecycle stages and two deception triggers: Active Deception, where models recognize infeasible or conflicting requirements but still present them as achievable, and Passive Deception, where models help fulfill explicit user requests to mislead others. We further introduce Neutral, Reward, and Pressure conditions to study the effect of external inducements, resulting in 720 test instances in Chinese and English. Evaluating seven mainstream LLMs, we find substantial deception even under the Neutral condition, with aggregate rates of 49.88% for Active Deception and 64.29% for Passive Deception. Deception rates vary across lifecycle stages, and external inducements affect Active and Passive Deception to different extents. We also evaluate lightweight defenses, finding that guard models miss many deceptive requests, and Self-Reminder reduces but does not eliminate deceptive responses. These findings highlight the need for more effective deception detection and mitigation methods to support trustworthy LLM-based software engineering.
