# A Study on the Impact of Natural Language Differences in Prompts on Automatic Code Generation Using LLMs

- arXiv ID: `2609.18311v1`
- Authors: Haruka Tokumasu, Masanari Kondo, Alexander Serebrenik, Dong Wang, Kei Koyanagi, Kotaro Noguchi, Naoyasu Ubayashi, Yasutaka Kamei
- Published: 2026-09-16
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.18311v1) | [pdf](https://arxiv.org/pdf/2609.18311v1)

## Abstract

Large Language Models (LLMs) have demonstrated remarkable performance in automatic code generation tasks, thereby encouraging new research in this area. Although numerous studies have explored LLM-based code generation, the impact of the natural language in input prompts remains unexplored (language bias). This study aims to (1) quantify how the natural language of input prompts influences LLM-based code generation performance and (2) evaluate a mitigation strategy to reduce language bias in code generation. We assess code generation Accuracy on AtCoder, LeetCode, and BigCodeBench. To quantify the language bias on code generation, each problem is presented in English, Japanese, and Chinese. We use seven LLMs (GPT-4o, o3-mini, DeepSeek-V3.2, Llama-3, Qwen2.5-Coder-14B, Qwen2.5-Coder-0.5B, and GitHub Copilot) and assess their performance in terms of Accuracy (the number of problems for which generated code passes all test cases). We compare Accuracy before and after translation to evaluate the effectiveness of translation as a mitigation strategy. We observed that the natural language of problem statements affects LLM-based code generation performance. Specifically, the languages officially supported by each dataset achieved the highest median Accuracy. Also, translation improved Accuracy, but its effectiveness was not consistent across datasets and model types. We found that AtCoder contained a particularly high proportion of narrative-style problem statements and longer problem statements. Natural language significantly affects LLM code generation accuracy. Translation can mitigate language bias in some settings, but its effectiveness depends on the dataset and model type. Furthermore, the narrative aspects and context length of input prompts are important factors related to language bias and the effectiveness of translation as a mitigation strategy.
