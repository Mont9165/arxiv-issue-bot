# LLM vs. Human Unit Tests: Fault Detection on Real Python Bugs

- arXiv ID: `2606.08588v1`
- Authors: Phouvadeth Vathana, Prapti Bhatt, Rishi Patel, Nasir U. Eisty
- Published: 2026-06-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.08588v1) | [pdf](https://arxiv.org/pdf/2606.08588v1)

## Abstract

Large language models (LLMs) have shown considerable promise for automated unit test generation, yet their practical effectiveness relative to human-written tests remains poorly understood. Existing evaluations commonly rely on coverage-oriented benchmarks that do not assess fault-detection capability directly. We present an empirical comparison of LLM-generated and human-written unit tests across three complementary Python benchmarks: 29 real historical bugs from BugsInPy, a function-level benchmark drawn from python-slugify and packaging, and a controlled paired benchmark. Our generation pipeline couples Gemini 2.5 Flash with a lightweight lexical retrieval mechanism that supplies bug-relevant context at generation time. Across eight quality dimensions, LLM-generated tests with retrieval-augmented context detect faults in 69% of cases compared to 17.2% for general-purpose human-written tests (Fisher's exact, $p < 0.001$, Cohen's $h = 1.10$). Critically, line and branch coverage are nearly identical between the two approaches (84.8% vs. 88.5% and 75.2% vs. 82.1%), confirming that coverage is an insufficient proxy for fault-detection capability. We discuss the conditions under which each approach excels, characterize their complementary strengths, and identify the critical role of retrieval context and reproducible benchmark construction in meaningful test-quality evaluation.
