# EcoTable: Cost-effective Table Integration in Data Lakes for Natural Language Queries

- arXiv ID: `2606.26613v1`
- Authors: Yuhui Wang, Jinqi Liu, Chengliang Chai, Hangyu Zhao, Yuhao Deng, Yuyu Luo, Xin Tang, Ye Yuan, Guoren Wang, Fengjin Wang, Lei Cao
- Published: 2026-06-25
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.26613v1) | [pdf](https://arxiv.org/pdf/2606.26613v1)

## Abstract

The diverse formats of CSV and Parquet files in data lakes pose a significant challenge to traditional ETL, which relies on data engineers to pre-define a target database schema and build a complex pipeline for data integration. Moreover, with this approach, the integrated data often cannot support various analytical needs, as the predefined schema does not necessarily satisfy the table format or join relationships required to answer unforeseen queries. To address this, we propose EcoTable, the first natural language-based data integration framework. Given a set of user-specified natural language queries, EcoTable automatically integrates the tables into a form that adequately supports the corresponding SQL queries. EcoTable achieves this by leveraging the semantic understanding and complex reasoning capabilities of LLMs. Moreover, EcoTable addresses the scalability and cost issues introduced by expensive LLM inferences with a set of novel ideas. First, EcoTable introduces a graph to represent the overall search space, where nodes represent tables and edges carry weights indicating join likelihood produced by a lightweight deep learning model. On top of this graph data structure, EcoTable designs three components to achieve our goal: (1) the table identification layer aims to identify relevant tables via a two-stage schema linking based on user queries; (2) the graph-based validation layer aims to discover significant join paths, including necessary data transformations and bridging tables, by modeling the problem as Steiner tree searches; and (3) the table transformation layer generates transformation code to implement the joins using LLMs. We construct 4 real-world benchmark datasets with more than 200 queries. Extensive experiments demonstrate that EcoTable outperforms the state-of-the-art baselines, increasing accuracy by more than 30% and cutting LLM invocation costs by 5 times.
