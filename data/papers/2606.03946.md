# MLSkip: Data Skipping for ML Filters via Lightweight Metadata

- arXiv ID: `2606.03946v1`
- Authors: Mihail Stoian, Mark Gerarts, Pascal Ginter, Andreas Zimmerer, Jan Van den Bussche, Andreas Kipf
- Published: 2026-06-02
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.LG`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2606.03946v1) | [pdf](https://arxiv.org/pdf/2606.03946v1)

## Abstract

Database vendors recently released AI functions that can be used in filter predicates. As such functions often rely on costly, black-box ML models, they unveil new data management challenges. Concretely, traditional data skipping techniques for integer and string data fail to be applicable to the new filter type. Indeed, there is no known mechanism for pruning non-qualifying row groups, e.g., when reading files from blob storage.
  In this work, we initiate the study of data skipping techniques for ML filters. We make the case that Parquet's default min-max metadata is enough to enable pruning. To this end, we draw connections to two lines of research: (i) the recently proposed query language for ML models and (ii) neural network verification.
  Our preliminary results on ReLU architectures show that on tables from TPC-H and TPC-DS, the average pruning effectiveness for filters of selectivity below 0.1% amounts to 27.4%. Finally, inspired by research on spatial joins, we propose an enhanced metadata structure: a size-bounded 2D convex hull that verification tools can make better use of, increasing the pruning effectiveness to 38.31%, while occupying at most 45 bytes per row group and column pair. We observe an end-to-end speedup of 1.07$\times$ over PyTorch in DuckDB.
