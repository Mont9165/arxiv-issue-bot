# Compared to What? A Human-Anchored Security Benchmark for LLM-Generated Infrastructure-as-Code

- arXiv ID: `2608.28021v1`
- Authors: Animesh Shaw
- Published: 2026-08-28
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`, `cs.MA`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.28021v1) | [pdf](https://arxiv.org/pdf/2608.28021v1)

## Abstract

Large language models are increasingly used to author Infrastructure-as-Code (IaC), where a single insecure default can be deployed directly into production. Prior evaluations report raw vulnerability counts for model-generated IaC, but without a human baseline they cannot determine whether models are actually worse than engineers. We introduce GenIaC-SecBench, a benchmark of 100 deployment scenarios stratified by architectural complexity, evaluated across 12 model configurations from four vendors, producing 1,196 IaC artifacts scanned by three independent policy engines (Checkov, Trivy, KICS). Critically, we also scan 634 human-authored IaC templates with the same toolchain, providing the first size-matched human security baseline.
  Vulnerability density is strongly inverse to artifact size (Spearman $ρ= -0.55$, $p < 10^{-77}$), meaning unmatched comparisons measure size rather than security. When matched on declared-resource count, all model configurations fall within 3.21x--3.87x the human vulnerability density, with the gap widening for simpler tasks (4.9x at one resource, 1.4x at twenty or more).
  We decompose reasoning into standard generation, prompt-engineered chain-of-thought, and vendor extended-thinking APIs. Vendor extended thinking significantly outperforms prompted chain-of-thought ($-12.0\%$, $p = 0.0013$), while prompted chain-of-thought is indistinguishable from standard generation ($-1.3\%$, n.s.). Token instrumentation shows extended thinking uses under 1\% of the output budget, explaining its bounded effect.
  Two negative results also emerge: deployability does not correlate with vulnerability ($r = 0.158$, $p = 0.625$), and classical complete-case Friedman testing is infeasible for realistic benchmark designs, motivating the Skillings-Mack statistic. All code, data, and regeneration scripts are released.
