# Agentic Proof and Property-Based Testing via Property-Templates in Data-Intensive Computing

- arXiv ID: `2607.09072v1`
- Authors: Seongmin Lee, Yaoxuan Wu, Miryung Kim
- Published: 2026-07-10
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.09072v1) | [pdf](https://arxiv.org/pdf/2607.09072v1)

## Abstract

As the cost of code generation becomes cheaper with AI, the new bottleneck in software engineering has shifted to intent specification and validation. Overcoming this durability crisis of AI-driven coding requires more than traditional fuzzing: each candidate property must be proven correct over a model and shown to hold on the real implementation, making formal proof and systematic property-based testing (PBT) complementary. However, validating properties this way at scale requires solving two subproblems: verifying candidate properties and operationalizing PBT without AI hallucination. We hypothesize that recurring property patterns, cast as property templates--abstract, parameterized forms with holes--address both at once.
  This paper investigates recurring property patterns in Apache Spark. In data-intensive scalable computing systems, correctness properties arise from the principles of data partition, computation decomposition, and dataflow computation. For instance, aggregation decomposition relates a global function executed on the entire dataset to a local function followed by a recombiner. We design an agentic, dual-track validation framework that uses property templates to formally verify correctness in the Lean 4 theorem prover and instantiate PBT templates as executable PySpark tests. Our evaluation shows that property templates increase agentic proof engineering success by up to 2.6x (1.6x on average) and reduce proof hallucinations by 59%. Template-guided PBT synthesis reduces intent misalignments from 22 to 1 and cuts synthesis cost by up to 5.7x (3.8x on average). Template-guided synthesis further exceeds a state-of-the-art Spark fuzzer and approaches unguided LLM-based PBT on code coverage. Finally, comparing the two tracks is informative: when a proof succeeds yet a PBT finds a counterexample, the mismatch identifies a gap between the formal model and implementation.
