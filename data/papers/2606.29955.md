# SpreadsheetBench 2: Evaluating Agents on End-to-End Business Spreadsheet Workflows

- arXiv ID: `2606.29955v1`
- Authors: Jian Zhu, Yuzheng Zhang, Zeyao Ma, Bohan Zhang, Armin Schoepf, Daniel Woloch, Peter Yiliu Wang, Guangyu Robert Yang, Samuel Jacob, Siddharth Nagisetty, Abhiram Chundru, Jean Lin, Spencer Mateega, Jing Zhang
- Published: 2026-06-29
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.29955v1) | [pdf](https://arxiv.org/pdf/2606.29955v1)

## Abstract

Spreadsheets are widely used for business analysis, financial modeling, reporting, and decision-making. However, most existing spreadsheet benchmarks evaluate isolated operations such as single-formula generation or local cell edits, and therefore fail to capture end-to-end workflows in realistic business settings. We introduce \textsc{SpreadsheetBench 2}, a workflow-level benchmark for spreadsheet agents that covers three task categories: generation, debugging, and visualization. The benchmark is constructed from authentic business data, including financial reports and corporate filings, and is annotated and validated by domain experts. The benchmark contains 321 tasks; each instance averages 11.8 worksheets and requires 593.5 cell modifications, reflecting large multi-sheet workbooks with cross-sheet dependencies. We evaluate eight frontier large language models under a unified multi-turn agent scaffold, and additionally include several LLM-based spreadsheet products as complementary baselines. Results show that current systems remain far from reliable on real-world workflows: the best model achieves 34.89\% overall task accuracy, and debugging accuracy is as low as 12.00\%. Trajectory analysis and a failure taxonomy further indicate that insufficient spreadsheet inspection and incorrect target-cell selection are the dominant bottlenecks. Together, these findings position \textsc{SpreadsheetBench 2} as a challenging testbed for advancing reliable spreadsheet automation. Project page: https://spreadsheetbench.github.io/
