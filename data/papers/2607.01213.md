# RepoRescue: An Empirical Study of LLM Agents on Whole-Repository Compatibility Rescue

- arXiv ID: `2607.01213v1`
- Authors: Zhihao Lin, Mingyi Zhou, Zhensu Sun, Yizhuo Yang, Renyu Yang, David Lo, Li Li
- Published: 2026-07-01
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.01213v1) | [pdf](https://arxiv.org/pdf/2607.01213v1)

## Abstract

Open-source libraries and tools are widely reused, but compatibility maintenance is expensive. Once maintainers leave, useful repositories can stop working as runtimes and dependencies evolve. We study whether LLM agents can adapt old repositories to modern environments, a task we call compatibility rescue. Unlike bug repair, compatibility rescue starts from a repository that worked in its original environment but fails after ecosystem drift. RepoRescue gives agents only the repository and its failing modern environment; the agent must diagnose the failure, locate affected code, and produce a source-code rescue that restores the historical test suite. We build RepoRescue from 193 Python and 122 Java repositories, each verified to pass historically and fail after modernization. We evaluate five deployed agent systems on Python and three on Java. Beyond full-patch pass rate, we rerun patches after removing test-file edits to measure source-only repair, add a runtime-enforced regime that blocks test edits, and validate practical use for repositories whose suites pass after rescue. We find that Claude Code systems sometimes edit failing tests even when prompted not to; with runtime blocking, Kimi still rescues 41.5% of repositories. Systems are complementary: their union reaches 62.7%, exceeding the best single system by 10.9 points. Difficulty concentrates in cross-file coordination: on 14 repositories requiring coordinated whole-codebase changes, GPT-5.2 through Codex passes all 14, while every Claude Code system passes at most two. Finally, a passing suite is only an initial signal: among 34 unmaintained Python candidates whose suites pass after rescue, 22 work in realistic scenarios and 12 pass bug-hunt with patches that address the compatibility failure. RepoRescue benchmarks compatibility rescue with source-only auditing, runtime enforcement, practical validation, and reasoning labels.
