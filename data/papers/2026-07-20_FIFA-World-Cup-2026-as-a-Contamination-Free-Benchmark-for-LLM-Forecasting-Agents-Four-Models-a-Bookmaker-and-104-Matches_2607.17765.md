# FIFA World Cup 2026 as a Contamination-Free Benchmark for LLM Forecasting Agents: Four Models, a Bookmaker, and 104 Matches

- arXiv ID: `2607.17765v1`
- Authors: Jiacheng Ding, Cong Guo, Jason Xu
- Published: 2026-07-20
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.17765v1) | [pdf](https://arxiv.org/pdf/2607.17765v1)

## Abstract

We introduce WC2026-Agents, a benchmark and dataset for evaluating large language models (LLMs) as autonomous forecasting agents on real, future events. For every one of the 104 matches of the 2026 FIFA World Cup, four frontier models -- Claude Opus 4.8, ChatGPT (GPT-5.5, high reasoning), Gemini 3.1 Pro, and Grok (Expert Mode) -- ran an identical search-act-reflect loop: gather evidence with a web tool, commit to a 1X2 (team-A win / draw / team-B win) distribution and a virtual 100-USD bet, and, after the match, reflect given only the final score. Because every match kicked off after the models' training cutoffs, the benchmark is contamination-free by construction. Crucially, we pair the four agents with a fifth competitor drawn from the same information environment -- the pre-match betting market -- collected as per-match 1X2 odds, giving an economically grounded baseline and letting us score not just what an agent predicts but what it does with money. The release contains 416 forecasts and 414 reflections with verbatim reasoning, ground truth (including penalty shootouts), odds, and a reproducible evaluation suite. A reference evaluation surfaces findings that raw accuracy hides: the four agents issue an identical top pick in 92% of matches and none beats the market's Brier score; indeed, a naive flat stake on the market favorite out-earns all four agents. Yet the agents diverge sharply as decision-makers: betting return-on-investment ranges from -18% to +10%, fading the market is unprofitable for all four, the share of forecasts that cite the market ranges from 12% to 100%, and self-reported error rates on wrong picks range from 36% to 86%. The benchmark thus measures calibration, decision quality, and self-knowledge -- axes on which frontier models differ even when their predictions do not. Data and code: https://github.com/graphuofm/FIFA2026LLM
