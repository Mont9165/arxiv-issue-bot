# Benchmarking Mythos-Linked Bug Rediscovery

- arXiv ID: `2605.17416v1`
- Authors: Isaac David, Arthur Gervais
- Published: 2026-05-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.17416v1) | [pdf](https://arxiv.org/pdf/2605.17416v1)

## Abstract

Anthropic's April 2026 Mythos materials combine benchmark claims with concrete bug-finding stories across OpenBSD, FreeBSD, Linux, FFmpeg, and browsers. This paper reports a controlled target-file rediscovery experiment on six public or high-confidence Mythos-linked systems tasks. Each model receives the same target file or files, read-only source tools, three repeats per task, and one manual target-matching rubric; prompts omit CVE identifiers, patch hashes, advisory text, author names, disclosure dates, and answer key root cause language. The experiment contains 54 counted model-task attempts: three models, six tasks, and three repeats, giving 18 attempts per model. GPT-5.5 xhigh achieves 5/18 target rediscoveries, covering 2/6 tasks; counting one wrong-target mpegts.c finding separately gives 3/6 distinct core bugs. Claude Opus 4.7 achieves 1/18 target rediscoveries, covering 1/6 tasks. Kimi K2 records 0/18 target rediscoveries. The dominant failure mode is early commitment to plausible alternate candidates within the assigned file: models often submit source-grounded hypotheses while missing the specific invariant corrected by public Mythos patch evidence. These results do not refute Anthropic's undisclosed workflow, but show that under this favorable target-file scaffold, systems-specific prompting yields only six target matches across 54 counted attempts.
