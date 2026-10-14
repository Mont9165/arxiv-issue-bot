# Separating Statistical Inference from Experimental Runtime: An Architecture for Sequential Scientific Analysis

- arXiv ID: `2610.15824v1`
- Authors: Alexander Stepanov, Andrej Novikov
- Published: 2026-10-11
- Primary category: `math.ST`
- Categories: `math.ST`, `cs.MS`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.15824v1) | [pdf](https://arxiv.org/pdf/2610.15824v1)

## Abstract

Sequential statistical procedures are increasingly embedded in scientific systems in which observations arrive incrementally from heterogeneous sources. In such systems the statistical update is only one part of the computation: observations must also be acquired, aligned across inputs, ordered, delivered, persisted, and replayed, and results must be passed to systems that display them or act on them. Sequential methods are nevertheless missing from the general software toolkit. They run inside proprietary experimentation platforms and commercial statistical packages, or exist as offline functions over complete data, and the batch fit interface that dominates machine-learning libraries has no place for a procedure that listens, keeps state, and decides when to stop. We propose an architecture that separates statistical inference from data topology, execution runtime, run lifecycle, persistence, and external action. Its central abstraction is the Sequential Procedure: a state-transition function that maps an inferential state, a valid statistical input, and a statistical random state to a new state and a scientific output. The procedure does not define how observations are acquired, paired, scheduled, stored, or acted upon. We specify the architecture semantically rather than through an object model, derive seven conformance invariants that any implementation can be tested against (among them synchronous/asynchronous, checkpoint, replay, and batch equivalence), and describe a dependency-free reference implementation in which all seven hold bitwise. Lorden's 2-SPRT for the Kiefer-Weiss problem serves as the reference procedure; the same contract accommodates sequential estimators, Bayesian filters, change-point detectors, and stateful predictive models.
