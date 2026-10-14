# Prefactory: Automated Discovery and Application of Library-Adoption Refactorings

- arXiv ID: `2607.17211v1`
- Authors: Islem Bouzenia, Michael Pradel
- Published: 2026-07-19
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.17211v1) | [pdf](https://arxiv.org/pdf/2607.17211v1)

## Abstract

Replacing hand-written code with library API calls is a common refactoring that can reduce code size, make code more idiomatic, and reuse well-tested implementations. Yet many library-adoption opportunities are hard to find automatically: the original code often does not mention the target library and may resemble the library API only in behavior, with little syntactic overlap. Existing tools, such as linters and static modernizers, cover only a small set of manually specified patterns. LLMs and LLM-based agents, on the other hand, can generalize to more patterns, but they are costly, difficult to reproduce and to apply systematically at scale. This paper introduces Prefactory, an automated approach for library-adoption refactoring in Python. The key idea is to use an LLM to synthesize executable search heuristics rather than relying on repeated LLM prompting over a codebase. Given a target project and a target library name, Prefactory collects library metadata and project vocabulary, then generates lexical and structural detectors. Prefactory executes the detectors during a scan phase to find candidate functions. It then heuristically ranks the candidate functions, generates refactorings for the highest-ranked ones using an LLM, and validates the results with project tests and newly generated differential tests. We evaluate Prefactory on PrefactoryBench, a benchmark of 100 real-world library-adoption refactorings from 61 open-source Python projects and 18 libraries. Prefactory detects 75 instances at the file level and 56 at the function level, compared with 35 and 32 for the strongest baseline (Codex CLI). From the 56 detected functions, Prefactory produces 40 test-validated refactorings.
