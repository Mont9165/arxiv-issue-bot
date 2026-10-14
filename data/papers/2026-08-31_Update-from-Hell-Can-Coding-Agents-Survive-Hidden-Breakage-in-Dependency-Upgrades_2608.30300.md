# Update from Hell: Can Coding Agents Survive Hidden Breakage in Dependency Upgrades?

- arXiv ID: `2608.30300v1`
- Authors: Zijian Luo, Runzhi He, Pengfei Gao, Yu Kang, Zeqi Lin, Minghua Ma, Qingwei Lin, Saravan Rajmohan, Yongqiang Tian
- Published: 2026-08-31
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2608.30300v1) | [pdf](https://arxiv.org/pdf/2608.30300v1)

## Abstract

Modern software systems rely heavily on third-party dependencies, but upgrading those dependencies remains a costly maintenance activity. Dependency upgrades do not always preserve the function signatures, type systems, APIs, or runtime semantics assumed by existing code. Consequently, developers often need to perform source code adaptations to accommodate dependency-induced changes. However, such code-level changes are often not explicitly communicated to project maintainers, posing a significant challenge to software reliability.
  Meanwhile, coding agents have emerged as a new form of software development tool and are increasingly adopted by developers due to their automation capabilities. In this paper, we introduce DEPBENCH, a benchmark consisting of 203 real-world dependency-upgrade tasks across five package ecosystems spanning five language communities, each involving hidden code-level changes that require source code adaptation. We evaluate mainstream coding agents on DEPBENCH. The best completed configuration solves only 104/203 tasks (51.2%), with substantial variation across agent harnesses, models, and ecosystems, highlighting an important gap between current agent capabilities and real-world software maintenance needs.
