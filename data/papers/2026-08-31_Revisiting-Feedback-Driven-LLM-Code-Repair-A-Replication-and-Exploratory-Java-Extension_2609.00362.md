# Revisiting Feedback-Driven LLM Code Repair: A Replication and Exploratory Java Extension

- arXiv ID: `2609.00362v1`
- Authors: Louis Lalonde, Wassim Keddache, Thomas Perron Touchette, Leuson Da Silva, Foutse Khomh
- Published: 2026-08-31
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.00362v1) | [pdf](https://arxiv.org/pdf/2609.00362v1)

## Abstract

Since the advent of Large Language Models (LLMs), practitioners have increasingly leveraged them to support their software engineering tasks, including automated code repair, showing promising results. Yet, concerns regarding reproducibility and generalizability remain largely unexplored. To further evaluate these concerns and associated impacts, we partially reproduce and conduct an exploratory Java extension of the FeedbackEval benchmark [1], which evaluates how LLMs leverage different feedback types for Python code repair. First, we partially replicate the original study on 394 repair tasks using GPT-4o and Claude 3.5 Sonnet, reproducing and observing the main qualitative trends reported in the original work. Second, we conduct an exploratory Java extension by constructing 100 erroneous repair instances from 50 Java tasks and evaluating feedback effectiveness. Our results show that previous conclusions from Python may be sensitive to benchmark construction, feedback representation, and tooling ecosystem, motivating more controlled multilingual benchmarks. Specifically, while test feedback remains the strongest feedback type in our Python replication, the same ranking is not observed in our Java extension, as simple and JUnit-based test feedback do not differ significantly. We hypothesize that differences in feedback informativeness and tooling ecosystems, such as the verbosity of test frameworks, may partly explain such a difference. Finally, lighter prompts reduce cost without significant differences in repair effectiveness. Overall, our findings confirm key trends under a partially controlled replication and highlight the need for more rigorous multilingual evaluation and careful feedback design in LLMbased repair systems.
