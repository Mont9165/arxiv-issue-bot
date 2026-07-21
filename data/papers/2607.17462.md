# PSASpotter: A Tool to Detect the Usage of Platform-Specific APIs in Python

- arXiv ID: `2607.17462v1`
- Authors: Ricardo Job, Andre Hora
- Published: 2026-07-20
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.17462v1) | [pdf](https://arxiv.org/pdf/2607.17462v1)

## Abstract

A platform-specific API is implemented for a particular platform (e.g., operating system), thus, it may not work on other platforms than the target one. Detecting the usage of such APIs is important for supporting software maintenance, as it allows maintainers to be alerted about APIs that could pose potential risks. This paper proposes PSASpotter, a tool to detect the usage of platform-specific APIs in Python systems. PSASpotter also identifies whether the platform-specific APIs are used within a defensive code, such as try/except blocks or if blocks that check the current platform. PSASpotter can support the development of novel empirical studies about the usage of platform-specific APIs in the Python ecosystem. Moreover, the defensive code detected by PSASpotter may contain alternative solutions for unavailable APIs, which can provide insights for software development and testing across multiple platforms. PSASpotter is available at: https://github.com/ricardojob/PSASpotter. Tool video: https://youtu.be/d3WyozTAKS8.
