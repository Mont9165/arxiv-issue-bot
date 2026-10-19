# Recall-Oriented Precise Binary-to-Source Function Matching

- arXiv ID: `2610.23546v1`
- Authors: Junlin Li, Jianjun Huang, Wei You, Bin Liang
- Published: 2026-10-16
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.23546v1) | [pdf](https://arxiv.org/pdf/2610.23546v1)

## Abstract

Binary-to-source function matching supports software composition analysis by identifying reused third-party code, but existing embedding-based approaches restrict subsequent refinement to initially retrieved candidates. When the correct source function is absent from this set, selecting or filtering the available candidates cannot recover the match. Inlining further complicates the retrieval by combining multiple source functions into one binary function. In this paper, we propose BScout to improve matching precision and uncover additional matches. BScout uses the positional information of existing matches to supplement candidates for unresolved binary functions, extending the search beyond the initial candidate set, and adopts composition-aware training to address the inlined composition matching. Large language models are adopted to select and review matches, while positional information also helps filter inconsistent results. Experiments show that BScout is effective in binary-to-source function matching. BScout achieves overall higher precision, recall and F1 scores than BinaryAI and SBridge with acceptable analysis costs. Particularly, on large stripped binaries, BScout outperforms the competitors with a precision increment of 32% and approximately 2.9 times the recall.
