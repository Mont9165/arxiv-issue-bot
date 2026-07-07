# Using OAI Overlay to Enhance REST API Fuzzing

- arXiv ID: `2607.04325v1`
- Authors: Omur Sahin, Man Zhang, Alexander Poth, Olsi Rrjolli, Andreas Faes, Piyun Teng, Kaiming Xue, Wenjuan Ma, Andrea Arcuri
- Published: 2026-07-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.04325v1) | [pdf](https://arxiv.org/pdf/2607.04325v1)

## Abstract

REST APIs are widely used in industry. Therefore, a lot of research has been focused on how to automatically generate test cases for REST APIs, with few different open-source fuzzers existing in the literature. For a thorough testing, especially in black-box scenarios, just relying on the information provided in the OpenAPI schemas is not enough. Testers typically need to provide extra input data to help steer the fuzzers in the right direction. Dedicated formats specific to each different fuzzer would work, but they would create a vendor lock-in, as well as increasing cognitive load. The OpenAPI Initiative (OAI) standard Overlay might be a solution to this problem. Such standard enables to define transformations on the OpenAPI schemas, where testers can provide input data in Overlay files where such data is provided as ``examples'' entries. In this paper, we have extended the state-of-the-art fuzzer EvoMaster to support Overlay files natively. Experiments are carried out in industry on five APIs from five enterprises from around the world (e.g., Belgium, China, Germany and Türkiye), including two Fortune500 enterprises as well as a 3-man startup. Our industrial results show that Overlay is a viable solution to better enable black-box fuzzing of REST APIs in industry.
