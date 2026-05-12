# Generating Complex Code Analyzers from Natural Language Questions

- arXiv ID: `2605.09304v1`
- Authors: Amirmohammad Nazari, Sadra Sabouri, Wang Bill Zhu, Robin Jia, Souti Chattopadhyay, Mukund Raghothaman
- Published: 2026-05-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.HC`
- Links: [abs](http://arxiv.org/abs/2605.09304v1) | [pdf](https://arxiv.org/pdf/2605.09304v1)

## Abstract

Many software development tasks, such as implementing features and fixing bugs, begin with developers posing questions about a codebase. However, answering questions about codebases that span millions of lines of code across thousands of files is non-trivial. Standard tools like grep cannot answer questions requiring semantic or inter-procedural reasoning, and large language models (LLMs) struggle with large codebases due to resource and context constraints. In this paper, we present Merlin, a new system for answering free-form questions that require analytical reasoning about code. Merlin integrates an LLM with CodeQL, a program analysis framework that supports expressive queries over large codebases. We face two principal challenges in the design of such systems: First, program analysis queries are diverse and semantically complex; as a result, even syntactically well-formed queries frequently produce degenerate/empty results. Furthermore, relatively few CodeQL queries are available online, limiting the out-of-the-box effectiveness of LLMs as CodeQL query generators. We address these challenges by developing a RAG-based iterative query-generation approach and a novel self-test technique. Our query debugging technique builds on the idea of assistive queries, which generate concrete witnesses that expose and explain semantic flaws in candidate queries. We evaluate Merlin through both experimental and user studies. Over a set of natural language questions derived from common bug-finding tasks, Merlin discovered not only the majority of software issues reported by other approaches, but also issues that would have otherwise remained undetected. Through a within-subject user study, we found that access to Merlin increased task accuracy by an average of 3.8* and simultaneously reduced the time for programmers to complete all tasks by 31%.
