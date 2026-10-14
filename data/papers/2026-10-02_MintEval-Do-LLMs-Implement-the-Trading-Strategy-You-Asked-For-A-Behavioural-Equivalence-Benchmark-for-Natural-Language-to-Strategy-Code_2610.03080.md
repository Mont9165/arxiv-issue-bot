# MintEval: Do LLMs Implement the Trading Strategy You Asked For? A Behavioural-Equivalence Benchmark for Natural-Language-to-Strategy Code

- arXiv ID: `2610.03080v1`
- Authors: Siyu Wang, Yifan Wang, Yuecheng He
- Published: 2026-10-02
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CL`, `cs.LG`, `q-fin.TR`
- Links: [abs](http://arxiv.org/abs/2610.03080v1) | [pdf](https://arxiv.org/pdf/2610.03080v1)

## Abstract

Large language models are moving from producing trading signals to writing the code that executes them. The failure mode of the second role is silent: generated code runs, a backtest plots, yet the risk logic that the trader described is not the logic being executed. Existing code benchmarks test functional correctness on unit tests and finance benchmarks test forecasting; neither measures whether an implementation behaves like the strategy that was asked for. We introduce MintEval, a benchmark in which reference strategies are generated programmatically from a library of composable building blocks, back-translated into colloquial trader instructions, and re-implemented by the model under test. Generated and reference programs are executed bar by bar on identical market data and frictions, and compared on their actions rather than on code similarity or profit: alpha is differenced away. MintEval v0 contains 800 tasks on BTCUSDT 15-minute data, stratified by an execution-measured state-span complexity tau that is decoupled from description length. Low-cost models reach a mean ActionMatch of at most 0.544 and reproduce at most 0.087 of tasks exactly; on a stratified subset of 200 tasks a frontier model (Claude Opus 5.5) reaches 0.889 and reproduces 0.575 exactly, yet still fails silently on 0.275 of tasks. Given a menu of building blocks, models identify the strategy almost perfectly, yet 79.2% of the implementations whose specification was read correctly diverge on more than 10% of active bars. The LLM judge of a recent strategy-generation benchmark, applied verbatim, accepts every one of these silent failures.
