# The Role of Agentic Instruction Categories for Code Generation: A Study of Five Python Libraries

- arXiv ID: `2610.21421v1`
- Authors: Warren Gerald Polandra, Yoshiki Higo, Raula Gaikovina Kula
- Published: 2026-10-15
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.21421v1) | [pdf](https://arxiv.org/pdf/2610.21421v1)

## Abstract

Agentic coding systems increasingly rely on repository-level agent files, such as AGENTS.md, to communicate project knowledge and developer intent. However, it remains unclear which categories of agent instructions enable efficient agent-file generation and accurate code generation. We evaluate five instruction categories: Repository Overview, Function Description, Implementation Detail, Testing, and Reconstruction Steps, across all 31 non-empty combinations using two Large Language Models (LLMs), Gemma 4 and GPT-5.4, and five human-written Python libraries. Our study addresses two research questions, comprising five sub-questions, on agent file generation and code generation. Results show that the number of instructions alone does not determine token usage for agent-file generation, with substantial variation across models and libraries. Although most AI-generated libraries compiled successfully regardless of the instruction combination, functional correctness remained limited. No Gemma 4 variant passed all tests, whereas 12.99% of GPT-5.4 variants did. Function Description achieved Gemma 4's highest partial-pass rate, while Reconstruction Steps achieved GPT-5.4's highest full-pass rate. For structural similarity to human-written code, Reconstruction Steps was most frequently associated with libraries closest to the originals in Lines of File and total Cyclomatic Complexity, while Testing and Reconstruction Steps were jointly most frequent for File Count and Function Count.
