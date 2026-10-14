# A Deterministic Control Plane for LLM Coding Agents

- arXiv ID: `2606.26924v1`
- Authors: Padmaraj Madatha
- Published: 2026-06-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2606.26924v1) | [pdf](https://arxiv.org/pdf/2606.26924v1)

## Abstract

LLM coding harnesses grant agents broad file and shell access, yet the configuration layer that steers them -- rules files, agent definitions, IDE-specific markdown -- is largely unmanaged. A prevalence study of 10,008 public GitHub repositories (n=6,145 agent config files) finds that agent configurations propagate as undeclared shared components: 10.1% of tracked paths are SHA-256 exact duplicates across independent repositories (fork-adjusted, threshold-independent), with 75.5% of clone pairs crossing organisational boundaries. Two further patterns are indicative: configurations are rarely revised (58% single-commit; 0.4 vs 0.6 commits/month age-normalised against CI/CD workflows), and rarely declare permission boundaries (<1% of agent configs vs 33% of Actions workflows, n=31 true positives).
  We propose a deterministic control plane above the harness that maps one-to-one to these gaps. Rel(AI)Build treats agent definitions as a managed supply chain (SHA-256 content addressing, HMAC-stamped lockfiles, hash-chained audit logs); enforces tiered permissions and attack-derived blocklists before LLM invocation; gates feature work through a phase state machine with requirement-to-file-to-test traceability; compiles a single canonical definition to seven IDE targets; and detects prompt drift via Jaccard similarity. Conformance tests on injected violations confirm each mechanism enforces its stated invariant; developer outcomes remain future work. Governance of this layer must be deterministic and tool-agnostic -- not delegated to further LLM orchestration.
