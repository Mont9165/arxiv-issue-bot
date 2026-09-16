# Enhancing Automated Unit Test Generation for NLP Libraries Using Large Language Models

- arXiv ID: `2609.14784v1`
- Authors: Amirhossein Deljouyi, Annibale Panichella, Andy Zaidman
- Published: 2026-09-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.14784v1) | [pdf](https://arxiv.org/pdf/2609.14784v1)

## Abstract

Automated unit test generation tools like EvoSuite perform well on general-purpose software but often struggle with domain-specific software such as Natural Language Processing (NLP) libraries, where inputs must follow semantic, syntactic, and structural constraints. Large Language Models (LLMs) can generate domain-relevant test code, but tests produced by LLMs alone often fail to compile or achieve sufficient coverage. We propose LLMSuite, a hybrid test generation framework that integrates self-refinement prompting with class-level LLM reasoning into the search-based testing process. In this mechanism, the LLM iteratively improves its test snippets based on feedback from previous generations. This enables the model to produce increasingly precise, domain-consistent code fragments that steer the evolutionary search toward exercising complex and otherwise hard-to-reach behaviors. When no objective improves over multiple generations in the underlying evolutionary algorithm, these refined snippets are parsed and injected into EvoSuite's population to expand the search space. To support our evaluation, we constructed a new dataset comprising 100 classes drawn from five widely used Java NLP projects. We also re-implemented CodaMOSA, a recent hybrid SBST-LLM technique, in Java to enable a direct comparison. Across this dataset, LLMSuite improves branch and line coverage by approximately 10% and 8%, respectively, and achieves an 11% higher mutation score than CodaMOSA-J. Compared to EvoSuite, LLMSuite yields roughly 15% higher branch and line coverage and 5% higher mutation score. Against an LLM-only baseline, it improves structural coverage by 36% and mutation score by about 24.7 percentage points. Finally, LLMSuite complements manually written test suites by exercising domain-specific behaviors that are often left untested.
