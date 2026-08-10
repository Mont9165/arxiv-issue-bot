# Characterizing the Quality Profile of AI-Generated C++ in Production

- arXiv ID: `2608.06640v1`
- Authors: Michael Tran, Fred Lewis, Kun Yang, Saksham Thakur, Aditya Kini, Aditya Patil, Milad Hashemi, Parthasarathy Ranganathan
- Published: 2026-08-06
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2608.06640v1) | [pdf](https://arxiv.org/pdf/2608.06640v1)

## Abstract

The widespread integration of AI coding assistants offers undeniable boosts to engineering velocity. Yet, recent studies point to a growing trade-off, revealing persistent challenges with code quality and maintainability. Industry leaders, including frontier AI labs, echo these concerns. As large language models are increasingly relied upon to author production code, understanding their impact on shipped software quality has become a critical priority. However, assessing these effects in industrial workflows remains difficult due to observability barriers. We study the impact of AI-generated code on production quality within a large enterprise operating global products relied upon by billions of users daily. Driven by this scale and user trust, the organization values code quality and has built thorough observability for every line of code deployed into production, enabling us to overcome measurement barriers to assess these effects.
  This study presents a large-scale empirical analysis of AI-generated C++ code from April 2025 to April 2026, tracking 3.52 million code changes across this enterprise's brownfield codebase. The core purpose is to understand the quality, performance, and maintenance characteristics of AI-generated code compared to human-written code in a production environment at scale. We find that AI-generated C++ code has a distinct quality profile, showing higher rates of interface and coupling burdens, copy and allocation overheads, and a reliance on explicit loops over optimized standard APIs. These issues translate into tangible downstream costs, including increased review effort and a 5-8% increase in compute resource consumption. However, we demonstrate that providing models with targeted, taxonomy-informed feedback can mitigate these effects, leading to an 11.1% reduction in targeted static analysis warnings and improved computational efficiency.
