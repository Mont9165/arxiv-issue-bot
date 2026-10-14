# Query Cost Model Calibration in Confidential Virtual Machines

- arXiv ID: `2606.26385v1`
- Authors: Qihan Zhang, Mengyuan Li, Ibrahim Sabek
- Published: 2026-06-24
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AR`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2606.26385v1) | [pdf](https://arxiv.org/pdf/2606.26385v1)

## Abstract

With the growing adoption of Confidential Computing, running databases in confidential virtual machines (CVMs) such as AMD SEV-SNP has become an attractive way to protect sensitive cloud data with minimal changes to legacy DBMSs. However, analytical queries in such CVMs often suffer substantial overhead, and prior database work has largely stopped at benchmarking these slowdowns rather than optimizing them. We show that this problem stems from a hardware-software mismatch: query optimizers still rely on KVM-oriented (non-encrypted VM) cost assumptions that no longer hold in CVMs. To address this, we propose a lightweight CVM-aware cost calibration. It models two dominant sources of optimizer-facing overhead: data movement and RMP-related translation using simple physical proxies already available to the optimizer. Experiments show that the calibration significantly narrows the KVM/CVM performance gap, recovering up to 48 percent performance and even outperforming the KVM baseline on some workloads.
