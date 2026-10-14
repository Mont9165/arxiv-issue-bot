# Reproducible Automated Program Repair Is Hard -- Experiences With the Defects4J Dataset

- arXiv ID: `2604.26674v1`
- Authors: Adam Krafczyk, Klaus Schmid
- Published: 2026-04-29
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2604.26674v1) | [pdf](https://arxiv.org/pdf/2604.26674v1)

## Abstract

In the research of automated program repair (APR), benchmark datasets consisting of known defects in combination with test suites that indicate the defects are of high importance. They allow for an evidence-based comparison of different APR approaches. In our own work on APR we found significant challenges when working with widely used defect datasets, which go beyond mere repeatability of defects via test cases. We summarize these identified challenges and related lessons learned to bring them to the attention of the APR community and quantify the potential impact of them.
  In particular, we investigate the widely used benchmark Defects4J, which has according to Google Scholar over 1,800 citations. It consists of 835 defects from 17 open-source Java projects; a hand-curated collection of defects, test suites that clearly indicate the defect, and human patches where any unrelated changes are removed. We find that, when executing the test suites with strict requirements for reproducibility in APR settings (beyond merely reproducing the defect via test cases), 180 (21.6 %) of the defects are not suitable for evaluation experiments. Further, we find that an additional 59 (7.1 %) defects have test suites that are obviously under-specified, as deleting a single statement from the code base makes all test cases pass, although the human-written patch does not only delete code.
  Our contributions are: a systematic collection of requirements for defect datasets for APR beyond traditional reproducibility of defects, a description of practical experiences and quantitative analysis of problems with the Defects4J dataset, as well as an implementation of an evaluation framework for APR tools for Java programs. This evaluation framework does stricter checking for indications of inadequate test suites, to avoid otherwise unnoticed problems in the test suite, such as flaky tests.
