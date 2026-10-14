# DTScribe: Generating Models for Digital Twin Reporting using Local Large Language Models

- arXiv ID: `2610.18635v1`
- Authors: Kérian Fiter, Angelica Portocarrero, Bentley Oakes
- Published: 2026-10-13
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.18635v1) | [pdf](https://arxiv.org/pdf/2610.18635v1)

## Abstract

The development of a digital twin brings together many stakeholders and technical components. We have previously investigated the reporting of the conceptual architecture for these digital twins as an artifact for discussion. However, we find that the activity of modeling the digital twin for visualization and consensus-building can be quite tedious and time-consuming.
  In this article, we explore the automation of model generation using large language models, targeting the model required for digital twin reporting. Our approach is designed to ingest digital twin documents and output both the conceptual architecture visualization and a reporting page for that digital twin. We first extract from the input the key details aligning with our twenty-one-characteristic Digital Twin Description Framework described in previous work. Then, we generate a description model in the Ontological Modeling Language, representing the digital twin as a constellation of models, data, enablers, and services. We utilize refinement loops with large language models acting as judges and ontological reasoning to increase artifact quality as measured by our metrics.
  We investigate how architectural and parameter choices affect artifact quality, such as how refinement loops enable local large language models to produce sufficiently high-quality results comparable to larger models. We also detail insights and lessons learned useful for practitioners, such that they can integrate our techniques to accelerate their digital twin reporting or for other model generation tasks. These insights include the use of medium-sized local models (around 20 billion parameters), the avoidance of large language models as judges and clustering for characteristic extraction, and the recommendation of at least two reasoner loops for Ontological Modeling Language refinement.
