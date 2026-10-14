# Measuring the Unmeasurable: Markov Chain Reliability for LLM Agents

- arXiv ID: `2604.24579v1`
- Authors: Phat T. Tran-Truong, Xuan-Bach Le
- Published: 2026-04-27
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.24579v1) | [pdf](https://arxiv.org/pdf/2604.24579v1)

## Abstract

Large language model (LLM) agents increasingly operate as sequential software systems, but their reliability is often summarized by scalar benchmark metrics. Metrics such as pass$@k$, pass$^k$, and the reliability decay curve (RDC) are useful summaries, but they do not identify the success-time distribution being estimated, test whether traces support that distribution, or quantify finite-trace uncertainty. We present \textsc{TraceToChain}, a reproducible pipeline that fits agent execution traces to an absorbing discrete-time Markov chain (DTMC), $\hat M=(\hat Q,\hat R_\oplus,\hat R_\ominus)$, with explicit diagnostics and uncertainty. The pipeline builds an automatic cluster taxonomy, estimates transitions with Laplace-smoothed maximum-likelihood estimation (MLE), checks fit with a composite Akaike information criterion (AIC) and Kolmogorov--Smirnov (KS) goodness-of-fit certificate, and reports Dirichlet-posterior credible intervals and non-parametric bootstrap intervals. We adapt classical reliability mathematics (Kemeny--Snell~\cite{kemenysnell}, Cheung~\cite{cheung1980}, Goel--Okumoto~\cite{goelokt}) to agent traces. The resulting first-passage view reconciles metrics usually reported separately: pass$@k$, pass$^k$, and the RDC are projections of one success-time distribution. On seven controlled MAST-style frameworks with a strict 50/50 fit/test protocol, held-out empirical RDCs overlay their analytic counterparts with max $L_\infty^{\mathrm{RDC}} = 0.053$ (median $0.048$). A two-sample KS test on the first-passage cumulative distribution function (CDF) accepts the fitted chain with $p>0.05$ on $7/7$ frameworks (min $p = 0.78$), and per-entry $95\%$ posterior and bootstrap intervals agree to $\approx\!0.01$ at the median.
