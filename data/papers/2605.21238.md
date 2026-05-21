# Beyond the Tip of the Iceberg: Understanding SATD in Dockerfiles through the Lens of Co-evolution

- arXiv ID: `2605.21238v1`
- Authors: Wei Minn, Yan Naing Tun, Biniam Fesseha Demissie, Rui'ang Hu, Jiakun Liu, Mariano Ceccato, Lwin Khin Shar, David Lo
- Published: 2026-05-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.21238v1) | [pdf](https://arxiv.org/pdf/2605.21238v1)

## Abstract

Dockerfiles enable the creation of portable container-based execution environments for the application code, and have become an important part of the modern software development process. As Dockerfiles are a form of Infrastructure-as-Code (IaC), they can include temporary workarounds and other suboptimal implementations, leading to the accrual of technical debt that affects their reliability, security, and maintainability in the future. Prior work characterized self-admitted technical debt (SATD) in Dockerfile comments and the surrounding file chunks. This single-file view is incomplete since source code evolution involves changes across different types of software artifacts such as production, test, build, and other configuration files. Thus, we address this gap by studying SATD events in Dockerfiles alongside the related source code.
  We find that approximately 27% of admission events and 40% of repayment events are coupled to non-Dockerfile artifacts, and coupling sources are subtype-specific. We also observed that coupled SATD in general are repaid significantly faster overall (p = 0.0201), while coupled SATD regarding missing functionalities persists longer than its isolated counterparts; Lastly, we conducted open and axial coding of coupled SATD events, and we observe that external dependency issues, more particularly regarding unreleased upstream packages and bug fixes, are the most common cause of admission triggers in the source code; we also observe that architectural refactoring is the most common prerequisite for the repayment of SATD in Dockerfiles. These findings indicate that both practitioners (e.g. developers and project managers) and SATD researchers should integrate the source code-side co-evolution, rather than the single-file view, as the primary unit of analysis.
