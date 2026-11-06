# Global Surveillance Under the Lens: Reconstructing Passive Dolev-Yao Intruders

- arXiv ID: `2611.07170v1`
- Authors: Paolo Modesti
- Published: 2026-11-04
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.07170v1) | [pdf](https://arxiv.org/pdf/2611.07170v1)

## Abstract

Global surveillance systems record large volumes of network traffic for retrospective analysis, but packet captures alone reveal little about protocol-level semantics. This paper presents an automated, specification-guided methodology for reconstructing passive Dolev-Yao intruder executions from captured network traffic and validating the reconstructed executions against a formal protocol specification. The framework takes a PCAP capture, an AnBx specification, and the associated deployment metadata; it extracts Java-serialised objects from TCP streams, reconstructs protocol sessions and channel-to-step assignments, and generates a passive intruder that evaluates the Dolev-Yao derived checks produced by the AnBx compiler. Three reconstruction challenges are addressed: multiple serialised objects and object references within a TCP stream, ambiguity in mapping interleaved connections to concurrent protocol sessions, and semantic validation of candidate reconstructions. We evaluate the methodology on 121 protocols from the AnBx test suite. For single-session captures, the standard JDK cryptographic provider recovers 97.8% of expected objects and achieves 94.2% successful reconstruction, where success requires complete object recovery and a clean passive-intruder execution. For the 112 parallel-capable protocols, the toolchain achieves 89.3% successful reconstruction for both two and three concurrent sessions, while recovering approximately 97.2% of expected objects. Experiments with mismatched protocol-role mappings and deliberately mutated traces show that the generated Dolev-Yao checks respond to semantic inconsistencies. By making the reconstruction step explicit, the solution produces protocol-level observations on which assessments of protocol resilience and the design of defensive countermeasures can be built.
