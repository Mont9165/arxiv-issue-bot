# PrepBench: How Far Are We from Natural-Language-Driven Data Preparation?

- arXiv ID: `2605.08687v1`
- Authors: Jingzhe Xu, Rui Wang, Jiannan Wang, Guoliang Li
- Published: 2026-05-09
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.08687v1) | [pdf](https://arxiv.org/pdf/2605.08687v1)

## Abstract

Data preparation is a central and time-consuming stage in data analysis workflows. Traditionally, commercial tools have relied on graphical user interfaces (GUIs) to simplify data preparation, allowing users to define transformations through visual operators and workflows. Recent advances in large language models (LLMs) raise the possibility of a paradigm shift toward natural language (NL)-driven data preparation, in which users can specify preparation intents in NL directly. However, it remains unclear how far current LLM-based agents are from this paradigm shift in practice. Existing code generation benchmarks do not capture key characteristics of data preparation, including ambiguous user intents, imperfect real-world data, and the need to translate code into interpretable workflows for validation. To bridge this gap, we present PrepBench, a benchmark designed to evaluate NL-driven data preparation along three core capabilities: interactive disambiguation, prep-code generation, and code-to-workflow translation. We crawl data from the Preppin' Data Challenges, and then extend it into a systematically designed benchmark. The benchmark covers diverse domains, and each task involves 3 to 18 data preparation steps. Nearly half of the tasks require over 100 lines of Python code, and the longest solutions approach 300 lines. Our evaluation shows that, despite recent progress, realizing this paradigm shift remains challenging for state-of-the-art LLMs. PrepBench provides a principled benchmark for measuring this gap and helps identify key challenges toward realizing NL-driven data preparation.
