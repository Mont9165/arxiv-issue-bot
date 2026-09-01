# RENSA: Rich Environment Metadata to Navigate Shared and Distributed Endpoints for Automated Federated SPARQL Query Generation

- arXiv ID: `2608.28963v1`
- Authors: Victor Eiti Yamamoto, Takeda Hideaki, Yamamoto Yasunori
- Published: 2026-08-29
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.CL`
- Links: [abs](http://arxiv.org/abs/2608.28963v1) | [pdf](https://arxiv.org/pdf/2608.28963v1)

## Abstract

The number of knowledge graph databases has increased significantly with the proliferation of knowledge graph technologies. Knowledge graphs enable the dynamic integration of distributed data through federated SPARQL queries. However, constructing efficient queries in a federated environment is challenging due to the lack of detailed structural knowledge across decentralized datasets. While standards like VoID provide basic metadata, they often fail to capture the complex interlinks and authority distributions necessary for optimization. Consequently, current engines frequently rely on runtime ASK queries for source selection, increasing communication overhead. We propose RENSA, a federated SPARQL query generation framework that leverages an extension of SPARQL Builder Metadata (SBM). By integrating class and authority information, mapping subject and object usage to specific predicates, RENSA enables precise source selection and semantic constraint inference for query variables without runtime communication. The generated profiles represent less than 1\% of the original dataset triples in most cases, ensuring storage efficiency. Evaluation on the LargeRDFBench benchmark (13 datasets with >1B triples, 32 queries) shows that RENSA achieves source selection results comparable to state-of-the-art methods while eliminating ASK query overhead. Furthermore, we demonstrate that RENSA infers class and authority constraints for query variables, enabling the identification of data sources even across heterogeneous endpoints. These profiles additionally offer human-readable structural insights for semi-automated query generation.
