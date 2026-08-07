# Where Does Agent Reliability Come From? A Cross-Benchmark Decomposition of Verification Loops, Specialist Models, and Scaffolding in a Production Enterprise Agent

- arXiv ID: `2607.17044v1`
- Authors: Arunabh Dastidar
- Published: 2026-07-19
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.17044v1) | [pdf](https://arxiv.org/pdf/2607.17044v1)

## Abstract

Multi-step enterprise agent tasks fail in a characteristic way: single-pass inference has no checkpoint between deciding an answer and committing to it. We study one production system (Leni) whose architecture installs such checkpoints: verification loops (execute, observe, compare, correct) staffed by lightweight task-specialized post-trained models. We evaluate the unmodified production configuration on three public benchmarks stressing distinct failure modes: SpreadsheetBench Verified (silent computation error), BullshitBench v2 (premise confabulation), and the GAIA validation split (cascade error over long tool chains). The full system improves over its frontier base model by +11.0 percentage points on SpreadsheetBench (91.25% vs 80.25%, n=400, p<0.001), +7 to +10 percentage points on BullshitBench (98% vs 91%, n=100), and roughly +15 points on GAIA validation (75.2% pass@1, n=165; 83.0% best-of-k). Our central contribution is a decomposition of that uplift: most of it comes from scaffolding, routing, and specialist models rather than from the verification step itself, whose isolated contribution is small (+1.5 points) but concentrated at the top of the score distribution, where it converts otherwise-failing tasks. We instrument the loop end-to-end, yielding an empirical verifier confusion matrix (catch rate about 0.20, fix rate 0.75, no false-alarm regressions) that grounds a compounding-reliability model. Specialist-swap ablations suggest that the loop's value depends on who observes it: replacing the small trained verifier with the generating frontier model eliminates most rescues. A valid-premise control shows zero over-rejections in 100 expert-level questions.
