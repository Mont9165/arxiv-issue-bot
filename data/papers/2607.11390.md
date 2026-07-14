# TerraRepair: A Tool-Grounded LLM Agent for Infrastructure-as-Code Repair

- arXiv ID: `2607.11390v1`
- Authors: Minase Mekete Mengistu, Juri Di Rocco, Phuong T. Nguyen, Davide Di Ruscio
- Published: 2026-07-13
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.11390v1) | [pdf](https://arxiv.org/pdf/2607.11390v1)

## Abstract

Background: Infrastructure-as-Code (IaC) scanners detect cloud misconfigurations in Terraform and other IaC languages before deployment, but repairing the flagged configurations remains largely manual. Recent Large Language Model (LLM)-based repair approaches can repair some findings, but may hallucinate unsupported constructs or suppress warnings without fixing the issue. Aims: We study whether tool grounding can improve LLM-based Terraform repair, and when a finding should be escalated because the required deploymnet-specific context is not availble. Method: We present TerraRepair, a prototype of a tool-grounded LLM agent for Terraform repair with structured escalation. TerraRepair retrieves dependency context from Terraform references, consults the installed provider schema, and re-runs the scanner before returning a candidate repair. Then teh required context is absent, TerraRepair escalates instead of fabricating a plausible fix. Results: We evaluate our tool on two vulnerable-by-design Terraform repositories using two IaC security scanners, Checkov and Trivy, across AWS, Azure, and GCP. On the combined AWS benchmark, TerraRepair improves scanner-verified fix rates from 26.6% to 78.4% on Checkov and from 44.8% to 72.4% on Trivy, compared with a controlled one-shot baseline. It repairs are labelled as correct under a majority-vote protocol. Conclusions: These emerging results show that tool grounding can substantially improve scanner-verified LLM-based IaC repair on the studied benchmarks, while missing deployment-specific context remains the main knowledge boundary for full autonomy.
