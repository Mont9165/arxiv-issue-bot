# Strategies for Guiding LLMs to Use Software Design Patterns: A Case of Singleton

- arXiv ID: `2605.26898v1`
- Authors: Viktor Kjellberg, Farnaz Fotrousi, Miroslaw Staron
- Published: 2026-05-26
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.26898v1) | [pdf](https://arxiv.org/pdf/2605.26898v1)

## Abstract

Large Language Models (LLMs) can generate functional source code from natural-language prompts, but often fail to consistently follow higher-level architectural structures or design patterns. Since LLMs are increasingly used in software engineering, their ability to apply established design principles to generated code is crucial to the long-term success of software products. Therefore, the goal of this paper is to identify strategies for guiding LLMs to incorporate design patterns into the generated source code. We designed a computational experiment to evaluate the ability of 13 LLMs to generate code that follows the Singleton design pattern, using four prompting strategies: instructions, binary automated feedback, extensive automated feedback, and extensive feedback with few-shot prompts, in 164 Java coding challenges from HumanEval-X. Our results shows that the optimal strategy to guide LLMs to include design patterns depends heavily on the type of model. Still, overall, iterative binary feedback provides the best alignment with Singleton while preserving or improving the code's functionality. With guiding with instructions, Llama 3.3 generated Singleton classes in 100% of cases and improved code functionality, increasing the number of tests passed by 34.1 percentage points. It achieved a similar result with guidance through instructions and binary feedback. Qwen 3 (8B) increased the alignment with Singleton to 99.2% and the functionality to 58.6% using binary feedback. Our result suggests that even simple strategies can be used to guide LLMs to use design patterns.
