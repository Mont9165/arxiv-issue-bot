# RANalyzer: Automated Continuous RAN Software Evaluation and Regression Analysis

- arXiv ID: `2604.23153v1`
- Authors: Ravis Shirkhani, Reshma Prasad, Leonardo Bonati, Tommaso Melodia, Michele Polese
- Published: 2026-04-25
- Primary category: `cs.NI`
- Categories: `cs.NI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.23153v1) | [pdf](https://arxiv.org/pdf/2604.23153v1)

## Abstract

Software-driven O-RAN architectures enable rapid innovation through frequent, independent updates to virtualized components. However, attributing performance variations to specific software changes is challenging due to the stochastic nature of wireless systems, where channel conditions, interference, and hardware variability confound analysis. Traditional threshold-based monitoring and manual troubleshooting do not scale with modern software evolution.
  This paper presents RANalyzer, an automated test analysis framework that quantifies the performance impact of software updates beyond what can be explained by wireless channel conditions. RANalyzer combines LLM-assisted semantic extraction with residuals analysis. The first categorizes code changes by affected protocol layers and functional components, while the second provides insights on the effect of load, channel, or code changes on the test performance. We contribute an extensive dataset collected over more than two years of continuous over-the-air testing on an experimental O-RAN testbed, comprising over 8,600 automated tests across 69 releases of the OAI stack. By modeling expected performance and interpreting deviations as software-induced effects, we identify degraded instances attributable to code changes and correlate them with specific change categories. The framework can be integrated into CI/CD/CT pipelines for automated, continuous evaluation of software updates at scale.
