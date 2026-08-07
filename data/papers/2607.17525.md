# FailureAtlas: A Taxonomy of Failure Modes in Multi-Provider LLM Serving Infrastructure

- arXiv ID: `2607.17525v1`
- Authors: Vishal Pandey, Gopal Singh
- Published: 2026-07-20
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.17525v1) | [pdf](https://arxiv.org/pdf/2607.17525v1)

## Abstract

Multi-provider LLM gateways reverse proxies that route, load-balance, and rate-limit requests across foundation-model APIs have become critical production infrastructure. Yet the failure modes specific to this architectural layer remain undocumented, scattered across issue trackers and post-mortems with no unifying framework. We introduce \fa{}, a two-axis taxonomy that classifies failures by their \emph{origin layer} (Network/Transport, Streaming/Protocol, State/Session, Model~Behavior, Governance/Cost) and their \emph{detectability} (Loud vs.\ Silent). We populate this taxonomy with five verified catalog entries sourced from public bug reports and first-hand stress testing, each accompanied by a mechanistic root-cause analysis. Three entries include standalone reproduction scripts. Our principal finding is that the most operationally severe failures are \emph{silent}: they return HTTP~200, pass every standard health check, and corrupt application state in ways that require semantic-level observability to detect. Two such silent failures a concurrency race condition causing history loss and a streaming index collision corrupting tool-call payloads were discovered first-hand during \cb{} evaluation campaigns.
