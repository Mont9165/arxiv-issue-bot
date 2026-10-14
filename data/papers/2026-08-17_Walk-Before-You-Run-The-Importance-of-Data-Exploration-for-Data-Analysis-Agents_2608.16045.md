# Walk Before You Run: The Importance of Data Exploration for Data Analysis Agents

- arXiv ID: `2608.16045v1`
- Authors: Yike Yuan, Virum Ranka, Tina Lasisi, Lin Ma
- Published: 2026-08-17
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.16045v1) | [pdf](https://arxiv.org/pdf/2608.16045v1)

## Abstract

LLM-based data-analysis tools are increasingly used to help users analyze messy spreadsheets and workbooks, from answering questions over uploaded files to generating code, summaries, and visualizations. These systems are often evaluated by the correctness of their final downstream answers. However, reliable data analysis also depends on an earlier step: understanding what the dataset contains before solving the requested task. For complex workbooks, this Data Exploration step includes identifying the logical tables behind physical sheets, interpreting column semantics, recovering keys and relationships, and detecting quality issues. In current tools and benchmarks, this step is usually left implicit, creating a gap between downstream task performance and the dataset understanding needed for reliable, human-checkable analysis. Our key contribution is to identify this overlooked gap, make Data Exploration a first-class evaluation target, and show through downstream experiments that stronger Data Exploration support improves task performance. To evaluate dataset understanding directly, we introduce two benchmark settings: a real multi-sheet workbook benchmark based on a Vitamin D study dataset, and an extension of DSBench with schema-fixed Data Exploration artifacts. In both settings, systems are evaluated by the quality of a structured artifact capturing tables, columns, semantic roles, relationships, and profiling signals. Our results show that strong LLMs and data-analysis agents still miss important logical structure even when they read spreadsheet content. Furthermore, explicit Data Exploration support often improves downstream correctness, suggesting it should be treated as a first-class, inspectable stage in LLM data-analysis workflows and a natural human-in-the-loop checkpoint where domain experts can review and correct the artifact before downstream analysis proceeds.
