# VulnSAGE: Adjudicating SAST Reports by Connecting LLM Reasoning to Program Structure

- arXiv ID: `2610.23035v1`
- Authors: Jinbao Chen, Zixiang Zhou, Yu Zhang, Yihong Wu
- Published: 2026-10-16
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2610.23035v1) | [pdf](https://arxiv.org/pdf/2610.23035v1)

## Abstract

Static Application Security Testing (SAST) reports flag operations whose safety depends on project-specific context, and maintainers must decide which reports describe real defects. Large language models (LLMs) can interpret this context, but adjudicating a report with them requires the decisive code, which often lies far from the reported line, and a decision basis that program analysis can check. We present VulnSAGE, an adjudication system for SAST reports that connects LLM reasoning to program structure in both directions. Its report-centered slicer recovers the dependencies of the reported operation together with the program structure that explains them, such as the caller object on which a helper acts. CLAIM, an intermediate representation for report judgments, records each model interpretation as a semantic fact that cites the program relations it assumes. Program analysis checks these premises, and the verdict follows from the facts whose premises hold. Both mechanisms share a program graph, which lets the model cite the code it reads and lets the checker query those citations. Statically supported true positives then guide proof-of-concept generation and runtime reproduction. Across 187 labeled reports from four corpora covering five vulnerability families, VulnSAGE rejects 89 of 97 false alarms and retains 85 of 90 real defects. Under a common PoC procedure, 25 of its positive verdicts reproduce at runtime, compared with three for the LLM-based adjudicator LLM4SA. Applied to 45,440 alerts raised by five SAST tools on the 200 most-starred C/C++ projects on GitHub, it reproduces 104 defects at runtime. Maintainers have confirmed 24 of the 26 defects they have responded to, including ten previously unknown defects, nine of which are already fixed.
