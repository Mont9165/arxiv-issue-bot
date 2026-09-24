# AST-Based Automated Elimination of break and continue Statements in Java Code

- arXiv ID: `2609.27627v1`
- Authors: Andrés Juárez, José Chicano, Rubén Saborido
- Published: 2026-09-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.27627v1) | [pdf](https://arxiv.org/pdf/2609.27627v1)

## Abstract

This work presents the development of an automatic refactoring tool for Java code built on top of the Eclipse JDT API. The proposed approach transforms control structures containing break and continue statements within different types of loops into semantically equivalent constructs that avoid their explicit use. To achieve this, auxiliary boolean variables are introduced to restructure the control flow while preserving the original program behavior.
  The main objective of this transformation is to improve code structure and enable the application of subsequent automated refactorings, particularly those based on the Extract Method operation, which are typically restricted by the presence of jump statements. The implementation relies on the analysis and rewriting of the Abstract Syntax Tree (AST), ensuring semantic equivalence in all addressed scenarios.
  The tool was validated through 54 manually designed test cases and 151 units tests, all of which produced satisfactory results. In addition, it was applied to 139 methods from seven open-source projects, generating code without compilation errors and preserving the original behavior as verified by the projects' test suites. The results demonstrate that the proposed approach safely automates the restructuring of code containing break and continue statements, facilitating further evolution and structural analysis.
