# Industrial Practice of LLM-Based Test Case Carving and Assertion Generation (Experience Paper)

- arXiv ID: `2607.24000v1`
- Authors: Haozhen You, Zhen Dong, Jingjing Wang, Qiang Li, Xin Peng
- Published: 2026-07-27
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.24000v1) | [pdf](https://arxiv.org/pdf/2607.24000v1)

## Abstract

Enterprise regression testing for microservice systems is often constrained by incomplete or outdated documentation. In practice, QA engineers frequently rely on real execution traffic to reconstruct business scenarios; however, turning raw traffic into replayable regression tests with stable validation logic remains labor-intensive and error-prone.
  This paper presents NL2Test, an end-to-end approach and tool that generates executable API regression tests from (i) a natural-language scenario description and (ii) a traffic capture recorded while executing the scenario. NL2Test addresses two coupled tasks: test case carving, which extracts a minimal replayable request sequence and reconstructs data dependencies so that dynamic values are bound from their responses rather than hard-coded; and assertion generation, which produces assertions aligned with business intent while avoiding non-deterministic fields and hallucinated paths. To improve reliability, NL2Test uses LLMs for semantic interpretation and constrained code synthesis, and uses deterministic algorithms for request filtering, dependency confirmation via value consistency, and assertion-path validation.
  We evaluate NL2Test on 51 industrial regression scenarios extracted from a large consumer-facing Internet company. NL2Test achieves an exact-match rate of 82.4% (42/51), and produces a functionally usable draft in 98.0% (50/51) of scenarios when allowing minor post-edits. In a 9-month production deployment starting in March 2025, NL2Test generated 3,196 test cases with an overall code adoption rate of 85.4%. These results indicate that traffic-grounded generation with deterministic guardrails can substantially reduce manual effort while improving regression automation in complex microservice environments.
