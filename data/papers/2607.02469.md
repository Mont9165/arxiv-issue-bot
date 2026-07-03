# TestEvo-Bench: An Executable and Live Benchmark for Test and Code Co-Evolution

- arXiv ID: `2607.02469v1`
- Authors: Jiale Amber Wang, Kaiyuan Wang, Pengyu Nie
- Published: 2026-07-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2607.02469v1) | [pdf](https://arxiv.org/pdf/2607.02469v1)

## Abstract

Software tests and code evolve together: a code change should be followed by new or updated tests that record the new software behavior. Yet existing test generation and update benchmarks often isolate the test from the code change, and rely on static metadata that does not verify whether a test is executable or semantically tied to the code change. This makes it difficult to evaluate whether a test automation agent understands how a code change should propagate into the test suite.
  We introduce TestEvo-Bench, a benchmark of test and code co-evolution tasks mined from software repositories, with two tracks: in test generation, the agent shall write new tests to capture the new software behavior; in test update, the agent shall adapt failing existing tests to the changed software behavior. Each task is anchored to a real commit history and packaged with environment configuration to support execution-grounded metrics such as pass rate, coverage, and mutation score. TestEvo-Bench is also a live benchmark: each task records the timestamp of the test and code changes, and new tasks are periodically mined by our automated pipeline, so evaluation can be restricted to tasks postdating a model's training cutoff to reduce data leakage risk. The current snapshot contains 746 test generation and 509 test update tasks, curated from 59,950 candidate co-evolution records across 152 open-source Java projects. We experiment with four state-of-the-art agents that combine strong harnesses (Claude Code, Gemini CLI, and SWE-Agent) with strong foundation models (Claude Opus 4.7 and Gemini 3.1 Pro). Results show that they achieve up to 77.5% success rate on test generation and 74.6% on test update. However, success rate is materially lower on the most recent benchmark tasks and drops significantly under limited per-task cost.
