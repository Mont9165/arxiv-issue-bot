# FacProcessTwin: An LLM-Based System for Process Twin Development

- arXiv ID: `2606.17666v1`
- Authors: Yash Pulse, Yong-Bin Kang, Abhik Banerjee, Prem Prakash Jayaraman
- Published: 2026-06-16
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.17666v1) | [pdf](https://arxiv.org/pdf/2606.17666v1)

## Abstract

Process twins provide real-time representations of entire production processes. By capturing how process steps interact, rather than monitoring a single machine in isolation as an asset-based digital twin does, they have the potential to drive efficiency gains across the whole process. However, developing a process twin is costly. It requires accurately modelling the entire production process: its process steps, the equipment and product-specific settings each step uses, and its process variations. The resulting model must then be bound to live operational data. We present FacProcessTwin, a system that leverages a large language model (LLM) to reduce this development time, building a process twin from a plant's process documentation and natural-language input from an operator. FacProcessTwin generates this complete process model and then automatically binds its process steps to live operational data. The generated model and its data bindings are rendered as an interactive process diagram through which manufacturing personnel can monitor and correct the system's autonomous decisions, such as resolving uncertainty at safety-critical binding steps. We evaluate FacProcessTwin through a real-world case study of an Australian food manufacturer, covering 16 production process flows that span chilled, frozen, and aseptic shelf-stable product categories and include process variations within the same product. The results show that FacProcessTwin generates these process models accurately (a mean F1 of 95.2% against ground truth) and builds each twin in roughly a sixth of the manual time. Its human-in-the-loop governance then keeps the safety-critical bindings correct: at ambiguous tags where a single-pass baseline silently mis-binds 75.0% of the time, FacProcessTwin defers to the operator and mis-binds none.
