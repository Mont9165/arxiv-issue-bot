# Correctness-Aware Repository Filtering Under Maximum Effective Context Window Constraints

- arXiv ID: `2605.14362v1`
- Authors: Shweta Mishra
- Published: 2026-05-14
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2605.14362v1) | [pdf](https://arxiv.org/pdf/2605.14362v1)

## Abstract

Context window efficiency is a practical constraint in large language model (LLM)-based developer tools. Paulsen [12] shows that all tested models degrade in accuracy well before their advertised context limits the Maximum Effective Context Window (MECW) which makes context construction a quality problem, not just a cost one. Modern software repositories routinely contain large non-code artifacts compiled datasets, binary model weights, minified JavaScript bundles, and gigabyte-scale log files that overflow the context window and push out task-relevant source code. We present a correctness-aware context hygiene framework: a pre-execution, size-based heuristic filter that intercepts repository scans before tokenization, using only OS-level stat() metadata with sub-millisecond overhead. Semantic retrieval approaches such as RepoCoder, GraphRAG, and AST-based chunking require index construction and query-time inference before any filtering decision is reached. Our framework, by contrast, requires no indexing and operates at <0.01 ms per file decision. Across 10 real open-source repositories (22,046 files, 5 languages), the proposed SizeFilter at θ=1 MB achieves 79.6% (\pm13.2%) mean token reduction at 0.30 ms overhead: the HybridFilter achieves 89.3% (\pm9.0%) the lowest variance of any filter evaluated. A token-density study across 2,688 files confirms a strong linear correlation (Pearson r=0.997, k=0.250 tokens/byte). A limited-scope evaluation (18 tasks, CodeLlama-7B-Instruct) yields 72% file-level accuracy under filtering versus 25% at baseline; hallucination frequency declines from 61% to 17%. All code and data are released for reproducibility.
