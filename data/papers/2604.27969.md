# From Mirage to Grounding: Towards Reliable Multimodal Circuit-to-Verilog Code Generation

- arXiv ID: `2604.27969v1`
- Authors: Guang Yang, Xing Hu, Xiang Chen, Xin Xi
- Published: 2026-04-30
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.27969v1) | [pdf](https://arxiv.org/pdf/2604.27969v1)

## Abstract

Multimodal large language models (MLLMs) are increasingly used to translate visual artifacts into code, from UI mockups into HTML to scientific plots into Python scripts. A circuit diagram can be viewed as a visual domain-specific language for hardware: it encodes timing, topology, and bit level semantics that are invisible to casual inspection yet safety critical once fabricated in silicon. Translating such diagrams into register-transfer-level(RTL) code therefore represents an extreme reliability test for vision-to-code generation. We reveal a phenomenon we call Mirage: replacing a circuit diagram with a blank image leaves Pass@k unchanged or even higher, because models bypass the visual input and instead exploit identifier semantics in the module header to retrieve canonical RTL templates. This constitutes a new, highly covert class of defect in AI-assisted code generation that directly undermines MLLMs' trustworthiness. To quantify the effect, we construct C2VEVAL and evaluate eight MLLMs under a paired Normal/Anony protocol in which Anony mode anonymizes all identifiers in both the diagram and the module header; Anony-mode scores drop sharply across all models, confirming that high Normal-mode accuracy is largely a Mirage. We then propose VeriGround (4B), trained with identifier anonymization, refusal augmentation, and D-ORPO (Decision-Focused ORPO) preference alignment that up-weights pivotal generate-or-refuse tokens. VeriGround achieves Functional Pass@1 of 46.11%/42.51%(Normal/Anony) with a False Refusal Rate of only 1.20%/0.00%, while maintaining >92% Refusal Rate on blank images. With only 4B parameters, VeriGround performs on par with GPT-5.4 under Normal and significantly outperforms all baselines under Anony, confirming genuine visual grounding.
