# The Illusion of Safety: Multi-Tier Verification of AI vs. Human C++ Code

- arXiv ID: `2607.00107v1`
- Authors: Saif Mahmud, Fadul Sikder, Yuede Ji, Zhang Haotian,  Jeff,  Lei
- Published: 2026-06-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.00107v1) | [pdf](https://arxiv.org/pdf/2607.00107v1)

## Abstract

Large language models increasingly generate C++, a memory-unsafe language where a single overlooked violation can become an exploitable bug. Yet most security evaluations of AI-generated code rely on static analysis alone, which flags warnings without confirming runtime violations or reasoning about untested paths. We ask whether AI-generated C++ is measurably less safe than human-written code, and whether common verification tools agree on the risk. We introduce VULBENCH-CPP, a benchmark of 8,918 C++ programs from three open-weight LLMs (Gemma 3 27B IT, LLaMA 3.3 70B Instruct, Qwen 2.5 Coder 32B Instruct) and human authors across 851 competitive-programming tasks. Each program is annotated by four verification tiers: functional testing, static analysis (cppcheck, clang-tidy), dynamic analysis (ASan/UBSan), and bounded model checking (ESBMC). Accounting for the correlation among solutions to a shared task, we find that AI-generated code is roughly twice as likely as human code to trigger a confirmed runtime violation, even after controlling for code length and test pass-rate. Under static analysis the two look equally safe, but this is misleading: the apparent similarity reflects code length rather than real safety, and the tiers detect largely different classes of violation, so no single tier is sufficient. The gap is consistent across independent generations.
