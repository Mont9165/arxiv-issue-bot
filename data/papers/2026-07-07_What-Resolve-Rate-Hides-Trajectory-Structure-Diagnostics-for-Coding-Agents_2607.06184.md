# What Resolve Rate Hides: Trajectory Structure Diagnostics for Coding Agents

- arXiv ID: `2607.06184v1`
- Authors: Rui Shu, Chun Yong Chong, Xin Zhou, Yun Peng, Zihan Wu, Xu Han, Zeyang Zhuang, Guowen Yuan, Yuan Wang
- Published: 2026-07-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.06184v1) | [pdf](https://arxiv.org/pdf/2607.06184v1)

## Abstract

Coding agents are ranked almost entirely by resolve rate: whether their final patch passes the target tests. Yet two agents can reach the same outcome through very different processes, and a single pass/fail label says nothing about why a run failed or why an accepted run spent extra steps, time, or tokens. This process evidence lives in the trajectory, which records a run's searches, reads, edits, tool calls, validation, and reversions. However, raw traces are heterogeneous and hard to compare across runs. We present TraceProbe, a trajectory-diagnostic framework that recovers what resolve rate hides. TraceProbe normalizes each raw run into a canonical nine-type action taxonomy with deterministic effect labels, then applies two rule-based modules: Insight names single-trajectory anti-patterns adapted from established debugging practice (e.g., search loops, verification skips), while Converge aligns pairs of runs and classifies where their behavior diverges under controlled references. Applying TraceProbe to 2,500 trajectories from five production settings on SWE-Bench Verified, we find that (i) file choice is too coarse to separate success from failure, whereas function selection and completion behavior localize it; (ii) Insight anti-patterns act mainly as corpus-level difficulty clues, with search loops the most stable; and (iii) even resolved runs differ in how quickly they reach relevant code and how much failed work they incur. Trajectory structure thus adds auditable diagnostic context to outcomes by localizing inspection targets, suggesting failure hypotheses, and prioritizing runs for review.
