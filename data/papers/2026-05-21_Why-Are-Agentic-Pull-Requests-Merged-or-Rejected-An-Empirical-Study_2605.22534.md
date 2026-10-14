# Why Are Agentic Pull Requests Merged or Rejected? An Empirical Study

- arXiv ID: `2605.22534v1`
- Authors: Sien Reeve O. Peralta, Fumika Hoshi, Hironori Washizaki, Naoyasu Ubayashi, Inase Kondo, Yoshiki Higo, Hiroki Mukai, Norihiro Yoshida, Kazuki Kusama, Hidetake Tanaka, Youmei Fan
- Published: 2026-05-21
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.22534v1) | [pdf](https://arxiv.org/pdf/2605.22534v1)

## Abstract

AI coding agents increasingly submit pull requests (Agentic-PRs) to open-source repositories, yet their performance is commonly assessed using merge and rejection outcomes alone. We hypothesized that these outcome labels do not reliably reflect agent capability without considering review interactions. To test this, we conducted a decision-oriented analysis of 11,048 closed Agentic Pull Requests, refined to 9,799 human-reviewed PRs, and manually inspected 717 representative cases to recover decision rationale from interaction artifacts. We found that rejection outcomes substantially overstate agent error: only 35.7% of rejected PRs reflected clear agentic failures, while 31.2% were driven by workflow constraints and 33.1% lacked observable decision rationale. Among merged PRs, 15.4% required explicit reviewer involvement through feedback or direct commits, and 5.5% showed no visible interaction trace. We further observed systematic differences across agents, with Copilot and Devin more often embedded in reviewer-mediated workflows, while Codex and Cursor PRs were typically merged with minimal interaction. These results reject the assumption that PR outcomes alone capture agent performance and demonstrate the need for interaction-aware evaluation grounded in review behavior.
