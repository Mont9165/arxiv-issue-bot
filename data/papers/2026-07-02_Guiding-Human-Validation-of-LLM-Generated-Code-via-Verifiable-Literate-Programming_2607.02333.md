# Guiding Human Validation of LLM-Generated Code via Verifiable Literate Programming

- arXiv ID: `2607.02333v1`
- Authors: Ziqi Yuan, Wenhao Lu, Hao Wu, Dunhong Jin, Chuan Wu
- Published: 2026-07-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2607.02333v1) | [pdf](https://arxiv.org/pdf/2607.02333v1)

## Abstract

Vibe coding democratizes software development by allowing users to generate code via natural-language (NL) interaction with large language models (LLMs). However, the code is reliable only when it faithfully implements the user's intent, which is difficult and labor-intensive for users to validate. Existing validation methods either rely on LLM-assisted automated testing, which suffers from prompt ambiguity and model fallibility, or involve users only in partial software artifacts such as prompts and test cases, which may overlook corner cases and program details. Motivated by a bug study of LLM-generated code, we find that detailed human feedback is essential, as failures often stem from underspecified requirements or subtle semantic deviations.
  This paper presents verifiable literate programming (VLP), a human-in-the-loop framework designed to make the review/validation process of LLM-generated code accessible to users at all programming levels. At its core, VLP proposes unambiguous NL-based documentation as a readable intermediate layer between prompts and code. The documentation demonstrates concrete program semantics and enables users to provide feedback on potential intent-code mismatches. It supports human-involved, end-to-end repair and validation via three techniques: (i) an NL-style literate language with unambiguous syntax and mostly deterministic code-to-documentation translation, (ii) LLM-based fine-grained mismatch detection that uses trace links between prompts and documentation to focus users' review effort on suspicious documentation lines, and (iii) a verification module that leverages user-validated documentation to derive API-usage checks and formal properties, which are then verified against the generated code using model checking. Our evaluation shows that VLP improves code pass@1 from 28.7%-73.2% to 65.4%-93.5% with reasonable user effort.
