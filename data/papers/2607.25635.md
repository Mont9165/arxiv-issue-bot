# An Empirical Study of Model Context Protocol Applications

- arXiv ID: `2607.25635v1`
- Authors: Muhammad Hamza Arshad Majeed, May Mahmoud, Sarah Nadi
- Published: 2026-07-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.25635v1) | [pdf](https://arxiv.org/pdf/2607.25635v1)

## Abstract

The Model Context Protocol (MCP) standardizes how large language model applications communicate with external tools, but leaves the application side unspecified: unlike traditional dependencies resolved through package managers, developers integrating MCP servers face no conventions for configuration, communication, or human oversight. This ecosystem is also under-researched, with existing work focused on servers rather than the applications consuming them. We conduct a large-scale study of 1,723 MCPApps mined from GitHub. We first derive MCPAppTax from a representative sample, then use an LLM-assisted pipeline to apply it across the full dataset, characterizing server integration across configuration, SDK use, and human-in-the-loop mechanisms. Our results show that the ecosystem has converged on some practices but not others: most MCPApps configure servers using files (85.2%) and use an official SDK (81.1%) to communicate with servers, yet no naming convention has emerged for configuration files. Human oversight diverges most, logging (90.8%) and enable/disable controls (77.2%) are common, but only 37.2% gate tool execution behind a blocking approval step, leaving the LLM able to invoke any enabled tool unconditionally in most MCPApps.
