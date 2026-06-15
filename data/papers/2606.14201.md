# TACO: A Benchmark for Open-Domain Text-to-SQL with Ambiguous and Cross-Database Queries

- arXiv ID: `2606.14201v1`
- Authors: Chao Deng, Ju Fan, Yuyu Luo, Qinliang Xue, Meihao Fan, Yuxin Zhang, Min Zhang, Xiaofeng Jia, Jing Zhang, Xiaoyong Du
- Published: 2026-06-12
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.14201v1) | [pdf](https://arxiv.org/pdf/2606.14201v1)

## Abstract

Text-to-SQL aims to translate natural language questions into executable SQL queries over structured databases. Existing benchmarks mainly focus on closed-domain settings with predefined database schemas and well-specified questions, but they fall short in addressing the challenges of open-domain scenarios, such as ambiguous questions, unspecified databases, and cross-database querying. To bridge this gap, we introduce TACO, a benchmark for open-domain Text-to-SQL with Ambiguous and Cross-database queries. TACO consists of 1,500 real-world Text-to-SQL examples based on a smart city data service and 13,000 high-quality synthetic examples generated based on large-scale open data portals, covering diverse domains such as transportation, healthcare, and finance. To construct the synthetic examples, we develop an effective data synthesis pipeline that preserves the complexity of real-world queries. To demonstrate the utility of TACO, we introduce a baseline TACO-SQL composed of question rewriting, table linking, and query planning, to illustrate the challenges posed by TACO and to better understand the limitations of existing Text-to-SQL approaches. Extensive experiments on TACO using a variety of recent Text-to-SQL approaches show that, while TACO-SQL achieves the best results, a significant gap still remains between the existing approaches and human-written SQL. These findings highlight the difficulty of open-domain Text-to-SQL and position TACO as a valuable benchmark to drive future research.
