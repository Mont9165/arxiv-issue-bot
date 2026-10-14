# TTHE: Test-Time Harness Evolution

- arXiv ID: `2607.08124v1`
- Authors: Jun Nie, Yonggang Zhang, Jun Song, Qianshu Cai, Dahai Yu, Yike Guo, Xinmei Tian, Bo Han
- Published: 2026-07-09
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2607.08124v1) | [pdf](https://arxiv.org/pdf/2607.08124v1)

## Abstract

The behavior of an LLM agent is determined not only by the underlying model, but also by its harness: the executable program that constructs context, invokes tools, verifies intermediate results, and recovers from failures. Existing approaches optimize such harnesses before deployment, searching training or development data for a fixed agent workflow that is then frozen at test time. This limits adaptation when the test distribution, failure modes, or tool interactions differ from those seen during development. We ask whether the harness can instead be optimized during evaluation itself, using only the unlabeled execution traces the agent produces on the test inputs. We introduce Test-Time Harness Evolution (TTHE), which treats the executable harness as the state of test-time adaptation. During evaluation, TTHE maintains a population of candidate harnesses and refines them through an agentic proposer that reasons over their execution traces, without gold labels or task-specific supervision; a judge then commits an improved harness from execution-derived proxy signals, and the selected program persists to govern subsequent inputs. Crucially, TTHE does not update model weights, require gold labels, or train a separate adaptation model: solver, proposers, and judge are different roles and harnesses around the same frozen LLM, so all adaptation occurs through changes to the surrounding program. Across text-to-SQL, competitive programming, software engineering, data-science coding, and agentic tool-use tasks, TTHE improves fixed ReAct-style baseline harnesses, yielding persistent, inspectable improvements rather than a pre-searched workflow or per-query retries. These results recast test-time adaptation for LLM agents as evolution over executable control programs and identify execution-derived proxy reliability as a central challenge for robust unsupervised agent improvement.
