# Spotting Setting-Related UI Display Bugs in Android Apps

- arXiv ID: `2607.04120v1`
- Authors: Huaxun Huang, Wu Liu, Jiahao Gu, Rongxin Wu
- Published: 2026-07-05
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.04120v1) | [pdf](https://arxiv.org/pdf/2607.04120v1)

## Abstract

Android provides a wide range of system settings that allow users to control the runtime behaviors of apps, such as screen rotation and UI display. However, setting-related bugs occur when developers do not fully align their apps with the extensive range of system settings that users can define. These bugs can commonly affect apps' UI, causing setting-related UI display (SUD) bugs that negatively impact user experience. While existing research has explored automated detection of SUD bugs, these approaches often suffer from false negatives. This limitation stems from an incomplete understanding of how app components should adapt UI elements to diverse system settings. To address this gap, we conducted an empirical study to identify common patterns of unexpected setting adaptations that result in SUD bugs. These patterns then served as the test oracle for our proposed automated tool, SUDFinder. To ensure the test coverage, SUDFinder injects a test activity to visually render the XML configuration files of each UI page. We evaluated SUDFinder on 29 popular, open-source apps on F-Droid and found that it effectively identifies 98 previously unknown SUD bugs, achieving a precision of 0.76. So far, 67 have been confirmed and 37 have been fixed by the app developers.
