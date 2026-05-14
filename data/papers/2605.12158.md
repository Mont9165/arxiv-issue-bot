# ReproBreak: A Dataset of Reproducible Web Locator Breaks

- arXiv ID: `2605.12158v1`
- Authors: Thiago Santos de Moura, Leon Adamietz, Samra Mehboob, Yannic Noller
- Published: 2026-05-12
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.12158v1) | [pdf](https://arxiv.org/pdf/2605.12158v1)

## Abstract

Automated GUI testing frameworks such as Cypress and Playwright rely on locators to find and interact with web elements. A locator break occurs when a structural change in the application under test causes a locator to no longer find its target element, resulting in test breakages even when the underlying functionality remains unchanged. Despite its impact on test maintenance, no dataset exists to evaluate locator fragility in Cypress and Playwright at scale. In this paper, we present ReproBreak, a dataset of reproducible locator breaks in web application GUI tests. We analyzed 359 open-source repositories to identify commits that contain locator changes. To confirm whether these changes are indeed locator breaks, we reproduced them in the top 4 projects with the largest number of locator changes and found 449 locator breaks, which are provided in the dataset along with scripts for automated reproduction. We believe ReproBreak serves as a valuable artifact to support research on locator fragility, repair techniques, and test robustness. The video is available at: https://youtu.be/mZByS_TnCvE. The dataset is at https://github.com/rub-sq/ReproBreak.
