# AOCI: Symbolic-Semantic Indexing for Practical Repository-Scale Code Understanding with LLMs

- arXiv ID: `2605.02421v1`
- Authors: Jinshi Liu, Hanying Zuo, Congyin Cao, Anran Zhang, Yixuan Liu, Xinzhou Xie
- Published: 2026-05-04
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.02421v1) | [pdf](https://arxiv.org/pdf/2605.02421v1)

## Abstract

Large language models struggle with understanding codebases beyond a certain scale -- repositories with hundreds of thousands of lines of code. Existing methods -- retrieval, summarization, agent exploration -- each construct a different view at query time. The view varies between runs, and what persists is typically ad-hoc rather than systematic. This paper introduces AOCI (AI-Oriented Code Indexing): a symbolic-semantic repository representation -- a structured blueprint that an LLM can read in a single pass to gain a complete repository-level picture of the system's architecture, dependencies, and key design decisions before any task. An AOCI index consists of encoding rules followed by entries, with one entry per code unit (file or database table). Each entry pairs a symbolic tag with semantic content. The symbolic component provides architectural coordinates; the semantic component carries function, dependencies, and constraints. Together they form a consistent, stable representation of the entire system. Index maintenance is incremental: when code changes, only affected entries are regenerated under protocol rules. The AOCI Platform automates this process, keeping the blueprint aligned with the code. We evaluated AOCI on four projects across three LLMs and six context conditions (2,160 evaluations). AOCI outperforms all deployable baselines and ranks second only to the Oracle upper bound in overall accuracy. On 19 industrial tasks across five systems, AOCI produced zero final-state defects, while three mainstream agent-based tools introduced defects in 12 tasks and consumed 4--130$\times$ more tokens ($p < 0.001$). The advantage grows with task complexity.
