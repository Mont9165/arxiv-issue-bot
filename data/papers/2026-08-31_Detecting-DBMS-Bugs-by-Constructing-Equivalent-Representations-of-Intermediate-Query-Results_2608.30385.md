# Detecting DBMS Bugs by Constructing Equivalent Representations of Intermediate Query Results

- arXiv ID: `2608.30385v1`
- Authors: Xiaoxu Niu, Gong Chen, Jinfu Chen, Xiaoyuan Xie
- Published: 2026-08-31
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.30385v1) | [pdf](https://arxiv.org/pdf/2608.30385v1)

## Abstract

Database Management Systems (DBMSs) support multiple SQL mechanisms for representing intermediate query results, including VIEWs, Common Table Expressions (CTEs), and Temporary Tables (TEMPTs). When these mechanisms are used to represent the same intermediate query result, the corresponding queries are expected to produce consistent results. However, we observe that such queries can return inconsistent results, indicating potential DBMS logic bugs. Existing approaches for detecting DBMS logic bugs have never explored result consistency across such equivalent representations. In this paper, we propose ERIQ, a novel testing approach for detecting DBMS logic bugs from the perspective of checking result consistency across Equivalent Representations of Intermediate Query Results. ERIQ constructs SQL variants using a VIEW, a CTE, or a TEMPT to represent the same intermediate query result, executes these variants, and compares their returned results. We evaluated ERIQ on four widely used open-source DBMSs: MySQL, MariaDB, Percona, and OceanBase. In total, ERIQ detected 64 bugs, 63 of which were confirmed by developers, and two have been fixed. Among the confirmed bugs, 54 were unique and previously unknown logic bugs, and one was a documentation issue.
