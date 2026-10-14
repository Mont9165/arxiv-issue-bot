# AgentSpy: Making AI Agent Behavior Observable

- arXiv ID: `2610.06001v1`
- Authors: Christoph Bühler, Matteo Biagiola, Luca Di Grazia, Guido Salvaneschi
- Published: 2026-10-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.06001v1) | [pdf](https://arxiv.org/pdf/2610.06001v1)

## Abstract

AI agents built on large language models (LLMs) run shell commands, read and write files, and reach the network, typically with their user's privileges. However, what an agent does during an execution is difficult to understand: tests assert on the result, and the agent's trajectory records only what the agent reports about itself, which may omit behavior executed by its subprocesses. We present AgentSpy, an approach that observes an agent from outside the agent. AgentSpy runs the agent in an isolated environment, configured by a declarative specification, and records the system calls and network traffic of the agent and of every process it executes. Based on this monitoring, AgentSpy supports two families of analyses: conformance analyses, which measure obligations, i.e., what an agent execution should do, and safety analyses, which check prohibitions, i.e., what an agent execution must never do. We instantiate one analysis of each family. The reliability analysis uses rules to summarize each run by the environment resources the agent uses: the commands it executed, the files it accessed, and the hosts it contacted. The security analysis applies deterministic rules to the system calls of an execution. For reliability, we evaluated AgentSpy on 77 tasks with the codex harness and three recent LLMs, executing each task three times. Sets of repeated runs of the same task are more similar than sets that include runs of another task in 92.2% of the comparisons. Among tasks for which all three runs pass outcome-based tests, the agent performs task-unrelated activities in 18% of the cases, reads the grading files in 7%, and does not use the developers' guidance in 17%. For security, the generic rules of AgentSpy detect four of five attack categories we considered, with no false positives across 50 runs.
