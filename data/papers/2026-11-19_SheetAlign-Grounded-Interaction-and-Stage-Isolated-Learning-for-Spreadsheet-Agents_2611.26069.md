# SheetAlign: Grounded Interaction and Stage-Isolated Learning for Spreadsheet Agents

- arXiv ID: `2611.26069v1`
- Authors: Yuxiang Wang, Junhao Gan, Jianzhong Qi
- Published: 2026-11-19
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.26069v1) | [pdf](https://arxiv.org/pdf/2611.26069v1)

## Abstract

Spreadsheets are widely used for data analysis and supporting decision-making. Automating spreadsheet analysis while protecting sensitive data and controlling deployment costs motivates locally deployed open-weight large language models (LLMs). Meanwhile, complex spreadsheet tasks require both task reasoning and workbook understanding, while predefined operation interfaces impose additional tool-selection and invocation demands. We introduce SheetAlign, a spreadsheet manipulation framework with stage-isolated policy learning, organized around where to operate, what to change, and how to implement transformations. Task-guided inspection and API grounding anchor code generation in workbook observations and available operations, while stage-isolated learning optimizes program generation and review using edit-progress rewards. At inference, execution consistency selects programs through agreement among workbook states. On SpreadsheetBench, our grounded task interface improves Qwen3-4B's accuracy from 13.5% to 29.2% on average without training. With learning and execution consistency, SheetAlign achieves 32.8% accuracy on average on SpreadsheetBench and 30.1% on Domain-Spreadsheet, outperforming comparable baselines. The code will be made publicly available upon publication.
