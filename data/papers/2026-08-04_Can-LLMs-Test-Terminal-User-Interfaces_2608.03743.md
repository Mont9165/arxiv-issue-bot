# Can LLMs Test Terminal User Interfaces?

- arXiv ID: `2608.03743v1`
- Authors: Chao Peng, Ruida Hu, Ajitha Rajan, Tegawendé F Bissyandé, Jacques Klein, Cuiyun Gao
- Published: 2026-08-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2608.03743v1) | [pdf](https://arxiv.org/pdf/2608.03743v1)

## Abstract

Terminal User Interfaces (TUIs) combine the stateful, screen-oriented behaviour of GUIs with terminal deployment and are now common in developer tools. Yet they lack a dedicated testing methodology. We survey 197 real-world TUI applications: only 12% of test code exercises the interface, and 45% of those tests never send input, checking a static frame instead. We turn these applications into a headless benchmark spanning ratatui/Rust, bubbletea/Go, textual/Python, and ink/TypeScript, packaging each as an instrumented Docker image. We record line and widget coverage where reliable, rendered terminal states, and crashes. Under equal wall-clock budgets, we compare four frontier LLMs with random exploration. No model dominates. Random is a strong time-budgeted baseline, but its crash advantage comes from higher throughput: per interaction, LLM guidance is more efficient and uniquely reaches input-gated faults. Automatically deriving launch inputs yields the largest practical gain, enabling applications that otherwise never start. Line coverage poorly predicts crash discovery, weakening it as a proxy for test effectiveness. Automated TUI testing is feasible but far from solved, and honest baselines matter more than model choice. We release the coverage tool tuicov at https://github.com/tui-testing/tuicov and the testing framework tuibot at https://github.com/tui-testing/tuibot.
