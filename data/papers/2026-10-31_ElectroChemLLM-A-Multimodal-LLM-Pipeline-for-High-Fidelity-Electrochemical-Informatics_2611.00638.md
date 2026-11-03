# ElectroChemLLM: A Multimodal LLM Pipeline for High-Fidelity Electrochemical Informatics

- arXiv ID: `2611.00638v1`
- Authors: Dikshya Mohanty, Manoj Praveen Nandigama, Kuldeepsinh Raj, Sourav Kanti Maiti, Jiannan Yang, Ruiqi Luo, Srinivasa Phani Madhav Marupudi, Mounika Geriki, Prayag Raghunandan, Puneet Lingutla, Tengfei Ma, Niranjan Balasubramanian, Nav Nidhi Rajput
- Published: 2026-10-31
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.DB`, `cs.IR`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2611.00638v1) | [pdf](https://arxiv.org/pdf/2611.00638v1)

## Abstract

Electrochemistry is central to solving many modern-day challenges, including energy storage systems for a sustainable future, and its advancement relies heavily on the data from past findings. Existing automated pipelines are limited by text-only architectures, context fragmentation, and numerical hallucinations - collectively preventing accurate, large-scale curation of property databases. We introduce ElectrochemLLM, a multimodal information extraction pipeline that jointly identifies structured electrochemical records encompassing electrolyte compositions, electrode materials, cell configurations, and their measured physicochemical properties from unstructured scientific PDFs at scale. By combining hybrid document parsing with vision-capable LLM orchestration, the pipeline extracts verifiable, structured data across text, tables, and figures. Evaluated on the battery-electrolyte subset of our manually annotated benchmark of 232 papers, ElectrochemLLM achieves an F-1 score of 0.97, and has been applied to curate ElectroChemDB, a structured database spanning 15,000 electrochemical research articles. We demonstrate the utility of this resource by training machine learning models for electrolyte property prediction, illustrating a complete pathway from unstructured literature to predictive materials discovery.
