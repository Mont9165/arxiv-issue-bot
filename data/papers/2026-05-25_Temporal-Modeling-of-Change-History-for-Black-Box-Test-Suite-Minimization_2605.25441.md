# Temporal Modeling of Change History for Black-Box Test Suite Minimization

- arXiv ID: `2605.25441v1`
- Authors: Kamruzzaman Asif, Md. Siam, Kazi Sakib
- Published: 2026-05-25
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.25441v1) | [pdf](https://arxiv.org/pdf/2605.25441v1)

## Abstract

Test Suite Minimization (TSM) reduces the size of test suites while preserving their fault detection capability. In black-box TSM, reduction is performed without relying on production-code instrumentation. While several black-box TSM approaches have explored metrics like test logs or test similarity, these often suffer from scalability and efficiency issues. Recently, change history has been explored as a lightweight and scalable indicator for guiding black-box TSM. However, existing approaches treat historical modifications uniformly, ignoring the temporal dynamics of software evolution where recently modified code tends to be more fault-prone. To address this limitation, we introduce temporal modeling into black-box TSM and propose Temporal Risk-driven Test Suite Minimization (TRTM). TRTM extracts modification history from version-control metadata and applies exponential temporal attenuation to weight changes based on recency, producing time-weighted class-level risk scores that reflect fault-proneness. Next, it determines dependencies between test cases and production classes by constructing static call graphs derived solely from test code, preserving the black-box setting. The risk scores of the classes exercised by each test case are then aggregated using statistical measures such as Average and Geometric Mean to compute a risk score for the test case. Finally, test cases with the highest risk scores are selected to construct the reduced suite. Evaluation on a large dataset containing 14 projects with 631 versions shows that TRTM consistently outperforms the state-of-the-art baseline, achieving a mean Accuracy of 0.72 (vs. 0.66) and Fault Detection Rate (FDR) of 0.75 (vs. 0.69), while also reducing execution time.
