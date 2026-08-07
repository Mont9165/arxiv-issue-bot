# Validating ETCS Data with the B Mathematical Language: An Industrial Pipeline and a Blueprint for LLM Integration

- arXiv ID: `2607.26111v1`
- Authors: Lecomte Thierry, Germain Vincent
- Published: 2026-07-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.26111v1) | [pdf](https://arxiv.org/pdf/2607.26111v1)

## Abstract

Can large language models participate in the production and validation of ERTMS/ETCS data without undermining the certification arguments required by CENELEC EN 50128/50716? ERTMS/ETCS is a distributed safety-critical system (trackside, onboard, radio-block centre) whose behaviour is parameterised by large volumes of data drawn from the UNISIG Subsets; errors in that data propagate through the distributed architecture. This paper reports the current status of an ongoing industrial research effort at CLEARSY, ValidAItion, that bridges the ERTMS Operational Simulator to the CLEARSY Data Solver and applies rules expressed in the B mathematical language to that trackside data. During construction, a large language model (Claude) has authored the rule corpus and the parsers through a Model Context Protocol server; every proposal is adjudicated by the downstream toolchain and by systematic human review, and the toolchain has already rejected a syntactically valid but semantically illegal generated scenario. The contribution is architectural and industrial, not algorithmic: the work combines frameworks already in use at CLEARSY (CLEARSY Data Solver, ERTMS Operational Simulator) with a conversational authoring loop, rather than proposing a new formal method. It is a progress report: rule coverage is growing, the human-review campaign is underway, and the quantitative results will be published separately. The paper argues, on the evidence gathered so far, that formal rules in the mathematical language of B must remain the source of truth, while the language model serves as the fenced assistant in a distributed safety-critical railway system: AI proposes, the formal oracle disposes, the human confirms.
