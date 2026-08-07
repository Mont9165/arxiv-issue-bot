# AgentPulse: A Continuous Multi-Signal Framework for Evaluating AI Agents in Deployment

- arXiv ID: `2604.24038v1`
- Authors: Yuxuan Gao, Megan Wang, Yi Ling Yu
- Published: 2026-04-27
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.24038v1) | [pdf](https://arxiv.org/pdf/2604.24038v1)

## Abstract

Static benchmarks measure what AI agents can do at a fixed point in time but not how they are adopted, maintained, or experienced in deployment. We introduce AgentPulse, a continuous evaluation framework scoring 50 agents across 10 workload categories along four factors (Benchmark Performance, Adoption Signals, Community Sentiment, and Ecosystem Health) aggregated from 18 real-time signals across GitHub, package registries, IDE marketplaces, social platforms, and benchmark leaderboards. Three analyses ground the framework. The four factors capture largely complementary information (n=50; $ρ_{\max}=0.61$ for Adoption-Ecosystem, all others $|ρ| \leq 0.37$). A circularity-controlled test (n=35) shows the Benchmark+Sentiment sub-composite, which contains no GitHub-derived signals, predicts external adoption proxies it does not aggregate: GitHub stars ($ρ_s=0.52$, $p<0.01$) and Stack Overflow question volume ($ρ_s=0.49$, $p<0.01$), with VS Code installs ($ρ_s=0.44$, $p<0.05$) reported as illustrative given that only 11 of 35 agents have non-zero installs. On the n=11 subset with published SWE-bench scores, composite and benchmark-only rankings are nearly uncorrelated ($ρ_s=0.25$; 9 of 11 agents shift by at least 2 ranks), driven by a strong negative Adoption-Capability correlation among closed-source high-capability agents within this subset. This is precisely why we rest the framework's validity claim on the broader n=35 test rather than the SWE-bench overlap. AgentPulse surfaces deployment signal absent from benchmarks; it is a methodology, not a ground-truth ranking. The framework, all collected signals, scoring outputs, and evaluation harness are released under CC BY 4.0.
