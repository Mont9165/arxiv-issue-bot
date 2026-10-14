# Generating Proof-of-Vulnerability Tests to Help Enhance the Security of Complex Software

- arXiv ID: `2605.03956v1`
- Authors: Shravya Kanchi, Xiaoyan Zang, Ying Zhang, Danfeng Yao, Na Meng
- Published: 2026-05-05
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.03956v1) | [pdf](https://arxiv.org/pdf/2605.03956v1)

## Abstract

Developers create modern software applications (Apps) on top of third-party libraries (Libs). When library vulnerabilities are reachable through application code, the applications can be vulnerable to software supply chain attacks. Prior work shows that developers often require concrete and executable evidence, i.e., proof-of-vulnerability (PoV) tests, to decide whether a reported dependency vulnerability poses a practical security risk to their application. However, manually crafting such tests is challenging, and existing tool support is insufficient to automate the procedure. To streamline test generation, we created PoVSmith -- a new approach that combines call path analysis, exemplar test, code context, and feedback into multiple prompts to guide a coding agent (i.e., Codex) and a large language model (i.e., GPT) for test generation, execution, and assessment. We evaluated PoVSmith on 33 $\langle$App, Lib$\rangle$ Java program pairs, where each App depends on a vulnerable Lib. PoVSmith revealed 158 unique application-level entry points (i.e., public methods) calling vulnerable library APIs; 152 (96\%) of them were correctly found, together with the call paths properly recognized. With such method call information, PoVSmith generated 152 tests, 84 (55\%) of which demonstrated feasible ways of attacking Apps by exploiting Lib vulnerabilities. PoVSmith substantially outperforms the state-of-the-art LLM-based approach, as it reduces human involvement while dramatically improving test quality. Our work contributes (1) a novel approach of agent-based test generation, (2) an iterative code refinement process driven by execution feedback, and (3) LLM-based quality assessment grounded in both the test context and execution logs.
