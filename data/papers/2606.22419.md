# Knowledge-Graph Grounding Helps LLMs Only for Out-of-Training Knowledge: A Controlled Study on Clinical Question Answering

- arXiv ID: `2606.22419v1`
- Authors: Madhulatha Mandarapu, Sandeep Kunkunuru
- Published: 2026-06-21
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.22419v1) | [pdf](https://arxiv.org/pdf/2606.22419v1)

## Abstract

A recent Nature Medicine study reports that general-purpose frontier LLMs outperform specialized retrieval-augmented clinical tools on medical benchmarks, and that retrieval can hurt strong models. We ask the natural follow-up: does structured knowledge-graph (KG) grounding change this, and when does grounding help at all? We contribute two results. First, a reproduction: the study's headline HealthBench score (~88) is the Consensus variant, not full HealthBench, where frontier models and ideal completions both score ~46-47 under a physician-calibrated grader (agreement 82.5%); we reproduce GPT-5.2 Consensus =90.9 and flag a score-deflating grader bug. Second, a knowledge-boundary result. Using a graph+vector engine (samyama-graph) over the public biomedical KG PrimeKG, neither naive triple retrieval nor an agentic natural-language-to-Cypher loop (82% successful queries) improves MedQA across a weak-to-strong model ladder (all |Delta| <= 3.4). On a synthetic counterfactual KG, and on a hybrid benchmark mixing known and novel facts, the identical pipeline lifts out-of-training accuracy from chance to ~100% (+68 to +79) while adding nothing on known facts (a no-LLM arm answers both). Across three regimes (no-knowledge, graph-aided, hybrid), grounding helps only insofar as the decisive fact lies outside the model's training -- public-KG facts are redundant, private and novel data are where it pays -- matching the study's institutional-data caveat.
