# Curriculum Matters: Data-Efficient Relational PFN Pretraining with Synthetic Data

- arXiv ID: `2607.29120v1`
- Authors: Mohammad Sadeq Abolhasani, Viswanath Ganapathy
- Published: 2026-07-31
- Primary category: `cs.LG`
- Categories: `cs.LG`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.29120v1) | [pdf](https://arxiv.org/pdf/2607.29120v1)

## Abstract

Relational Prior-Data Fitted Networks (PFNs) such as RDB-PFN approximate Bayesian inference over multi-table relational databases by pretraining on millions of synthetic tasks. We investigate three intertwined questions about this paradigm. First, can a structurally different synthetic generator PluRel substitute for RDB-PFN's prior? Second, how much does the order in which synthetic data is presented to the PFN affect downstream performance? Third, how much relational reasoning can a PFN acquire from single-table synthetic pretraining alone, before any relational data is introduced? Using PluRel as the sole synthetic data source across all experiments, we find: (i) a progressive single-table curriculum that gradually widens schema complexity from 7 to 17 columns reaches 0.703 average ROC-AUC on the 23-task tabular benchmark using only approximately 13,300 synthetic tables (approximately 45x fewer single-table datasets than RDB-PFN's reported warm-up recipe), while the same data trained all-at-once collapses to 0.541 ROC-AUC; (ii) a relational curriculum trained from scratch on only approximately 5,500 PluRel databases reaches 0.638 average ROC-AUC on the 19-task RelBench/4DBInfer benchmark, recovering 88% of RDB-PFN's reported performance with approximately 220x less relational synthetic data; and (iii) the single-table curriculum model, evaluated directly on the relational benchmark without any relational adaptation, achieves 0.631, nearly matching the dedicated relational pipeline. Together, these findings suggest that curriculum design and synthetic data diversity may matter more for relational PFN pretraining than the specific relational generator or raw synthetic scale alone.
