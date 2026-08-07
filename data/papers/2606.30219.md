# EvalSafetyGap: A Hybrid Survey and Conceptual Framework for LLM Evaluation-Safety Failures

- arXiv ID: `2606.30219v1`
- Authors: Buğra Alperen Uluırmak, Rifat Kurban
- Published: 2026-06-29
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.30219v1) | [pdf](https://arxiv.org/pdf/2606.30219v1)

## Abstract

LLM evaluation and AI safety face a shared measurement problem: benchmark scores, reward-model signals, and reported safety metrics can improve while the latent properties they are meant to represent remain difficult to verify. This paper combines a hybrid survey - a systematic search paired with narrative synthesis and separately tracked grey evidence - with a conceptual framework and a structured ten-model audit. The synthesis spans eight evidence streams: benchmark validity, dynamic evaluation, LLM-as-judge reliability, safety evaluation, jailbreak/refusal robustness, reward hacking, mechanistic interpretability, and governance/auditability, covering 2018-2026 evaluation-safety measurement work. We introduce EvalSafetyGap as an organizing hypothesis for comparing evaluation-side and alignment-side proxy failures under optimization pressure, using Goodhart's Law together with two constructs we develop here - an Instability Decomposition and an Alignment Trilemma - as tools for generating testable comparisons. The audit shows how conclusions shift when capability, behavioral safety, and governance are measured separately. In this sample (n = 10), the association between capability and sustained adversarial robustness is statistically indeterminate using the displayed Table 3 inputs (Pearson r = +0.232, p = 0.520), and the apparent open-closed safety gap is modest, driven mainly by governance and disclosure rather than behavioral robustness, and sensitive to how a single borderline model is classified; attempt-budget results are protocol dependent. Because the public evidence uses heterogeneous protocols, the audit is diagnostic rather than rank-generating. The contribution is a shared vocabulary and evidence map to support dynamic evaluation, transparent source reporting, multi-attempt safety measurement, and auditable alignment practice.
