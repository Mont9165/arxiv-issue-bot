# TorchGWAS : GPU-accelerated GWAS for thousands of quantitative phenotypes

- arXiv ID: `2604.21095v1`
- Authors: Xingzhong Zhao, Ziqian Xie, Islam, Sheikh Muhammad Saiful, Tian Xia, Chen, Cheng, Degui Zhi
- Published: 2026-04-22
- Primary category: `cs.DC`
- Categories: `cs.DC`, `cs.SE`, `q-bio.GN`
- Links: [abs](http://arxiv.org/abs/2604.21095v1) | [pdf](https://arxiv.org/pdf/2604.21095v1)

## Abstract

Motivation: Modern bioinformatics workflows, particularly in imaging and representation learning, can generate thousands to tens of thousands of quantitative phenotypes from a single cohort. In such settings, running genome-wide association analyses trait by trait rapidly becomes a computational bottleneck. While established GWAS tools are highly effective for individual traits, they are not optimized for phenotype-rich screening workflows in which the same genotype matrix is reused across a large phenotype panel. Results: We present TorchGWAS, a framework for high-throughput association testing of large phenotype panels through hardware acceleration. The current public release provides stable Python and command-line workflows for linear GWAS and multivariate phenotype screening, supports NumPy, PLINK, and BGEN genotype inputs, aligns phenotype and covariate tables by sample identifier, and performs covariate adjustment internally. In a benchmark with 8.9 million markers and 23,000 samples, fastGWA required approximately 100 second per phenotype on an AMD EPYC 7763 64-core CPU, whereas TorchGWAS completed 2,048 phenotypes in 10 minute and 20,480 phenotypes in 20 minutes on a single NVIDIA A100 GPU, corresponding to an approximately 300- to 1700-fold increase in phenotype throughput. TorchGWAS therefore makes large-scale GWAS screening practical in phenotype-rich settings where thousands of quantitative traits must be evaluated efficiently. Availability and implementation: TorchGWAS is implemented in Python and distributed as a documented source repository at https://github.com/ZhiGroup/TorchGWAS. The current release provides a command-line interface, packaged source code, tutorials, benchmark scripts, and example workflows.
