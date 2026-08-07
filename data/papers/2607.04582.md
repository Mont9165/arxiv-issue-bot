# Finetuning Lightweight LLMs for Control Flow Graph Generation

- arXiv ID: `2607.04582v1`
- Authors: Hanyu Zhang, Tomoji Kishi
- Published: 2026-07-06
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.04582v1) | [pdf](https://arxiv.org/pdf/2607.04582v1)

## Abstract

Control Flow Graph (CFG) is an important program representations for software analysis, code understanding, and software maintenance. Traditional CFG generation techniques mainly rely on bytecode or abstract syntax trees. However, these approaches usually require complete, compilable, and syntax error-free code, which limits their applicability to incomplete or erroneous code. Furthermore, they often depend on language specific tools, making it difficult to support multiple programming languages in a unified manner. To address these limitations, this paper investigates the use of fine-tuned lightweight large language models (LLMs) for CFG generation. We first design a unified CFG output format and a task-specific fine-tuning prompt for CFG generation. Then, we construct a dataset based on an existing LeetCode dataset through automatic CFG generation and error augmentation. We evaluate the proposed approach on six lightweight LLM models, including three code-specific LLMs: CodeLlama, QwenCoder, and DeepSeekCoder; and three general purpose LLMs: Llama3.2-3B, Qwen-4B, and Phi-4B. The experimental results show that, through fine-tuning, lightweight LLMs achieve promising results for CFG generation, particularly when the input code is incomplete or erroneous. It also demonstrates cross-language generalization capability on programming language not included in the fine-tuning data.
