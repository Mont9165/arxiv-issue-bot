# PR-Aware Automated Unit Test Generation: Challenges and Opportunities

- arXiv ID: `2605.25285v1`
- Authors: Vahid Haratian, Atakan Akar, Berk Çakar, Eray Tüzün
- Published: 2026-05-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.25285v1) | [pdf](https://arxiv.org/pdf/2605.25285v1)

## Abstract

Automated test generation has a substantial body of work, yet most studies focus on generating tests for complete software units, such as classes, and rely on metrics such as code coverage for assessment. In contrast, modern software development primarily evolves through small, targeted changes introduced in pull requests (PRs). Despite this, the crucial task of generating tests specifically for these PRs has been overlooked, and the performance of state-of-the-art tools for this purpose remains unknown.
  This study evaluates two distinct approaches for PR-aware test generation: EvoSuite, a leading search-based tool, and GPT-4o, one of the widely used large language models (LLMs). To measure their effectiveness at validating PR-specific changes, we assess their ability to generate fail-to-pass (F2P) test cases, meaning tests that fail on the code before the change and pass on the code after the change.
  Our evaluation shows that EvoSuite outperformed GPT-4o, producing at least one F2P test for a significantly higher percentage of PRs (36 percent vs. 13 percent). The performance of GPT-4o was significantly hampered by a high rate of compilation errors (63 percent), whereas only 2 percent of EvoSuite's generated tests failed to run. Despite EvoSuite's relative success, our findings indicate that both tools are largely ineffective for this task, as they failed to generate any meaningful change-capturing tests for the large majority of the PRs (64 percent).
  Although both generators could not achieve a high F2P ratio in our evaluation, and EvoSuite outperformed GPT-4o, we believe that agentic code generation methods may have significant potential for this task. Ultimately, our work highlights a critical gap in tooling and calls for the development of high-performance test generators tailored to the incremental nature of modern software development.
