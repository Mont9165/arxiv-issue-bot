# Automating Categorization of Scientific Texts with In-Context Learning and Prompt-Chaining in Large Language Models

- arXiv ID: `2604.23430v1`
- Authors: Gautam Kishore Shahi, Oliver Hummel
- Published: 2026-04-25
- Primary category: `cs.IR`
- Categories: `cs.IR`, `cs.AI`, `cs.CL`, `cs.DL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.23430v1) | [pdf](https://arxiv.org/pdf/2604.23430v1)

## Abstract

The relentless expansion of scientific literature presents significant challenges for navigation and knowledge discovery. Within Research Information Retrieval, established tasks such as text summarization and classification remain crucial for enabling researchers and practitioners to effectively navigate this vast landscape, so that efforts have increasingly been focused on developing advanced research information systems. These systems aim not only to provide standard keyword-based search functionalities but also to incorporate capabilities for automatic content categorization within knowledge-intensive organizations across academia and industry. This study systematically evaluates the performance of off-the-shelf Large Language Models (LLMs) in analyzing scientific texts according to a given classification scheme. We utilized the hierarchical ORKG taxonomy as a classification framework, employing the FORC dataset as ground truth. We investigated the effectiveness of advanced prompt engineering strategies, namely In-Context Learning (ICL) and Prompt Chaining, and experimentally explored the influence of the LLMs' temperature hyperparameter on classification accuracy. Our experiments demonstrate that Prompt Chaining yields superior classification accuracy compared to pure ICL, particularly when applied to the nested structure of the ORKG taxonomy. LLMs with prompt chaining outperform the state-of-the-art models for domain (1st level) prediction and show even better performance for subject (2nd level) prediction compared to the older BERT model. However, LLMs are not yet able to perform well in classifying the topic (3rd level) of research areas based on this specific hierarchical taxonomy, as they only reach about 50% accuracy even with prompt chaining.
