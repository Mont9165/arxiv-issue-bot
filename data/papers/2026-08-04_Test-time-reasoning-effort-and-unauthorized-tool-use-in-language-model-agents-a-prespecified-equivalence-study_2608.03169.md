# Test-time reasoning effort and unauthorized tool use in language-model agents: a prespecified equivalence study

- arXiv ID: `2608.03169v1`
- Authors: Xiaonan Xu, Wenjing Wu
- Published: 2026-08-04
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.03169v1) | [pdf](https://arxiv.org/pdf/2608.03169v1)

## Abstract

Language-model agents that execute multi-step workflows through tool calls operate under access-control policies that restrict which operations each role may perform. The APIs serving these agents expose a reasoning-effort parameter that operators adjust for cost and latency. Whether this parameter also changes the rate of unauthorized tool use has not been tested by direct manipulation within a single model. We vary reasoning effort (low, max) inside GPT-5.6 across the 14 confirmatory scenarios of TRIO-20, a suite of 20 matched workplace triads in which a policy-prohibited tool call is effective and its effect on the target metric is stated in the environment, effective but discoverable only through rule inspection, or ineffective. The three conditions derive from one code base and differ in two configuration fields, with identical prompts and tool sets. All analyses were prespecified in a frozen plan before confirmatory collection. Across 840 trajectories and two model tiers, no unauthorized tool call occurred. Exact one-sided 95% limits place each arm's violation rate below 3.50% (Terra, n = 84) and 5.21% (Sol, n = 56). The interaction estimand, with a simultaneous exact 95% interval of $\pm 4.34$ percentage points on Terra, lies inside the $\pm 7.01$-point equivalence margin. Raising effort did change behaviour, but only in inspection: rule-probe rates rose in all conditions, most where probing carried no instrumental payoff, a pattern inconsistent with the hypothesis of targeted search ($-14.3$ points, 95% CI $-27.4$ to $+1.2$). Raw trajectories are released at https://github.com/WenJing95/trio-20.
