# Validating HTTP Semantics in REST APIs With Constructed Call Sequence Scenarios

- arXiv ID: `2608.16239v1`
- Authors: Omur Sahin, Andrea Arcuri
- Published: 2026-08-17
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.16239v1) | [pdf](https://arxiv.org/pdf/2608.16239v1)

## Abstract

Context: REST APIs are widely used in industry. These APIs use HTTP for their communications. Failures in following the specifications of HTTP can lead to confusing and hard to use APIs, with possibly serious software faults with dire consequences. Objectives: Define novel automated techniques to automatically find HTTP semantics-level faults in existing REST APIs. Methods: We extended the state-of-the-art fuzzer EvoMaster with 9 new oracles to detect HTTP semanticslevel faults. Once the standard fuzzing process is finished generating N test cases, a new phase is executed in which these N tests are used as a starting point to create new scenarios (i.e., new sequences of HTTP calls) aimed at validating specific HTTP properties defined in these 9 oracles. Results: Experiments on 9 artificial APIs with inject faults show that our novel techniques can successfully detect all of them. Further experiments on 36 APIs from the WFD corpus show that our novel techniques can automatically find 166 existing faults in these real-world APIs. Conclusion: REST APIs use HTTP, and, as such, they need to follow its semantics to avoid misleading their clients and introducing subtle software faults. The novel techniques presented in this paper are shown to be effective at automatically finding several of this type of faults.
