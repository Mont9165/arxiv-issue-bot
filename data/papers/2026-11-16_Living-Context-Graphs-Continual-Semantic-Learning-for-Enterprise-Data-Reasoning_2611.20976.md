# Living Context Graphs: Continual Semantic Learning for Enterprise Data Reasoning

- arXiv ID: `2611.20976v1`
- Authors: Varun Agrawal, Ayush Srivastava, Eshan Gujar, Kaushal Kumar, Ayush Gupta
- Published: 2026-11-16
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`, `cs.ET`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2611.20976v1) | [pdf](https://arxiv.org/pdf/2611.20976v1)

## Abstract

Enterprise AI can now perform analytics, reporting, and data-driven workflows, yet the data foundations it relies on remain hard to operationalize: business meaning, relationships, metric definitions, and reporting conventions are absent from database schemas and scattered across undocumented systems and tribal knowledge. We introduce the Living Context Graph (LCG), a continually learned context layer that makes existing enterprise data operational for AI without requiring a copy or transformation of the underlying warehouse. LCG bootstraps base semantics and relationships from the data itself, builds a concept graph that indexes business context as queries are served, writes durable semantic learnings from verified outcomes, and withdraws or re-earns context when later outcomes contradict prior routes. We evaluate LCG through text-to-SQL, a core data-reasoning task, on a transfer-aware split of three BIRD databases comprising 499 questions: 353 form the learning history and 146 are held out and never used to update the context layer. Bootstrapping alone improves overall accuracy by +4.6 percentage points. Learning only from the history raises accuracy on the untouched held-out transfer set by +22.6 points (95% CI [+14.4, +30.8]), exceeding five-shot retrieval from the same history by +12.3 points. Incremental learning reaches the one-shot endpoint within observed evaluation noise on every database. Ablating the graph changes held-out accuracy by at most one question per database but increases per-query cost 2.3-3.3x and median latency 1.8-3.4x: continually learned semantics drive accuracy, while the graph makes that context efficient to serve.
