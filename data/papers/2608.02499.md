# SWE-Touch: Benchmarking Coding Agents When Users Touch the Code

- arXiv ID: `2608.02499v1`
- Authors: Yuqiao Tan, Jinxiang Meng, Fangyu Lei, Minzheng Wang, Shizhu He, Jun Zhao, Kang Liu
- Published: 2026-08-03
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2608.02499v1) | [pdf](https://arxiv.org/pdf/2608.02499v1)

## Abstract

Real-world software development requires coding agents to operate in shared workspaces where users may inspect and modify code during an ongoing task, yet existing repository-level benchmarks typically evaluate agents working alone or restrict user participation to messages. This leads us to ask: how do coding agents understand and respond to code changes in a shared workspace? We introduce SWE-Touch, a framework that stress-tests this setting through validated Counter-Edits: plausible edits to task-relevant code that conflict with task completion. SWE-Touch mines task-critical regions from multiple repair trajectories, uses a separate User Patch Generator to construct the edits, and injects them with contextual user messages when agents reach the relevant code. We evaluate nine coding models on SWE-bench Verified, with additional experiments on longer-horizon tasks from SWE-Bench Pro and DeepSWE. Counter-Edit lowers average resolve rate by 7.7 percentage points on SWE-bench Verified, with degradation also persisting on both longer-horizon benchmarks. Trajectory analysis links these failures to limited awareness of the evolving workspace: agents may retain conflicting code or replace it without sufficiently re-inspecting the repository and validating the revised code with targeted tests. These findings show that strong autonomous performance does not yet ensure the state awareness and adaptive behavior needed for shared-workspace collaboration, and point to detecting workspace changes, reconciling conflicting edits with the task, and verifying the affected behavior as key capabilities for future optimization.
