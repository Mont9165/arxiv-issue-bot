# Astragalus: Automatic Configuration Repair for Production Networks

- arXiv ID: `2605.22092v1`
- Authors: Zhenrong Gu, Peng Zhang, Xing Feng, Xu Liu
- Published: 2026-05-21
- Primary category: `cs.NI`
- Categories: `cs.NI`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.22092v1) | [pdf](https://arxiv.org/pdf/2605.22092v1)

## Abstract

Network configurations are prone to errors, which can lead to catastrophic service outages. A tool that can achieve automatic configuration repair (ACR) is highly desired by operators. Existing tools for ACR follow a semantic-driven approach: they model network semantics as a set of SMT constraints, and solve them for a location or fix of the error. Due to the complex semantics of networks, constructing and solving these constraints can be prohibitively expensive, making these tools neither general nor scalable. Inspired by automatic program repair (APR), we explore another direction, i.e., a syntax-driven approach, which tries to repair program bugs by ``grafting'' some existing code in the same repository, without modeling program semantics. Following this direction, we propose Astragalus, a syntax-driven method for ACR. It uses multiple iterations of a ``localize-fix-validate'' pipeline to search for repairs, and proves quite effective on configurations of our production network. Specifically, we show that Astragalus can repair every incident in multiple sizes of a synthesized network, and 97.5\% of the incidents on a real network, both with 15 types of errors injected, within an average time of 7.36 seconds. It has also provided valid repair options in under 6 minutes for 4 recent network incidents or undesired changes, in a real production network with O(1,000)Õ(10,000) devices.
