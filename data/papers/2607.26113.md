# NISPO: Open-source IUPAC name generation tool

- arXiv ID: `2607.26113v1`
- Authors: Nicholas T. Runcie, Fergus Imrie, Charlotte M. Deane
- Published: 2026-07-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.26113v1) | [pdf](https://arxiv.org/pdf/2607.26113v1)

## Abstract

Systematic International Union of Pure and Applied Chemistry (IUPAC) names are standard for communicating molecular structures in chemical literature, patents, and databases. We introduce NISPO, an open-source RDKit-based Python package for IUPAC name generation. NISPO was developed by an agentic self-improvement loop using OpenAI's Codex with the GPT-5.5 model. A generated name was considered correct if the open-source OPSIN tool parsed it back to the input structure. Guided by this objective, the agent implemented and refined NISPO against 2.68 million molecules from SureChEMBL, resulting in the tool achieving 98.1% round-trip accuracy on a held-out set of 103 million PubChem molecules. NISPO is freely available at https://github.com/oxpig/nispo.
