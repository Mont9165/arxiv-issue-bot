# TACO: Task-Aware Column Description Generation Using LLMs

- arXiv ID: `2606.21685v1`
- Authors: Ting Cai, Rakesh R. Menon, Yiru Chen, Zifan Liu, Yuan Tian, Fei Wu, Anudeep Chimakurthi, Prashanthi Ramamurthy, Sunav Choudhary, Kun Qian, Yunyao Li
- Published: 2026-06-19
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.21685v1) | [pdf](https://arxiv.org/pdf/2606.21685v1)

## Abstract

Generating accurate and informative column descriptions (e.g. "membership status of customers" for the column name "cust_mem") is essential for a wide range of downstream NLP tasks on tabular data, including NL2SQL, table question answering, and entity linking. This problem arises in enterprises, domain sciences, government data portals, and so on. Despite its importance, most real-world datasets suffer from missing or cryptic documentation, often due to abbreviated column names or domain-specific jargon. Existing approaches largely rely on single-prompt large language models (LLMs), which struggle with three key issues: (i) inconsistent or incorrect handling of abbreviations, (ii) hallucinated or incomplete descriptions, and (iii) redundancy or vagueness that hinders downstream performance. We present TACO, a task-aware framework for automatic column description generation using LLMs. TACO introduces a three-step pipeline: (1) abbreviation expansion, which standardizes column names; (2) description generation, which produces initial semantic descriptions enriched with synonyms and search-oriented keywords; and (3) description revision, which refines these outputs using simulated downstream tasks. In addition, we investigate human-in-the-loop extensions and release new evaluation datasets for entity linking and schema enrichment. Extensive experiments across public and proprietary datasets show that TACO consistently outperforms existing methods, improving downstream task performance by up to 32%.
