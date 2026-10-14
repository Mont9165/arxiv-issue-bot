# LLM-Guided ANN Index Optimization for Human-Object Interaction Retrieval

- arXiv ID: `2606.05489v1`
- Authors: Shahrzad Esmat, Chaunte W. Lacewell, Sameh Gobriel, Nilesh Jain, Ali Jannesari
- Published: 2026-06-03
- Primary category: `cs.CV`
- Categories: `cs.CV`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.05489v1) | [pdf](https://arxiv.org/pdf/2606.05489v1)

## Abstract

Retrieval systems underpin modern AI applications -- spanning visual search, recommendation engines, and multi-modal question answering. Modern multi-stage retrieval systems require the joint optimization of highly coupled parameters, yet traditional hyperparameter optimization (HPO) methods -- including Tree-structured Parzen Estimators (TPE) and Gaussian Process Bayesian Optimization -- rely on an independence assumption that fundamentally prevents them from navigating these coupled configuration spaces. We address this limitation with a phase-aware large language model (LLM) agent that conditions each proposal on its full optimization history, navigating the coupled parameter space across phase-partitioned exploration, exploitation, and fine-tuning stages. Evaluated on the HICO-DET human-object interaction retrieval benchmark using Intel VDMS (Visual Data Management System), our agent outperforms Optuna TPE by +33.3% and VDTuner by +34.2% under SIEVE (Safeguarded Index Evaluation of Vector-search Efficiency, a quality-constrained throughput metric), delivering a 15.3x throughput gain over UniIR. Validation across three benchmarks confirms that the agent's advantage grows with the degree of parameter coupling: +33.3% on HICO-DET (high coupling), methods converge within 1% on GLDv2 (moderate coupling) and within 3.6% on SIFT1M (near-independent control). Cross-system validation on Milvus confirms the optimizer ranks first on all three datasets without modification, demonstrating transferability across vector database management system (VDBMS) platforms.
