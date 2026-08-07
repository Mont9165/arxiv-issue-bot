# Leveraging System-Level Observations to Inform Bayesian Learning of Model Parameters for Quantitative Verification

- arXiv ID: `2608.03489v1`
- Authors: Simos Gerasimou, Xingyu Zhao
- Published: 2026-08-04
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.LO`
- Links: [abs](http://arxiv.org/abs/2608.03489v1) | [pdf](https://arxiv.org/pdf/2608.03489v1)

## Abstract

Combining Bayesian learning and quantitative verification is a powerful toolset for analysing key quantitative properties of software systems, like reliability and response time. However, the accuracy and robustness of verification results strongly depend on the prior knowledge (PK) underlying Bayesian inference. This knowledge reflects original beliefs about the probability of events and typically depends on domain expertise. Using inaccurate or uninformative PK can negatively affect quantitative analysis, yielding incorrect verification results. Our EPIK approach tackles this important challenge by eliciting and embedding PK in quantitative verification equipped with Bayesian estimators. Unlike existing approaches that require PK on formal model transition parameters, EPIK leverages system-level properties that are directly observable and are linked to real-world semantics. EPIK formulates a twofold optimisation problem to derive the distributions of unknown transition parameters and then embeds these distributions to verify new or difficult-to-measure (elusive) properties. The detailed experimental evaluation using multiple variants of real-world case studies and diverse EPIK instantiations shows its effectiveness, flexibility and generality.
