# Beyond Repository Boundaries: Cross-Repository Graph Retrieval for Code Generation

- arXiv ID: `2609.09987v1`
- Authors: Minh Le-Anh, Nam Le Hai, Quyen Tran, Anh Nguyen Hoang, Linh Ngo Van, Bach Le, Nghi D. Q. Bui
- Published: 2026-09-09
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.09987v1) | [pdf](https://arxiv.org/pdf/2609.09987v1)

## Abstract

Repository-level code generation requires generated code to be compatible not only with the target repository but also with its dependency environment. Existing retrieval-based methods mainly retrieve context from the local repository, leaving external API usage dependent on the model's pretrained knowledge, which can be insufficient for unseen or version-specific APIs. Moreover, current retrieval strategies largely focus on one-hop evidence and overlook the structural relationships among code components. We propose CrossCoder, a cross-repository code generation framework that explicitly incorporates external libraries into the retrieval context through a unified knowledge graph over repository and library entities. CrossCoder identifies important nodes via planning and semantic retrieval, then selectively expands neighboring nodes to retrieve richer multi-hop contextual evidence for generation. To further evaluate dependency-version compatibility, we introduce VersionExec, an execution-based benchmark derived from BigCodeBench that evaluates generation under different dependency versions. Experimental results on RepoExec, DevEval, and VersionExec demonstrate that CrossCoder consistently improves both functional correctness (up to 6.3% on pass@1) and robustness to dependency-version changes.
