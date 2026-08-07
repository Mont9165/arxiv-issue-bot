# From Custom-Fit to Portable: Bridging the Gap Between Synthesized and Engineered GPU Query Execution

- arXiv ID: `2607.07632v1`
- Authors: Ivan Donchev Kabadzhov, Eugenio Marinelli, Raja Appuswamy
- Published: 2026-07-08
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.07632v1) | [pdf](https://arxiv.org/pdf/2607.07632v1)

## Abstract

GPUs are increasingly used for analytical query processing, but developing GPU-based database engines that achieve the peak performance of the underlying hardware requires substantial research and engineering effort. A recent line of work argues that query processing should be synthesized, not engineered. In this scenario, instead of tuning a general-purpose engine to fit a workload, a large language model (LLM) generates code specialized to one query, one dataset, and one machine, thereby achieving an order-of-magnitude improvement in performance. This thesis, however, has so far been tested only on CPUs. In this work, we revisit the synthesize-versus-engineer debate for GPU analytics by answering three questions: (i) how good is synthesized GPU code?, (ii) why is it faster than engineered engines?, and (iii) how much of its advantage can be transferred back into a single, performance-portable engine?
  To answer the first question, we present SHADB, an LLM-based synthesis framework that generates optimized CUDA or HIP kernels using an automated, profile-guided optimization loop. Using SHADB, we show that the synthesized code approaches the memory-bandwidth ceiling and outperforms a state-of-the-art JIT-compiled GPU database engine (HeavyDB) by 7.4$\times$ on SSB SF100. To answer the second question, we decompose this performance gap and systematically classify optimizations as generalizable or workload-specific. Finally, to answer the third question, we integrate these generalizable optimizations into SYCLDB, a performance-portable engine written entirely in the open SYCL programming model. Using optimized SYCLDB, we show that it is possible to substantially bridge the gap to synthesized code (within 1.27$\times$ total execution time) while retaining workload-level generality and hardware-level performance portability.
