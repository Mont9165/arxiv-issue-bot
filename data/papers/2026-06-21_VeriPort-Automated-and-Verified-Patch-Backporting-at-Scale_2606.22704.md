# VeriPort: Automated and Verified Patch Backporting at Scale

- arXiv ID: `2606.22704v1`
- Authors: Jonah Ghebremichael, Wenxin Jiang, Mikola Lysenko, Benjamin Barslev Nielsen, William Enck, Alexandros Kapravelos
- Published: 2026-06-21
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.22704v1) | [pdf](https://arxiv.org/pdf/2606.22704v1)

## Abstract

One of the key challenges for securing the software supply chain is addressing known vulnerabilities in third-party open-source dependencies. Security patches are frequently only available for the latest version of a dependency, leaving developers with the choice of either upgrading to the latest version (risking breaking changes) or manually backporting the security fix. Prior work backports to a single version that must be specified in advance and does not produce sufficient evidence to demonstrate that their patches block exploitation and preserve functionality. In this paper, we present VeriPort, an end-to-end agentic system that scalably backports a patch for a given vulnerability advisory to every affected version of the package. For each backport, VeriPort builds a chain of evidence to confirm that the patch blocks exploitation and preserves intended behavior. VeriPort reliably resolves 95.3% of 128 backporting tasks in BackportBench, outperforming the best existing solution (Claude Code) by 22.7 percentage points. We further deployed VeriPort on 169 high- and critical-severity CVEs and have generated over 5,000 verified backported patches. Moreover, VeriPort's value extends beyond simply backporting patches. It uncovered 2,100 versions incorrectly reported as affected and 127 previously unidentified vulnerable versions across 92 advisories, and 23 advisories have since been corrected upstream by removing 387 versions and adding 81.
