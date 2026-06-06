# A Taxonomy of Runtime Faults in Model Context Protocol Servers

- arXiv ID: `2606.05339v1`
- Authors: Joshua Owotogbe, Indika Kumara, Willem-Jan van den Heuvel, Damian Andrew Tamburri, Antonio Ken Iannillo, Roberto Natella
- Published: 2026-06-03
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2606.05339v1) | [pdf](https://arxiv.org/pdf/2606.05339v1)

## Abstract

MCP (Model Context Protocol) enables LLMs (Large Language Models) to interact with external tools and data sources via a standardized protocol. Its rapid adoption in tool-augmented Artificial Intelligence (AI) workflows has introduced new reliability challenges, such as configuration parameters that are accepted but not enforced at runtime, leading to unintended default behavior, whose runtime fault characteristics remain empirically unexamined. We present the first empirical taxonomy of runtime faults in MCP servers. We manually analyzed 837 MCP-specific runtime fault threads from 473 actively maintained MCP server GitHub repositories and derived a taxonomy using a bottom-up open coding procedure. The taxonomy comprises 11 top-level categories and 27 subcategories (73 leaf fault types), covering recurrent failures across protocol interactions, tool invocations, schema enforcement, state management, model-provider integration, security validation, and timeouts or explicit cancellations of in-progress operations. To assess the taxonomy's external validity, we surveyed 55 MCP server developers. Respondents reported experiencing an average of 20 of the 27 fault subcategories, and no category remained unobserved. These results indicate that the taxonomy reflects widely observed runtime failures in MCP-based systems and shall assist AI software maintenance and evolution in the future.
