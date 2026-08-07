# ScarfBench: A Benchmark for Cross-Framework Application Migration in Enterprise Java

- arXiv ID: `2605.06754v1`
- Authors: Advait Pavuluri, Bridget McGinn, Ashita Saxena, George Safta, Srikanth Tamilselvam, Raju Pavuluri, Michele Merler, Baishakhi Ray, Rahul Krishna
- Published: 2026-05-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.06754v1) | [pdf](https://arxiv.org/pdf/2605.06754v1)

## Abstract

Java remains central to enterprise software, and many applications outlive their original architecture. Migrating them across frameworks is a behavior-preserving refactoring spanning build configuration, dependency injection, persistence, request handling, and deployment. Existing software-engineering benchmarks cover bug fixing, feature implementation, and language or version modernization, but leave cross-framework refactoring largely unmeasured.
  We introduce ScarfBench, a benchmark for behavior-preserving cross-framework refactoring of enterprise Java applications. It is built from expert-written implementation triples across Spring, Jakarta EE, and Quarkus: 34 applications (29 focused single-layer, 5 whole) yielding 102 variants (~151K lines across 1946 source and test files) and 204 directed refactoring tasks. Each task gives an agent a working source application and a target framework; the agent must synthesize a target implementation preserving the source behavior. Correctness is evaluated by an application-specific executable oracle: the candidate must compile, deploy in a containerized target runtime, and pass behavioral tests over the application's observable interface.
  We evaluate five state-of-the-art coding agents on ScarfBench. The strongest achieves only 15.3% aggregate test pass on focused-layer migrations and 12.2% on whole applications, and only one of the 204 tasks yields a fully behaviorally equivalent target. Difficulty is asymmetric across framework directions and architectural layers: Spring<->Quarkus is the most tractable pair, and Jakarta-targeted migrations are hardest. From LLM-as-a-judge and expert adjudication of failed-task traces, we derive a taxonomy of recurring failure categories spanning build, deploy, and test stages. We release the benchmark, harness, and agent traces at https://scarfbench.info.
