# EnterpriseSynth: Zero-Execution SFT and Evaluation Data from OpenAPI Specs

- arXiv ID: `2610.22412v1`
- Authors: Rashmi Thimmaraju, Natan Vidra, Setty Spurthi
- Published: 2026-10-14
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.22412v1) | [pdf](https://arxiv.org/pdf/2610.22412v1)

## Abstract

Tool-using large language model agents require substantial training and evaluation data, yet collecting execution traces from enterprise APIs is often unsafe, expensive, or infeasible because of access controls, compliance constraints, rate limits, and the risk of modifying production data. We present EnterpriseSynth, a zero-execution framework that converts OpenAPI specifications into supervised fine-tuning trajectories and paired evaluation instances without invoking the underlying APIs. The framework uses a four-stage pipeline for specification parsing, intent generation, trajectory synthesis, and static validation. Each generated trajectory is checked against the source specification for endpoint, parameter, type, and schema consistency before being admitted to the dataset. We evaluate EnterpriseSynth on 17 real and synthetic APIs. Adversarial refinement increases the validator's detection rate for planted schema violations from 57-80% to 98% (43/44). Across five random seeds, a compact open-weight model fine-tuned on EnterpriseSynth data outperforms both an untuned model and a Self-Instruct baseline on held-out APIs. Performance remains consistent on five private, hand-authored API specifications that were not available during training, with tool-selection accuracy of 40.0% on the private set and 39.6% on the public held-out set. However, an independent LLM-based evaluation shows that endpoint-selection accuracy substantially overestimates end-to-end correctness: accuracy falls from 48.9% under the endpoint-level metric to 21.3% when argument selection and values are also evaluated. These results demonstrate that OpenAPI specifications can support scalable, execution-free data generation, while highlighting the need for argument-level evaluation when assessing the deployment readiness of tool-using agents.
