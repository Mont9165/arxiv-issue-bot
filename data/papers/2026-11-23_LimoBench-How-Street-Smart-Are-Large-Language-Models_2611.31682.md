# LimoBench: How Street Smart Are Large Language Models?

- arXiv ID: `2611.31682v1`
- Authors: Gautam Choudhary, Jack Peng, Udesh Kumarasinghe, Rachel Rafik, Yousef Hammad, Ahmed Samy, Walid G. Aref
- Published: 2026-11-23
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.31682v1) | [pdf](https://arxiv.org/pdf/2611.31682v1)

## Abstract

Large language models (LLMs) have transformed how humans interact with information, enabling natural-language interfaces across various domains. They are increasingly deployed for geospatial applications including map-based question answering, location-based services, and natural-language interfaces to spatial databases. But are LLMs truly location-aware, able to reliably interpret and precisely answer location queries involving real-world coordinates, points of interest (POIs), and geospatial distances? To answer this concretely, we present LimoBench, a street-level benchmark of 82 natural-language location queries over seven canonical spatial operations: geocoding, reverse geocoding, routing, directionality, range search, $k$-nearest-neighbor search, and spatial join. The queries are grounded in real map data of West Lafayette, Indiana, and are graded by location and semantic complexity. They are designed to probe LLMs' street-level spatial awareness, from simple lookups to multi-step spatial reasoning. We also present Limo, an approach based on the Model Context Protocol (MCP) that enhances the location awareness of LLMs. Limo grounds LLMs in PostGIS-backed spatial data through a compact set of tools. We find that ungrounded models mostly achieve single-digit accuracy (3.1% for GPT-6 Luna) across different spatial operations. In contrast, the same models achieve near-perfect accuracy (99.3% for GPT-6 Luna) when given access to Limo's spatial tools through MCP. Current LLMs thus have limited and unreliable street-level spatial knowledge, while grounding provides accurate answers at modest overhead (+0.2 s latency, 7.7$\times$ tokens, and 2.2$\times$ cost for GPT-6 Luna). We release the benchmark, Limo toolset, and evaluation code to encourage the community to evaluate their own location-aware LLM approaches.
