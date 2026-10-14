# Long-Range Correlation in Code Commit Dynamics as a Novel Indicator of Software Product Stability: A Detrended Fluctuation Analysis Study

- arXiv ID: `2605.03574v1`
- Authors: Goran Mitevski
- Published: 2026-05-05
- Primary category: `physics.soc-ph`
- Categories: `physics.soc-ph`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.03574v1) | [pdf](https://arxiv.org/pdf/2605.03574v1)

## Abstract

This work proposes the fractal scaling exponent alpha, estimated via Detrended Fluctuation Analysis (DFA) on the unaggregated time series of lines of code added per commit event in a software repository, as a novel process-level indicator of software product stability. The proposal rests on the hypothesis that stable software products arise from development processes characterised by long-range temporal correlations in commit behaviour: each code addition is shaped not only by the immediately preceding commits but by patterns extending weeks or months into the past and anticipating work to be done in the future. This hypothesis is tested on two non-overlapping 712-day time series of lines of code added per commit event, drawn from a closed-source software organisation and labeled as stable and unstable by the lead engineer on the basis of crash-analytics data. Applied to these series, DFA yields alpha = 0.70 (n_min = 16) for the stable period and alpha = 0.57 for the unstable period, with all estimates substantially above the shuffled-surrogate baseline (alpha ~= 0.50 +/- 0.01). Results are robust to three parameterisations (n_min in {4, 16, 48}) and validated against 1,000 surrogate time series per condition. Remarkably, the unstable period generated 3.2 times more commit events than the stable period, yet exhibited lower long-range memory, demonstrating that commit volume alone does not predict stability, and that the temporal organisation of development activity is the key variable. This result can be situated in the broader literature on fractality in human creative production, discuss methodological limitations, and outline a research programme for deploying alpha as a continuous code-health indicator in version-control pipelines.
