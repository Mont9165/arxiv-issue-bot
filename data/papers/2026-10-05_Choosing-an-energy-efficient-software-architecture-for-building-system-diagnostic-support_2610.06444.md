# Choosing an energy-efficient software architecture for building system diagnostic support

- arXiv ID: `2610.06444v1`
- Authors: Roxane Koitz-Hristov, Franz Wotawa
- Published: 2026-10-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.06444v1) | [pdf](https://arxiv.org/pdf/2610.06444v1)

## Abstract

Around 30\% of global energy expenditure can be attributed to the building sector, where a large portion of energy-consumption could be avoided by repairing existing faults. Fault detection and diagnosis (FDD) software addresses this issue; however, its creation and operation also have an environmental impact. The magnitude of this impact is influenced by the diagnosis architecture, as different architectures and methods have different energy demands. Yet, simply considering the energy consumed by the software itself is not sufficient to assess its overall environmental impact, since the diagnostic performance, e.g., number of detected faults or number of faults missed, also contributes to its ecological footprint.
  In this paper, we propose an energy-consumption model that considers FDD performance and energy spend directly by the diagnosis software. In an initial experiment, we compare several FDD architecture families, i.e., rule-based, model-based, classical machine learning, and large-language-model-based, in simulation using performance and energy-consumption values collected from prior literature. The results show that considering the computational energy and accuracy of FDD can change the relative benefit of the different approaches. Computationally efficient machine learning methods, such as random forest, provide the largest net savings on smaller buildings, whereas more resource-intensive approaches, such as fine-tuned large language models, become advantageous as building size increases. Our findings suggest that overall energy efficiency depends not only on the computational demand of the FDD software, but also on its diagnostic performance and the scale of the building.
