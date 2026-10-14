# Truly Sub-$3^n$ Min-Sum Subset Convolution and Join Ordering

- arXiv ID: `2610.10282v1`
- Authors: Mihail Stoian
- Published: 2026-10-07
- Primary category: `cs.DS`
- Categories: `cs.DS`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.10282v1) | [pdf](https://arxiv.org/pdf/2610.10282v1)

## Abstract

We present a deterministic reduction from min-sum subset convolution to min-plus matrix product. We show that if the min-plus product of two $D\times D$ matrices with $β$-bit integer entries can be computed in $D^{3-δ}\operatorname{poly}(β,\log D)$ time for a fixed rational $0<δ<1$, then min-sum subset convolution on an $n$-element universe can be solved in $(2+2^{-δ})^n 2^{O(\sqrt n\log(n+1))}\operatorname{poly}(n,β)$ time. Instantiating this reduction with the recent breakthrough on subcubic min-plus matrix product by Alman and Vassilevska Williams gives a Las Vegas algorithm with expected running time $O^*(2.9987^n)$ and a deterministic algorithm with running time $O^*(2.9997^n)$, strictly breaking the longstanding $3^n$ computational barrier. Notably, these speedups translate directly to database query optimization, yielding the same expected and deterministic running-time bounds for join ordering under the $C_{\mathrm{out}}$ cost function.
