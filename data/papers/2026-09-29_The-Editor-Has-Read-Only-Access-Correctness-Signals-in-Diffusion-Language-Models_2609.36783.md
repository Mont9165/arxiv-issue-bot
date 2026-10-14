# The Editor Has Read-Only Access: Correctness Signals in Diffusion Language Models

- arXiv ID: `2609.36783v1`
- Authors: Angad Miglani, Samrath Singh Chadha, Kevin Li, Manas Venkata Sai Ravulapalli
- Published: 2026-09-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.36783v1) | [pdf](https://arxiv.org/pdf/2609.36783v1)

## Abstract

Diffusion language models generate code by repeatedly updating a partially masked sequence. We ask whether their internal activations encode code correctness and whether that information can improve generation. Across six diffusion models, linear probes distinguish passing from failing attempts, with the strongest reads generally appearing beyond the early layers. Controls using small semantic mutations support a connection to correctness rather than surface style alone. In comparisons with model confidence, probe point estimates offer no consistent advantage. Adding a probe-derived direction to the residual stream does not yield a dependable improvement in the tested steering settings, while the opposite direction degrades performance. We distinguish these observations from claims about statistical significance or a general inability to steer. Supplementary methods, archived results, and code document the tested interventions and the limits of their statistical calibration and reproducibility.
