# Causal Explanations for Stratified Datalog

- arXiv ID: `2608.21141v1`
- Authors: Ratan Bahadur Thapa, Steffen Staab
- Published: 2026-08-21
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.21141v1) | [pdf](https://arxiv.org/pdf/2608.21141v1)

## Abstract

Rule-based reasoning with exceptions requires causal explanations that account for both present and absent facts. For positive Datalog, monotonicity allows minimal supports to determine deletion causality. Stratified negation removes that property because inserting or deleting a fact may create or destroy an answer. We study actual causes, responsibility, and robustness for safe and stratified Datalog under perfect-model semantics and interventions over a finite set of mutable extensional facts. We prove that minimal supports and inclusion-minimal outcome-changing interventions do not determine causality, while robustness radius one may coexist with unbounded minimum contingencies. Our main result characterizes the minimum contingency size of a candidate fact by compatible prime implicants for the observed and opposite outcomes. The characterization conservatively recovers support-based causality for positive Datalog and yields path--cut characterizations for blocked recursive reachability. For fixed nonrecursive stratified programs, we establish data-complexity NP-completeness for cause recognition, robustness, and responsibility, and coNP-completeness for intervention-response equivalence between two such programs.
