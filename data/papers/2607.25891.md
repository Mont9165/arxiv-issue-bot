# Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation

- arXiv ID: `2607.25891v1`
- Authors: Stefan Krsteski, Charlotte Meyer, Guillaume Allegre, Tony O'Halloran, Alexandre Sallinen
- Published: 2026-07-28
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.25891v1) | [pdf](https://arxiv.org/pdf/2607.25891v1)

## Abstract

Evaluating AI agents in interactive environments is hindered by fragmented tasks, scaffolds, verifiers, and scoring rules. Existing efforts focus on narrow settings, remain limited in scale, or require costly reruns, leaving much of the empirical record incomparable. We introduce Messier, a unified corpus of 957,253 records that span 30 benchmarks, 714 agents, 11,891 tasks, and 74,205 verifiers. Messier consolidates public benchmark scores and supplements them with five-agent runs across six underrepresented professional and scientific domains, including a recent legal benchmark. Each record is standardized by model, scaffold, environment, task, verifier, and aggregation rule, with SOC/NAICS classifications for occupational and industry analysis. Using this corpus, we show frontier progress is uneven across benchmark types, with "function calling" saturated, "programming" improving the fastest, and "enterprise workflows" remaining the most challenging. Furthermore, counterfactual rescoring shows that strict all-pass aggregation in multi-verifier tasks can obscure progress and artificially alter agent rankings. From these standardized records, we derive capability scales that align with Epoch's Evaluation Capability Index rankings at Spearman \r{ho} = 0.81 and can be specialized by domain, occupation, action space, or verifier type. Messier provides a foundational, reusable infrastructure for agent capability scaling, benchmark auditing, and fine-grained analysis of evaluation failures.
