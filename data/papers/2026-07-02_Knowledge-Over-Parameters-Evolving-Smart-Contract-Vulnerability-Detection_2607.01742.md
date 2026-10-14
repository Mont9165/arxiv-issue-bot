# Knowledge Over Parameters: Evolving Smart Contract Vulnerability Detection

- arXiv ID: `2607.01742v1`
- Authors: Yuqiang Sun, Han Liu, Ying Li, Yiran Zhang, Zong Cao, Ziyun Guo, Yang Liu
- Published: 2026-07-02
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.01742v1) | [pdf](https://arxiv.org/pdf/2607.01742v1)

## Abstract

Smart contract vulnerabilities are predominantly logic bugs whose detection requires structured, step-by-step procedural knowledge of attack patterns and contract semantics. Existing LLM-based methods struggle to generate this knowledge automatically: prompt-based methods rely on manually crafted detection rules, while fine-tuning requires massive labeled datasets that are inherently scarce in this domain. We present EvoVuln, an automated framework that reformulates vulnerability detection as a procedural knowledge evolution problem, synthesizing and refining detection logic using only a minimal number of labeled samples.
  To achieve this, EvoVuln introduces two key mechanisms. First, a Runtime with an Inversion of Control (IoC) architecture compiles detection rules into Executable Policies. This strictly decouples deterministic control flow from LLM semantic reasoning, ensuring faithful logical adherence and producing dense diagnostic telemetry for precise error localization. Second, a two-phase evolution pipeline refines the rule via abductive semantic debugging without any parameter updates: Cold Start bootstraps and stress-tests an initial rule using auto-synthesized corner cases; Few-Shot Evolving then grounds the policy in real-world semantics using only five vulnerable and five safe examples per vulnerability type.
  Evaluated across five real-world vulnerability types, EvoVuln achieves a 71% macro-average F1-score, outperforming all baselines. The evolved procedural knowledge is portable across models: it enables a lightweight, low-cost model to surpass a much larger zero-shot model by 19 percentage points, and transfers to other LLMs without retraining, at a one-time evolution cost under $50.
