# Evaluating Language Models on Cross-Language Code Functional Equivalence

- arXiv ID: `2608.23961v1`
- Authors: Hui Sun, Anderson Uchôa, Rohit Gheyi, Wesley K. G. Assunção
- Published: 2026-08-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2608.23961v1) | [pdf](https://arxiv.org/pdf/2608.23961v1)

## Abstract

Background: Large Language Models (LLMs) have demonstrated strong performance across a variety of code-understanding tasks, leading many to believe that they can reason about program semantics. However, existing evaluations primarily focus on single-language settings or rely on synthetically generated code, raising concerns about whether current results reflect true semantic understanding. Aims: We investigate whether LLMs can accurately judge functional equivalence across different programming languages in human-written code, a setting that requires deeper reasoning beyond superficial similarity. Method: We introduce PolyHuman, a dataset of human-written programs in CPP, Java, and Python. Using this dataset, we evaluate intra- and inter-language equivalence detection across open-weight and proprietary LLMs, selecting GPT-o4-mini as a representative model to assess stability. We then manually analyze 81 cases of systematic disagreement in which models incorrectly judge functional equivalence, examining the code logic and the generated Chain-of-Thought reasoning. Finally, we categorize these failures and compare them across GPT-o4-mini, Claude-Opus-4.7, and Gemini-3-Flash to determine whether they reflect model-specific issues or broader limitations of state-of-the-art LLMs. Results: We identify a difficulty-dependent breakdown in equivalence judgment (harder problems make the model increasingly prone to misclassifying non-equivalent code as equivalent), a model-specific sensitivity to programming language for the best-performing model (particularly a more conservative behavior on Python), and a partial reliance on similarity-based cues. GPT-o4-mini also shows substantial run-to-run instability under identical settings, indicating inconsistent rather than absent capability. Conclusions: Current LLMs do not reliably capture functional equivalence within or across languages.
