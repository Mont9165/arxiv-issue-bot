# Bug Finding With Agentic Symbolic Execution

- arXiv ID: `2611.15596v1`
- Authors: George Granberry, Wolfgang Ahrendt, Andy Gordon, Moa Johansson
- Published: 2026-11-11
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LO`, `cs.SC`
- Links: [abs](http://arxiv.org/abs/2611.15596v1) | [pdf](https://arxiv.org/pdf/2611.15596v1)

## Abstract

Symbolic execution, in tools such as CrossHair for Python, is a powerful technique for finding bugs, but two barriers hinder its adoption: the human effort of annotating code with assertions, and the need to model the execution environment outside Python, such as an external database. To overcome both, we design an agentic harness that orchestrates the symbolic execution tool CrossHair together with an AI coding agent. Without human intervention, it instruments a repository with assertions, synthesizes a constraint-aware symbolic environment for the database, runs symbolic execution, and constructs a concrete test as evidence for each bug it reports. We evaluate our harness on 1,156,044 lines of Python code over 11 popular open-source Python web applications (Zulip, NetBox, Apache Superset, and others). With the synthesized environment, CrossHair executes 81% of the 5,406 contracted functions, against 4.5% without it. Our pipeline finds 1,050 bugs, each reproduced by a test against the unmodified application, 221 of them by CrossHair, and 312 of them are missed by a baseline in which the same LLM inspects the code. The two find different kinds of bugs: CrossHair's are mostly crashes on input-domain corner cases that validation admits, such as empty strings, missing fields and unusual characters, while inspection's are mostly bugs that produce wrong output. Our framework thus lets symbolic execution supplement inspection-based bug finding.
