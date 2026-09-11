# Can AI Remediate Backend Failures Safely? GuardedAct with Blast-Radius-Aware Sandboxing

- arXiv ID: `2609.11264v1`
- Authors: Wanrong Cai, Tianyu Yu, Shaorui Pi, Xiaoxuan Sun, Wenrui Ma
- Published: 2026-09-10
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.11264v1) | [pdf](https://arxiv.org/pdf/2609.11264v1)

## Abstract

Large Language Models (LLMs) have shown promising capabilities in generating remediation actions for microservice failures. However, directly executing AI-generated repair actions in production risks cascading collateral damage. We propose GuardedAct, a sandbox-first remediation framework that interposes a blast-radius-aware verification layer between the LLM action generator and the production environment. GuardedAct operates in four phases: (1) ingesting a diagnosis report together with the live system topology and recent telemetry, (2) prompting an LLM to produce a ranked list of candidate remediation actions, (3) simulating each action in a lightweight digital-twin sandbox that estimates the blast radius and assigns a risk label, and (4) enforcing a rollback-confidence gate that auto-executes only low-risk actions while escalating high-risk ones for human review. We evaluate GuardedAct on five fault scenarios injected into the DeathStarBench social-network application. Experimental results show that GuardedAct achieves an overall recovery rate of 87.4% while reducing collateral damage by 79.7% relative to direct LLM execution (from 25.6% to 5.2%), at the cost of a modest sandbox-induced increase in mean time to recovery (approximately 8 s). Ablation studies confirm that each component contributes meaningfully to the safety-speed trade-off.
