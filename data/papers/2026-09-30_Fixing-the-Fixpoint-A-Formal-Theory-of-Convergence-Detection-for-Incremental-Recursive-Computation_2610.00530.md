# Fixing the Fixpoint: A Formal Theory of Convergence Detection for Incremental Recursive Computation

- arXiv ID: `2610.00530v1`
- Authors: Chengxi Yang, Tej Chajed, Thomas Reps
- Published: 2026-09-30
- Primary category: `cs.PL`
- Categories: `cs.PL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2610.00530v1) | [pdf](https://arxiv.org/pdf/2610.00530v1)

## Abstract

Modern incremental computation theories like DBSP have enabled efficient incrementalization of general recursive computations. To do so, they require a runtime Fixpoint Detection (FPD) mechanism to detect whether an iterative computation has reached the fixpoint and thus should terminate. However, we show that the commonly suggested "FirstZero" strategy is unsound even in naturally arising cases, and that exact FPD is impossible for arbitrary DBSP circuits with expressive primitive nodes. This issue reveals a fundamental gap between the mathematical specification and implementations of such theories. To fill this gap, using DBSP as a core calculus, we develop a formal theory of convergence detection. Within this theory, we define internal convergence (IntConv) as a declarative criterion corresponding to the internal-state-stability strategy used by practical implementations, and prove that IntConv is a sufficient condition for external convergence. We then define the state fixpoint (StFP) predicate and a sound and complete StFP detector. Combining the StFP detector with fixed-input and zero-output checks yields a sound and complete IntConv detector. Moreover, for a large class of useful circuits (programs) including Datalog queries, nested while queries, and their incrementally optimized versions, we show that IntConv is not only sound but also complete (meaning any convergence in the theory implies the convergence in our criterion). As a result, our theory provides semantic guarantees for convergence detection on all these circuits. Our results are formally verified in Lean, with the formalization available at https://github.com/Arcadia-Y/fixing-the-fixpoint/.
