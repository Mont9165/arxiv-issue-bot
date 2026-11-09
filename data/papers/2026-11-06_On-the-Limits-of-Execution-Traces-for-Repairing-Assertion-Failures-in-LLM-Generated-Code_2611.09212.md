# On the Limits of Execution Traces for Repairing Assertion Failures in LLM-Generated Code

- arXiv ID: `2611.09212v1`
- Authors: Muntasir Adnan, Carlos C. N. Kuhn
- Published: 2026-11-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2611.09212v1) | [pdf](https://arxiv.org/pdf/2611.09212v1)

## Abstract

Iterative repair returns a failed program's error to a large language model (LLM) and asks it to fix it. After iterative repair, the remaining failures are mostly assertion failures: with four Qwen2.5 models, they make up 79% of residual failures on BigCodeBench, all on HumanEval and 93% on LiveCodeBench. We argue, through an information view of the feedback, that an assertion failure says little about where the fault lies. We propose Breakpoint Debugging (BPD), which returns the failed program annotated inline with its variables' runtime values. We take the tasks that iterative repair failed to fix with five repair attempts and compare two ways of spending five further generations on them: BPD, and resampling. On BigCodeBench, BPD repairs 26.7% of these tasks against 22.4%, and its advantage grows with model size. On HumanEval, BPD outperforms resampling but only slightly, and on LiveCodeBench, fresh sampling repairs more (6.5% against 4.9%). Furthermore, BPD reduces unchanged-code resubmissions from 28% to 8% on BigCodeBench. Using only the first failing test's trace, it outperforms tracing all failing tests while using fewer tokens than both all-trace BPD and plain iterative repair. On LiveCodeBench, BPD gives no gain even on the public tests, so a visible failing input is not enough for a trace to help. These results match the information view: a trace helps only when the test exposes a failing input, and the fault is an implementation slip; otherwise, a repair loop should resample rather than trace.
