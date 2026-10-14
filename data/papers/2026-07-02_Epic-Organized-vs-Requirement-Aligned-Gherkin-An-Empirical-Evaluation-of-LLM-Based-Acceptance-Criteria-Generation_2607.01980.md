# Epic-Organized vs. Requirement-Aligned Gherkin: An Empirical Evaluation of LLM-Based Acceptance Criteria Generation

- arXiv ID: `2607.01980v1`
- Authors: Shahbaz Siddeeq, Mateen Abbasi, Jussi Rasku, Zheying Zhang, François Christophe, Tommi Mikkonen, Pekka Abrahamsson
- Published: 2026-07-02
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.01980v1) | [pdf](https://arxiv.org/pdf/2607.01980v1)

## Abstract

Automated authoring of Gherkin Behavior-Driven Development (BDD) acceptance criteria remains a manual bottleneck in requirements engineering. This study investigates whether epic-organized LLM-generated Gherkin produces higher quality and coverage than requirement-aligned generation. We compare our Timeless (an epic-organized LLM pipeline) approach against a naive large language model (LLM) baseline on four requirements documents (107 requirements) from the PURE dataset. Evaluation covers structural metrics, automated requirement coverage via TF-IDF and dense embeddings, and blind expert assessment by four researchers. In our evaluation, the JSON-constrained pipeline produced structurally valid scenarios across all generated outputs, while the zero-shot baseline achieved 99% structural validity. Semantic coverage was comparable to the baseline, with Timeless achieving 94.3% semantic Requirement Coverage Rate compared with 92.9% for the baseline. TF-IDF produced lower coverage scores for the epic-organized output, suggesting that lexical metrics may miss coverage when scenarios paraphrase requirements at a higher level of abstraction. Expert raters prefer the epic-organized strategy on Correctness (4.61 vs 4.14), Executability (4.61 vs 4.07), and Completeness (4.31 vs 3.50). Overall, the results suggest that epic-organized generation can improve perceived Gherkin quality while maintaining comparable semantic coverage, although broader replication is needed before generalizing this finding.
