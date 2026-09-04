# Refusing the Impossible: A Taxonomy and Benchmark for Code Hallucination in Large Language Models

- arXiv ID: `2609.03267v1`
- Authors: Vishnu Asutosh Dasu, Ashish Kundu, Gang Tan
- Published: 2026-09-03
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.03267v1) | [pdf](https://arxiv.org/pdf/2609.03267v1)

## Abstract

Large language models (LLMs) often produce code that looks plausible but is not grounded in reality. The code may import packages that do not exist or claim to implement algorithms that violate proven theorems, while still compiling and running. We study \emph{code hallucination} as \emph{ungrounded generation} and separate it from ordinary \emph{code error} (bugs in otherwise grounded programs). We propose a taxonomy with three dimensions: \textbf{groundedness} (absolute violations of universal truths vs.\ relative fabrications of contingent or ecosystem-specific facts), \textbf{manifestation level} (syntactic, semantic, or factual), and \textbf{behavior} (from confident fabrication to degenerate output), organized into a severity ordering. We build an \textbf{adversarial} suite of deliberately unsatisfiable tasks where the correct response is to refuse and categorize the responses under our taxonomy. The suite contains \textbf{270 prompts} across six languages and 24 subcategories, paired with \textbf{91 matched solvable controls}, and responses are judged by a two-tier protocol validated against human labels (82\% agreement, $κ{=}0.73$). Across twelve open-weight code and reasoning models (4{,}332 judged responses), models produce ungrounded code on about 60\% of unsatisfiable prompts and refuse only 27\%, while wrongly refusing 0\% of the solvable controls.
