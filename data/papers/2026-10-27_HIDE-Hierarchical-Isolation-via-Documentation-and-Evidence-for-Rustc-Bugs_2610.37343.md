# HIDE: Hierarchical Isolation via Documentation and Evidence for Rustc Bugs

- arXiv ID: `2610.37343v1`
- Authors: Tianrong Zhang, Yakun Zhang, Dan Hao
- Published: 2026-10-27
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.37343v1) | [pdf](https://arxiv.org/pdf/2610.37343v1)

## Abstract

Rustc bugs can prevent valid programs from compiling or cause incorrect compilation results, making the identification of responsible source files essential for repair. Using large language models (LLMs) for rustc bug isolation raises three challenges. First, distributed compiler functionality requires understanding both what individual files do and how they work together. Second, a large source file search space makes exhaustive analysis of all files costly. Third, including documentation and source code for many candidate files in LLM prompts leads to context overload, which can reduce bug isolation accuracy. We propose HIDE, a hierarchical LLM-based approach that combines compiler documentation with bug evidence to rank suspicious rustc source files. Given a rustc revision and a bug context, HIDE consists of two stages that generate compiler documentation and narrow the search space. To understand distributed compiler functionality, the Layered Documentation Aggregation stage summarizes what individual files do and how files with similar functions work together. To reduce the large source file search space, the Hierarchical Bug Isolation stage uses hierarchical candidate selection to reduce the number of files requiring detailed analysis. To mitigate context overload, this stage uses Scoped Candidate Competition and Evidence-Guided Code Slicing to limit the number of candidates and the amount of source code included in each prompt, respectively. We evaluate HIDE on 160 reproducible rustc bugs and compare it with Agentless, SoapFL, and GraphLocator. With GPT-5.4, HIDE achieves 42.08% Accuracy@1 and 80.42% Accuracy@10, exceeding the strongest baseline results by 5.83% and 6.04%, respectively. These results demonstrate that generating compiler documentation, narrowing candidates hierarchically, and limiting analysis context enable effective rustc bug isolation.
