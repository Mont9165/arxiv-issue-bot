# SatMend: LLM Agents for Automated Software Repair in Satellite Constellations with Intermittent Ground Contact

- arXiv ID: `2611.29227v1`
- Authors: Pengcheng Luo, Zenghui Zhang, Genke Yang, Jian Chu
- Published: 2026-11-22
- Primary category: `cs.SE`
- Categories: `cs.SE`, `eess.SY`
- Links: [abs](http://arxiv.org/abs/2611.29227v1) | [pdf](https://arxiv.org/pdf/2611.29227v1)

## Abstract

Satellite constellations rely on onboard software to sustain services across cooperating spacecraft. Maintaining this software requires handling related component versions and different failure causes while delivering repairs through intermittent ground contact. Automated software repair in satellite constellations remains underexplored, particularly the coordination of repairs across related versions with verified onboard recovery under intermittent ground contact. To address this gap, we propose SatMend, a software repair method driven by ground-based large language model (LLM) agents. SatMend organizes related versions into persistent sessions to retain diagnostic context and combines source and runtime evidence to select code repair or state recovery actions. It validates each version separately and submits ready candidates during continued repair, allowing ground preparation to overlap with onboard delivery and verification. Experimental results show that across configurations with 16 to 64 satellites, SatMend restores 192 of 224 faulty applications within 600 s, compared with 40 for SWE-agent, 77 for Agentless, 124 for RepairAgent, and 115 for SWE-Search. These results demonstrate SatMend's effectiveness in restoring applications and supporting service continuity in satellite constellations with intermittent ground contact.
