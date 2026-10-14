# What Happens When the Model Eats the Stack? Rethinking the Research Agenda for Data Agents to Withstand the Bitter Lesson

- arXiv ID: `2609.03141v1`
- Authors: Liana Patel, Siddharth Jha, Negar Arabzadeh, Carlos Guestrin, Ion Stoica, Matei Zaharia
- Published: 2026-09-02
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.03141v1) | [pdf](https://arxiv.org/pdf/2609.03141v1)

## Abstract

The bitter lesson poses an existential question for the data systems community, whereby large language models (LLMs) trained end-to-end are rapidly internalizing new capabilities that previously required carefully engineered data agents. Guided by empirical insights, we argue that as models continue to improve, many proposed system layers designed to compensate for model limitations on a given task will increasingly be subsumed by the model itself. We instead identify enduring research opportunities, which lie in supporting data agents across many queries with curated contextual information about the data environment, which we call persistent semantic context. We find that these context layers demonstrate strong promise for improving data agent performance, but they also raise significant system challenges. Thus, a key requirement for future data systems will lie in natively serving persistent semantic contexts as a first-class abstraction in order to enable capable data agents working over huge, complex knowledge corpora. Towards this vision, we outline exciting new research opportunities, including designing efficient context data structures, storage methods, compression techniques, and semantic consistency protocols, to ensure integrity and correctness of the stored contextual knowledge.
