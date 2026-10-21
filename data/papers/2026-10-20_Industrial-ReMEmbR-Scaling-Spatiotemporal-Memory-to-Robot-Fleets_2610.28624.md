# Industrial ReMEmbR: Scaling Spatiotemporal Memory to Robot Fleets

- arXiv ID: `2610.28624v1`
- Authors: Jad Yammine, Malek Wahidi, Abrar Anwar, Yan Chang, Mihir Acharya, Anthony Rizk
- Published: 2026-10-20
- Primary category: `cs.RO`
- Categories: `cs.RO`, `cs.AI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.28624v1) | [pdf](https://arxiv.org/pdf/2610.28624v1)

## Abstract

Warehouse robot fleets continuously observe operational conditions, but preserving these observations as reusable semantic memory incurs substantial computation, communication, and storage costs. For example, explaining recurring aisle blockages can require reviewing video from multiple robots across several shifts. We present IndustrialRemembr, a shared spatiotemporal memory system that extends NVIDIA ReMEmbR to robot fleets and reduces server-side computation by generating scene descriptions only on demand. On each robot, an NVIDIA Jetson encodes video clips into retrieval embeddings with Cosmos-Embed1, vision tokens with Cosmos3-Edge, and reconstruction latents with the Wan2.2 VAE, without uploading raw camera frames. The encoding models are re-used to detect people in image patches, zeroing them out to support PII abstraction for GDPR-compliant deployments. We split Cosmos3-Edge at its vision-language boundary, placing the vision encoder on the robot and the language decoder on an on-premises server. A Nemotron agent retrieves memories by content, position, and time and queries the decoder using cached vision tokens. This design eliminates caption generation at write time, while cached-token decoding reproduces the unsplit model's output in all 450 tested decodes.
