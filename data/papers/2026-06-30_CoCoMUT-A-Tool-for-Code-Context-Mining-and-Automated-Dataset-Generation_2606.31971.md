# CoCoMUT: A Tool for Code-Context Mining and Automated Dataset Generation

- arXiv ID: `2606.31971v1`
- Authors: Alessandro Botta, Shiven Garisa, Jaya Vardhini Akurathi, Ahsanul Ameen Sabit, Trey Woodlief, Soneya Binta Hossain
- Published: 2026-06-30
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.31971v1) | [pdf](https://arxiv.org/pdf/2606.31971v1)

## Abstract

Software-engineering assistants often need method-level context beyond an isolated body, including enclosing-class information, documentation, callers, callees, type hierarchy, and structural characteristics. Manually collecting this context is time-consuming, inconsistent, and difficult to reproduce across large Java projects.
  We present CoCoMUT, a Java tool for Code-Context Mining and Automated Dataset Generation. CoCoMUT extracts context for a focal method or generates datasets at class, package, or system scope. It discovers project structure, resolves build and classpath information, constructs a SootUp static call graph, and reconciles bytecode-level call edges with Spoon-based source extraction. Each method record combines source, class, documentation, call-graph, and metadata context, providing reproducible inputs for training and running learned software-engineering techniques.
  The key contribution is a reusable, task-independent pipeline that unifies build discovery, source extraction, call-graph construction, source-bytecode reconciliation, and versioned JSON dataset generation. The resulting records can be consumed individually as context for a focal method or collectively as datasets for documentation, explanation, testing, review, repair, search, and program-comprehension workflows. We evaluate CoCoMUT on 20 real-world Java repositories evenly split between Maven and Gradle. CoCoMUT processed all 20 repositories, emitting 56,512 method-context records and 386,048 serialized call edges. Among call edges whose bytecode targets belonged to project source, CoCoMUT reconciled 97.8% to source method identities. In a manual audit of 200 randomly sampled methods across 10 systems, 99.0% of generated context records passed all applicable correctness checks.
