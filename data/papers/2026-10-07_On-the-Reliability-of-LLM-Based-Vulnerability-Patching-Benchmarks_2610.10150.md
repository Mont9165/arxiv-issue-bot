# On the Reliability of LLM-Based Vulnerability Patching Benchmarks

- arXiv ID: `2610.10150v1`
- Authors: Dang K Le, Wenxuan Shi, Xinyu Xing
- Published: 2026-10-07
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.10150v1) | [pdf](https://arxiv.org/pdf/2610.10150v1)

## Abstract

Large language models (LLMs) have shown strong potential for automated vulnerability patching, but current benchmarks can substantially distort reported performance. Drawing on extensive experience developing, running, and stress-testing such frameworks, we identify under-examined pitfalls across three dimensions: (1) agent-level factors, where prompting, tool availability, and detailed instructions can raise success rates without improving developer-aligned patch quality; (2) framework-level factors, where permission errors, infrastructure bugs, and timeout handling can silently suppress or inflate performance; and (3) dataset-level factors, where bug reports and single proof-of-concept (PoC) tests fail to capture whether patches address root causes or follow developer intent. We curate 112 historical bugs from 84 open-source C/C++, Go, and Rust projects, each with PoC tests, regression tests, and additional developer tests that assess alignment with the original developers' design principles. Through controlled experiments and case studies, we show that LLMs can achieve high PoC passing rates under ideal conditions, yet benchmark execution choices can materially change measured success. More importantly, developer-test passing rates remain low and improve only marginally with newer models, suggesting that models increasingly suppress symptoms without consistently producing upstream-quality fixes. These results show that benchmark scores are highly sensitive to evaluation design, and we provide practical guidelines for more rigorous, reliable, and reproducible evaluation.
