# Breaking, Stale, or Missing? Benchmarking Coding Agents on Project-Level Test Evolution

- arXiv ID: `2605.06125v1`
- Authors: Ye Shang, Quanjun Zhang, Haichuan Hu, Chunrong Fang, Liang Xiao, Zhenyu Chen
- Published: 2026-05-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.06125v1) | [pdf](https://arxiv.org/pdf/2605.06125v1)

## Abstract

As production code evolves, the test suite must co-evolve to remain effective. Existing benchmarks for test evolution operate at method-level granularity with pre-paired inputs, bypassing the task of locating affected tests from the full project and excluding the need for new tests entirely. We present TEBench, the first project-level benchmark for test evolution. Given a project repository and a code-changing commit, TEBench requires systems to autonomously identify tests requiring modification, determine where new tests are needed, and produce the corresponding test patch. We construct TEBench through a four-stage pipeline over Defects4J projects, curating 314 task instances from 10 projects with developer-written ground truth. Each instance is annotated with one or more of three evolution types: Test-Breaking (tests that fail), Test-Stale (tests that pass but no longer meaningfully validate updated behavior), and Test-Missing (new tests needed for introduced behavior). We evaluate seven configurations spanning three industrial agent frameworks (Claude Code, Codex CLI, OpenCode) and six base models, alongside a heuristic baseline. All seven configurations converge on an identification F1 of 45.7% to 49.4%, revealing a shared performance ceiling across both frameworks and base models. Test-Stale is the most challenging type, averaging F1 around 36%, since configurations rely on execution failure signals and lack proactive semantic reasoning. On the update task, configurations produce highly executable test modifications whose surface form diverges substantially from ground truth. Trajectory analysis reveals a reactive "execute-fail-fix" loop that succeeds for breaking tests but structurally cannot address stale or missing tests. TEBench is available at https://github.com/iSEngLab/TEBench with a leaderboard at https://tebench-leadership.vercel.app.
