# ITHICA: Intra-Thread Instruction Checking Approach for Defect-Induced Silent Data Corruptions

- arXiv ID: `2605.15638v1`
- Authors: Ioanna Vavelidou, Subho S. Banerjee, Eric X. Liu, Mike Fuller, Subhasish Mitra, Caroline Trippel
- Published: 2026-05-15
- Primary category: `cs.AR`
- Categories: `cs.AR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.15638v1) | [pdf](https://arxiv.org/pdf/2605.15638v1)

## Abstract

Hyperscaler reports of silent data corruptions (SDCs), presumed to be caused by silicon manufacturing defects, have motivated the development of functional tests for detecting defective CPUs. We present ITHICA, an approach for automatically generating functional tests for defect-induced errors from arbitrary programs by inserting intra-thread, instruction-level error checks, primarily leveraging instruction duplication and output comparison. Our key insight is that the most pernicious defects cause inconsistent errors: two executions of the same instruction within the same thread, given the same inputs, can produce different architectural outputs depending on the execution context in which they run. By exploiting this insight, ITHICA enables arbitrary programs to serve as tests and identifies affected instructions upon error detections. We use ITHICA to transform industrial hyperscaler test programs (our baseline), datacenter workloads, and common libraries into functional tests, and evaluate them on over 3,000 CPU servers. ITHICA error checks detect 39% more defective servers than native checks within the ITHICA tests derived from our baseline programs, and enable novel findings on defect behavior that challenge conclusions drawn by prior hyperscaler fleet studies.
