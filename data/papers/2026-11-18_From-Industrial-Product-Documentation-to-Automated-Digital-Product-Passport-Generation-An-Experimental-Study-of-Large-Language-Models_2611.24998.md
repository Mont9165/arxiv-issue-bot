# From Industrial Product Documentation to Automated Digital Product Passport Generation: An Experimental Study of Large Language Models

- arXiv ID: `2611.24998v1`
- Authors: Marco Buecheler, Grant Richards, Nathan Hartman
- Published: 2026-11-18
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.24998v1) | [pdf](https://arxiv.org/pdf/2611.24998v1)

## Abstract

Manufacturing companies that are planning to sell certain products in the European Union (EU) will be required to provide mandatory digital product passports (DPPs). The use of DPPs is to provide standardized product information throughout multiple product life cycles in a circular economy. Required passport information, such as technical specifications, material composition, and environmental product footprint, is available in manufacturers' data sources but is scattered across different heterogeneous systems, documents, and data formats. The given paper investigates using large language models (LLMs) to automate the generation of DPPs based on the asset administration shell (AAS). A retrieval-augmented generation (RAG) approach is used to extract product information from industrial documentation and generate populated AAS instances. Product documentation is processed and divided into text chunks. The text chunks are then stored in a persistent ChromaDB vector database using vector embeddings. The retrieval process combines semantic and lexical search to identify relevant information based on standardized AAS submodel template requirements. The retrieved information is provided to five LLMs to generate structured AAS instances. The experiments cover different industrial products and AAS submodels. Four levels of prompt guidance are investigated to assess their influence on generation quality. The generated passports are evaluated against a ground truth. The experimental evaluation includes 4,560 executions across 76 product-submodel combinations. Of the generated passport outputs, 97.4% are valid JSON, while 44.9% pass the full AAS validation procedure. Under deterministic scoring, mean completeness, conditional accuracy, and overall field correctness are 49.6%, 58.3%, and 30.8%, respectively. An LLM-as-a-judge yields better scores of 66.5%, 88.9%, and 60.4% for the same outputs.
