# Dhaani: A Data-Flow-Driven Tool for Greenfield Construction and Brownfield Modernisation

- arXiv ID: `2611.28798v1`
- Authors: Shraddha Surana, Ashwin Srinivasan
- Published: 2026-11-21
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.28798v1) | [pdf](https://arxiv.org/pdf/2611.28798v1)

## Abstract

Large language models can generate plausible code quickly, but an end-to-end prompt leaves developers with little control over decomposition, interfaces, or the assumptions that must survive later revisions. We present Dhaani, a free desktop application for greenfield program construction and brownfield repository modernisation. It makes an annotated data-flow diagram (ADFD) the inspectable contract between intent and implementation. In the greenfield workflow, Build, a user turns natural-language requirements into a typed graph, reviews process specifications and pre/post-conditions, ratifies generated modules, and proceeds in dependency order for Python or .NET (C#). In the brownfield workflow, Migrate uses source inference to recover an ADFD from a Fortran repository, performs target generation in bounded dependency groups, and exposes source-target alignment, generated code, errors, time, token use, and cost. The tool keeps code and artifacts on the user's machine and supports cloud or locally hosted models. Two scientific synthesis case studies produced executable systems where matched low/no-code baselines failed or were substantially less accurate. On 50 open-source Fortran repositories, the migration workflow made all 382 fixed source-oracle probes runnable and passed 327 (85.6%); two direct translation baselines each passed 83 (21.7% of planned probes). Pre-built installers and usage instructions are freely available. Tool and usage guide: https://shraddhasurana.github.io/dhaani/. Video: https://youtu.be/SShWwOMgJ9c.
