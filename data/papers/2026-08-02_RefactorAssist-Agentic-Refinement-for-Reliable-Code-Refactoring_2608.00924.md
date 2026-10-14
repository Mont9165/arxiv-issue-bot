# RefactorAssist: Agentic Refinement for Reliable Code Refactoring

- arXiv ID: `2608.00924v1`
- Authors: Jonathan Cordeiro, Shayan Noei, Ying Zou
- Published: 2026-08-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.00924v1) | [pdf](https://arxiv.org/pdf/2608.00924v1)

## Abstract

Code refactoring aims to enhance the internal structure of source code without affecting its functional behavior. The recent advancements of Large Language Models (LLMs) have demonstrated potential for automating software engineering tasks, such as code refactoring. However, the refactorings produced by LLMs often introduce subtle errors, leading to functional behavior changes and failed unit tests, which limit their practical adoption. To address the limitations of LLM-generated refactorings, we analyze the root causes of their failures and develop the RefactorAssist agent to improve the functional correctness of LLM-generated refactorings. To this end, we use 10 open-source Java projects with their native test suites and manually evaluate why LLM-generated refactorings fail unit tests. We then design an agentic approach that leverages unit-test logs, error explanations, project context retrieval, and code diffs to guide the iterative refactoring. Our findings show that the main reasons for failure are context misunderstanding/hallucination (24.3%), incorrect or inconsistent renaming (15.3%), adding new functionality or variables (13.7%), code incompleteness (11.3%), syntax and structural errors (9.7%), edge cases not handled (9%), improper type handling (8.7%), and variables outside scope (8%). To make our approach cost-effective, RefactorAssist first applies a static repair step for missing imports, unbalanced brackets, and compilation errors without LLMs. For remaining failures, RefactorAssist incorporates error logs and code diffs, achieving up to a 70.8% repair rate on the remaining failures and a 94.2% cumulative pass rate under the best-performing configuration. These results indicate that static checks and test-guided, context-aware agentic repair can increase the reliability of LLM-generated refactorings, bringing them closer to practical integration within developer workflows.
