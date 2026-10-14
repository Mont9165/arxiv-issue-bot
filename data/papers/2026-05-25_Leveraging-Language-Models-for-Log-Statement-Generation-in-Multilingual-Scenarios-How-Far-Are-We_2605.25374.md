# Leveraging Language Models for Log Statement Generation in Multilingual Scenarios: How Far Are We?

- arXiv ID: `2605.25374v1`
- Authors: Kazuki Kusama, Honglin Shu, Masanari Kondo, Yasutaka Kamei
- Published: 2026-05-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.25374v1) | [pdf](https://arxiv.org/pdf/2605.25374v1)

## Abstract

Log statements capture critical information for software maintenance activities such as testing, debugging, and failure analysis. Because of this importance, developers must carefully design log statements, which requires significant effort. To support developers, various end-to-end automated log statement generation approaches have been proposed, whereas these approaches have mainly been evaluated within a single programming language environment and their effectiveness in multilingual environments remains underexplored. In this paper, we therefore comparatively evaluate three state-of-the-art log statement generation approaches and five large language models (LLMs) across multiple programming languages. For this purpose, we constructed a multilingual benchmark comprising 150,000 instances across five programming languages. Our empirical results demonstrate that UniLog, a state-of-the-art approach, achieves the best overall performance, maintaining high effectiveness even in multilingual environments. We also observe substantial variance in the difficulty of log generation across languages: Python presents a greater challenge, whereas JavaScript yields comparatively better performance. Detailed analysis reveals that these disparities stem from variations in log insertion distributions and language-specific logging idioms. Our findings indicate that simply scaling model size or the volume of training data is insufficient for multilingual log generation; rather, designing approaches tailored to the specific characteristics of target languages is crucial. These findings suggest that future automated logging techniques should explicitly account for language-specific logging characteristics to achieve robust performance in multilingual software development environments.
