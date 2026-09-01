# Database-Augmented RAG for Automated Repair of REST API Misuses

- arXiv ID: `2608.29290v1`
- Authors: Shoei Inoue, Norihiro Yoshida, Erina Makihara, Shiyu Yang, Katsuro Inoue
- Published: 2026-08-29
- Primary category: `cs.IR`
- Categories: `cs.IR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.29290v1) | [pdf](https://arxiv.org/pdf/2608.29290v1)

## Abstract

Many Internet of Things (IoT) services provide Representational State Transfer (REST) APIs, which require client developers to implement applications that conform to the corresponding API specifications. When client programs contain API misuse, developers debug them based on error responses. However, such responses are often insufficient for identifying the root cause, requiring developers to repeatedly communicate with the server. Retrieval-Augmented Generation (RAG) is a promising approach for providing large language models (LLMs) with external knowledge. However, in automated repair of REST API misuses, it remains unclear how specifications should be stored in a RAG database. This study evaluates how different configurations for organizing API specifications affect RAG-based repair of REST API misuse. We constructed 11 RAG configurations with different database structures and compared their repair rates with a baseline method. For evaluation, we used REST API misuse cases collected from real-world repositories. The results show that, in the studied datasets, the baseline method achieved a repair rate of 54.3%, whereas a RAG-based method using four databases achieved a maximum repair rate of 88.6%. These results indicate that organizing specifications according to version and content type can be an effective design choice for RAG-based REST API misuse repair.
