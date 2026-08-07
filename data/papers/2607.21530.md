# From Resource Flow to Executable Tests: Petri-Net-Guided LLM Test Generation for Concurrent Stateful Rust APIs

- arXiv ID: `2607.21530v1`
- Authors: Kaiwen Zhang, Guanjun Liu
- Published: 2026-07-23
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2607.21530v1) | [pdf](https://arxiv.org/pdf/2607.21530v1)

## Abstract

Concurrent stateful library APIs expose behavior through evolving resource ownership, lifecycle states, and competing interleavings. Large language models can synthesize executable Rust tests, but their outputs often violate API preconditions, remain shallow, or reduce concurrency to accidental sequential traces. Conversely, model-based and systematic testing techniques provide semantic control but commonly require substantial handwritten code to turn abstract scenarios into executable tests. This paper addresses the gap between formal scenario design and low-cost test concretization. We present a Petri-net-guided methodology for test generation over concurrent stateful Rust APIs. The method represents API resources, lifecycle conditions, and causal dependencies as colored tokens and transitions; derives legal deep-state, near-legal, and partial-order concurrent scenarios; and uses these scenarios as a constrained intermediate representation for LLM-based code synthesis. A local-faithfulness contract and structural repair loop preserve the modeled intent during concretization, while Petri-guided schedule shaping prioritizes high-conflict concurrency skeletons for systematic exploration. A layered semantic oracle then distinguishes synthesis failures from violations of the target API's expected behavior.
