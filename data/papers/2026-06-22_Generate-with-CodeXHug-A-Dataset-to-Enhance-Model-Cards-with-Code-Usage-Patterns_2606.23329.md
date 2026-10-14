# Generate with CodeXHug: A Dataset to Enhance Model Cards with Code Usage Patterns

- arXiv ID: `2606.23329v1`
- Authors: Stefano Palombo, Claudio Di Sipio, Juri Di Rocco, Davide Di Ruscio
- Published: 2026-06-22
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.23329v1) | [pdf](https://arxiv.org/pdf/2606.23329v1)

## Abstract

Pre-trained models (PTMs) are becoming increasingly popular in the software engineering community. Their usage is facilitated by model repositories, e.g., HuggingFace, which collect, store, and maintain a wide range of PTMs. However, the actual adoption of these models in real-world projects is still an open question, i.e., many of them are used in toy projects or simply as a mirror for the HF repository. In addition, most of the available model cards and textual documents that contain critical information about their usage do not include explanatory code patterns, thus increasing the difficulty for newcomers. Thus, we see the need for a curated codebase related to PTMs to support developers and practitioners who are interested in using them in their projects.
  In this paper, we present CodeXHug, a curated dataset of HuggingFace PTMs exploited in the Github ecosystem and the related code usage patterns. Starting from the latest HF dump, we first conduct a data curation to collect PTMs with a tag and a model card. Then, the Github platform has been queried to find actual usages of the identified PTMs, resulting in 7,325 different models and 20,545 Python files.
  To demonstrate a concrete application of CodeXHug, we propose a usage scenario focused on extracting representative code usage patterns for specific PTMs through a statistical analysis and clustering techniques applied to relevant code snippets.
