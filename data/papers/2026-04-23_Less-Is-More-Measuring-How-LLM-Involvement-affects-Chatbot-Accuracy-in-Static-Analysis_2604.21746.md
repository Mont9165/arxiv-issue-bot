# Less Is More: Measuring How LLM Involvement affects Chatbot Accuracy in Static Analysis

- arXiv ID: `2604.21746v1`
- Authors: Krishna Narasimhan
- Published: 2026-04-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.21746v1) | [pdf](https://arxiv.org/pdf/2604.21746v1)

## Abstract

Large language models are increasingly used to make static analysis tools accessible through natural language, yet existing systems differ in how much they delegate to the LLM without treating the degree of delegation as an independent variable. We compare three architectures along a spectrum of LLM involvement for translating natural language to Joern's query language \cpgql{}: direct query generation (\approach{1}), generation of a schema-constrained JSON intermediate representation (\approach{2}), and tool-augmented agentic generation (\approach{3}). These are evaluated on a benchmark of 20 code analysis tasks across three complexity tiers, using four open-weight models in a 2\(\times\)2 design (two model families \(\times\) two scales), each with three repetitions. The structured intermediate representation (\approach{2}) achieves the highest result match rates, outperforming direct generation by 15--25 percentage points on large models and surpassing the agentic approach despite the latter consuming 8\(\times\) more tokens. The benefit of structured intermediates is most pronounced for large models; for small models, schema compliance becomes the bottleneck. These findings suggest that in formally structured domains, constraining the LLM's output to a well-typed intermediate representation and delegating query construction to deterministic code yields better results than either unconstrained generation or iterative tool use.
