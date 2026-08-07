# Vul4Py: Benchmarking Automated Vulnerability Repair in Python with Paired Exploit and Functional Oracles

- arXiv ID: `2608.00692v1`
- Authors: Tan Bui, Ting Zhang, Ferdian Thung, Yunpeng Xiong, Penghao Jiang, Xin Zhou, David Lo
- Published: 2026-08-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.00692v1) | [pdf](https://arxiv.org/pdf/2608.00692v1)

## Abstract

Automated Vulnerability Repair (AVR) has advanced rapidly across program analysis, machine learning, and Large Language Models (LLMs), but a verifiable, head-to-head comparison of AVR approaches on Python is still missing. Python underpins critical web, data, and machine-learning infrastructure, yet existing Python benchmarks accept a patch on the strength of a proof-of-concept exploit alone, or apply a functional test only on the subset of entries whose upstream project happens to ship one. Both therefore miss functional regressions, in which a patch defeats the exploit but breaks unrelated behavior. We present Vul4Py, a Python AVR benchmark in which every entry carries a paired oracle: an exploit oracle that must fail on the vulnerable revision and pass on the fixed one, together with a project-native pytest functional oracle that must pass on both. Vul4Py comprises 100 real vulnerabilities from 60 open-source projects, spanning 60 distinct CWEs and the years 2017 to 2025, each packaged with a pinned, reproducible per-instance environment. Using Vul4Py, we compare six approaches in three categories: a specialized vulnerability repair tool, directly prompted LLMs, and software engineering agents. The agents dominate: OpenHands repairs 41 of 100 vulnerabilities, against 4 for the strongest directly prompted LLM and 2 for the specialized tool, despite all three sharing the same backbone model. The paired oracle is what makes these counts trustworthy: it rejects 15 of the 119 patches that an exploit-only oracle would accept, and 98 of the 104 patches it admits are manually confirmed to be semantically equivalent to the developer's patches
