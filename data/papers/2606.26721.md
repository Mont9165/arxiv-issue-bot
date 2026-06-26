# Knowledge-Based Pull Requests: A Trusted Workflow for Agent-Mediated Knowledge Collaboration

- arXiv ID: `2606.26721v1`
- Authors: Xinyu Zhang, Weiwei Sun
- Published: 2026-06-25
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.HC`
- Links: [abs](http://arxiv.org/abs/2606.26721v1) | [pdf](https://arxiv.org/pdf/2606.26721v1)

## Abstract

AI coding agents are changing the bottleneck in software collaboration: code is increasingly cheap, while understanding intent, negotiating scope, and governing long-term project responsibility remain costly. This paper proposes \emph{Knowledge-Based Pull Requests} (KPR), a trusted workflow for agent-mediated software collaboration across trust boundaries, including open source, enterprise, vendor, contractor, and customer-driven settings. In KPR, an external collaborator's local code, tests, and cleaned agent interaction trace are treated as knowledge sources rather than as the default merge candidate. Agents distill these sources into a human-confirmed knowledge package and render it into reviewer-facing forms such as design memos, risk checklists, test plans, or implementation briefs. A project-owned inner trusted coding agent then regenerates candidate code inside the receiving project's environment under repository context, engineering conventions, tests, and security policy. KPR therefore separates two decisions that traditional pull requests often collapse: whether the knowledge should enter the project, and whether a particular implementation should be merged. We contribute the KPR workflow, a candidate artifact schema, a cost-accounting view, a collaboration gateway architecture, a minimal controlled simulation pilot over seven merged public pull requests, and an evaluation agenda. The pilot shows that KPR packages can be instantiated from real PR material and stress-tested under description ablation, diff ablation, and synthetic poisoned-patch conditions. We position KPR as an empirically testable workflow: its value depends on whether auditable extraction, transformation, and project-side regeneration reduce the cost of understanding and reworking high-context external changes.
