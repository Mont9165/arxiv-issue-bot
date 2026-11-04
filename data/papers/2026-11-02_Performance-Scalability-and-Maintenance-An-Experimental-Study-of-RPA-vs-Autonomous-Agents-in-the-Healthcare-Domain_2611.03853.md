# Performance, Scalability and Maintenance: An Experimental Study of RPA vs. Autonomous Agents in the Healthcare Domain

- arXiv ID: `2611.03853v1`
- Authors: Daniel Schulz, Pedro Cabral Buchaim, Bernardo Soares, Fernando Rafael Ensslin Schwengber, Lorenzo Farias, Daniela Duarte da Silva Bagatini, Ana Paula Wernz da Cunha Müller
- Published: 2026-11-02
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.03853v1) | [pdf](https://arxiv.org/pdf/2611.03853v1)

## Abstract

Healthcare information systems are fragmented, and retrieving data from legacy web portals is a recurrent need. Robotic Process Automation (RPA) is deterministic but sensitive to interface changes, whereas autonomous agents based on large language models (Agent Process Automation, APA) promise adaptability at a higher computational cost. Following Design Science Research, we developed and compared an RPA solution (Playwright) and an APA solution (browser-use, LangGraph and Gemini 2.5 Flash-lite) to retrieve mammography and breast ultrasound reports from a laboratory portal, treating reports solely as informational artifacts. Across two rounds (T and T+7), RPA reached 98.90% accuracy and 98.27% F1-score versus 96.49% and 94.48% for APA, was about 13 times faster (16.07 s vs. 207.21 s per patient) and cost about six times less per report (USD 0.030 vs. 0.187). Both reached 100% step success rates; APA varied more over time. For a stable interface, RPA was superior.
