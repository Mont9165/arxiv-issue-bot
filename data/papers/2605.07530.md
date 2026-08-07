# Search-based Robustness Testing of Laptop Refurbishing Robotic Software

- arXiv ID: `2605.07530v1`
- Authors: Erblin Isaku, Hassan Sartaj, Shaukat Ali, Malaika Din Hashmi, Francois Picard
- Published: 2026-05-08
- Primary category: `cs.RO`
- Categories: `cs.RO`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.07530v1) | [pdf](https://arxiv.org/pdf/2605.07530v1)

## Abstract

The Danish Technological Institute (DTI) focuses on transferring advanced technologies (including robots) to the industry and the public sector. One key application is laptop refurbishment using specialized robots, aimed at promoting reuse, reducing electronic waste, and supporting the European Circular Economy Action Plan. The software of such robots often includes features that use object detection models to detect objects for various purposes, such as identifying screws for laptop disassembly or detecting stickers to remove them. Ensuring the robustness of such models to small input variations remains a critical challenge, and addressing it is important to avoid potential damage to laptops during refurbishment. In this paper, we propose PROBE, a search-based robustness testing approach that leverages multi-objective optimization to identify minimal, localized perturbations that expose failures in object detection models used in the software of laptop refurbishing robots. PROBE employs NSGA-II to systematically explore the perturbation space, optimizing for failure induction considering both localization and confidence, and perturbation magnitude, while enabling the discovery of diverse failure cases. Results show that PROBE is 3$\times$ to 7$\times$ more effective than random search in generating failure-inducing perturbations, while requiring smaller perturbation magnitudes, and that the generated perturbations transfer across models. We further show that metamorphic relations provide additional insights into model robustness, enabling the assessment of stability even in non-failing cases.
