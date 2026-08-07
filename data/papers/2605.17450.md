# ContraFix: Agentic Vulnerability Repair via Differential Runtime Evidence and Skill Reuse

- arXiv ID: `2605.17450v1`
- Authors: Simiao Liu, Fang Liu, Li Zhang, Yang Liu, Yinghao Zhu
- Published: 2026-05-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CL`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2605.17450v1) | [pdf](https://arxiv.org/pdf/2605.17450v1)

## Abstract

Large language model (LLM) agents are increasingly used for automated vulnerability repair (AVR), where repository-level reasoning enables them to inspect context and produce source-code patches. However, recent empirical results show that these agents still struggle with real-world vulnerabilities. Their main failure mode is semantic misunderstanding: choosing a repair direction that does not match the root cause. We identify two reasons for this gap. Existing agents usually reason from the failing execution alone. A crash report can pinpoint where the program failed, but it does not reveal which variable or state transition, among many candidates near the fault site, separates the crashing behavior from safe execution. As a result, agents often produce symptom-oriented patches instead of causal fixes. Moreover, evidence collected for one vulnerability is rarely retained, so similar cases in later repositories must be diagnosed again from scratch. We present ContraFix, an agentic AVR framework that couples differential runtime evidence with reusable repair skills. Its Mutator constructs PoC variants that straddle the failure boundary; its Analyzer inserts state probes around the fault region and summarizes divergences between crashing and non-crashing executions into a repair specification; and its Patcher converts the specification into verified source patches. Each successful repair updates a two-track skill base containing repair specifications and mutation strategies, which are retrieved through a three-tier policy for future instances. On SEC-Bench (C/C++, 200 instances) and PatchEval (Go, Python, JavaScript, 225 instances), ContraFix with GPT-5-mini resolves 84.0% and 73.8% of the tasks, respectively, achieving state-of-the-art performance on both benchmarks while costing less than one-third of the strongest comparable baseline.
