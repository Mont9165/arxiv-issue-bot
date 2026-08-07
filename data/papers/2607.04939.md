# Teaching LLMs a Low-Resource Language: Enhancing Code Completion in Pharo

- arXiv ID: `2607.04939v1`
- Authors: Kilian Kier, Alessandro Giagnorio, Omar AbedelKader, Oleksandr Zaitsev, Robert Peharz, Romain Robbes, Gabriele Bavota, Stéphane Ducasse
- Published: 2026-07-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.04939v1) | [pdf](https://arxiv.org/pdf/2607.04939v1)

## Abstract

Large Language Models (LLMs) unlocked new possibilities in automated code writing, becoming the backbone of most code completion tools. While LLMs excel in mainstream languages, they often lack support for the so-called low-resource languages where training data is scarce. As a result, these languages lag behind in the quality of code completion tooling available to their communities. A concrete example is Pharo, a Smalltalk-inspired language whose IDE currently offers only single-token completion. In this work, we report on our experience bringing LLM-based code completion to Pharo. First, we describe an end-to-end pipeline that combines Pharo-specific data curation, continued pre-training and fine-tuning of open code LLMs. Second, we introduce a set of Pharo code completion benchmarks designed to evaluate whether models (i) learn Pharo's syntax and (ii) accurately complete masked Pharo code from real-world GitHub repositories. Third, we show empirically that Pharo-specialized models substantially outperform their original base checkpoints and also exceed the accuracy of substantially larger code LLMs on Pharo completion. Overall, our case study demonstrates the feasibility of bringing strong LLM-based code completion to low-resource programming languages, with models small enough to provide ``real-time'' in-IDE support.
