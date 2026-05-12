# Usability as a Weapon: Attacking the Safety of LLM-Based Code Generation via Usability Requirements

- arXiv ID: `2605.10133v1`
- Authors: Yue Li, Xiao Li, Hao Wu, Yue Zhang, Yechao Zhang, Yating Liu, Fengyuan Xu, Sheng Zhong
- Published: 2026-05-11
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.10133v1) | [pdf](https://arxiv.org/pdf/2605.10133v1)

## Abstract

Large Language Models (LLMs) are increasingly used for automated software development, making their ability to preserve secure coding practices critical. In practice, however, many security requirements are implicit or underspecified, whereas usability requirements are explicit and high-signal. This asymmetry motivates our investigation of usability pressure as a practical attack surface: realistic usability-oriented requirements (e.g., new features, performance constraints, or simplicity demands) can cause coding LLMs to satisfy explicit usability goals while silently dropping implicit security constraints -- a form of reward hacking. We formalize this threat as UPAttack and propose U-SPLOIT, an automated framework to craft UPAttack that (i) selects tasks where a model is initially secure, (ii) synthesizes usability pressures by identifying usability rewards of insecure alternatives across three vectors (Functionality, Implementation, Trade-off), and (iii) verifies security regression via both existing test cases and dynamically generated exploit payloads. Across 75 seed scenarios (25 CWEs x 3 cases), spanning multiple languages (Python, C, and JavaScript), U-SPLOIT achieves attack success rates up to 98.1% on multiple state-of-the-art models (e.g., GPT-5.2-chat and Gemini-3-Flash-Preview).
