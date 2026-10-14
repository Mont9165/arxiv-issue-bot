# ASSEMBLAGE-DEEPHISTORY: A Cross-Build Binary Dataset with Temporal Coverage

- arXiv ID: `2605.21615v1`
- Authors: Chang Liu, Noah Fleischmann, Nicolò Altamura, Edward Raff, James Holt, Kristopher Micinski
- Published: 2026-05-20
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.LG`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.21615v1) | [pdf](https://arxiv.org/pdf/2605.21615v1)

## Abstract

Existing binary corpora typically capture only one or two axes of binary variation: they either provide cross-compiler builds without a temporal axis, or CVE labels for single-build binaries. None combine cross-build diversity, cross-version history, and CVE labels into a queryable structure. We present ASSEMBLAGE-DEEPHISTORY, which consolidates these dimensions into a unified framework where every binary's compilation context, source code, vulnerable functions, and package version are stored as first-class metadata.
  ASSEMBLAGE-DEEPHISTORY comprises 73,610 binaries spanning 248 open-source projects, compiled across GCC, Clang, and MSVC at multiple optimization levels on Linux and Windows, with multi-year historical builds. Each binary is indexed in a database that links it to its source code, functions, debug info, variant builds, historical versions, and vulnerable functions. Three analyses demonstrate this structure's value: (1) a three-stage LLM benchmark (recognition, strategy-guided detection, and cross-build transfer) to test whether LLMs reason about binary vulnerabilities or pattern-match on build-specific artifacts; (2) a comparison of MalConv embeddings, jTrans function embeddings, and TLSH fuzzy hashes quantifying how same-package versions cluster in each space; and (3) a Bayesian regression decomposing binary similarity into contributions from temporal distance, file changes, and commits.
