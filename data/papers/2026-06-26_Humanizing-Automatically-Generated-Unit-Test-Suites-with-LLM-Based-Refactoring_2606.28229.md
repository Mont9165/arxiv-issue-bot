# Humanizing Automatically Generated Unit Test Suites with LLM-Based Refactoring

- arXiv ID: `2606.28229v1`
- Authors: Wendkûuni C. Ouédraogo, Yinghua Li, Xueqi Dang, Paweł Borsukiewicz, Lingfeng Bao, Anil Koyuncu, Jacques Klein, David Lo, Tegawendé F. Bissyandé
- Published: 2026-06-26
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.28229v1) | [pdf](https://arxiv.org/pdf/2606.28229v1)

## Abstract

Search-based test generation tools such as EvoSuite produce compilable and high-coverage unit tests at scale, but their suites are often hard to read and maintain. LLMs can generate more natural tests, yet direct generation remains brittle, with compilation rates of only 51-78% in our study. We introduce TestHumanizer, a hybrid SBST+LLM approach that uses LLMs as controlled refactoring layers over compilable SBST suites to improve naming, structure, and developer-oriented clarity while preserving behavior and compilation validity. We evaluate TestHumanizer on 350 classes from Defects4J and SF110. EvoSuite generates 15 suites per class, and each suite is refactored under three context configurations using gpt-4o and mistral-large-2407, yielding 31,500 refactorings. TestHumanizer reaches 88-98% compilation rates, close to EvoSuite's 100% baseline and clearly above direct LLM generation. Structural coverage is largely preserved, typically within 1-2 percentage points, and 86-95% of refactorings satisfy a composite faithful-refactoring threshold. Refactored suites also improve predicted readability, reduce control-flow and cognitive complexity, and mitigate structural smells. The summary-based setting offers the most robust trade-off, while long code-centric prompts are more prone to hallucination-induced failures. A developer study on 30 classes and 444 test methods confirms significant gains in perceived readability and willingness to adopt, with Wilcoxon p less than 0.01 and substantial inter-rater agreement. Overall, LLMs are most effective not as standalone generators but as validation-gated refinement layers over robust SBST outputs.
