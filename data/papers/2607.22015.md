# Are Production Cloud Skills Adequately Tested? Measuring and Governing Skill Test Coverage in Practice

- arXiv ID: `2607.22015v1`
- Authors: Haotian Si, Junyi Chen, Shuyang Yu, Ruifeng Nie, Jiate Li, Jianqiang Zhao, Meng Li, Dengcheng He
- Published: 2026-07-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2607.22015v1) | [pdf](https://arxiv.org/pdf/2607.22015v1)

## Abstract

Cloud platforms increasingly deliver reusable Cloud Skills that guide AI agents in creating, configuring, monitoring, and troubleshooting cloud resources. Workflow-oriented Skills specify multiple resource operations, user choices, validation steps, and recovery behavior. Existing Skill evaluation primarily measures whether a Skill improves task success. Passing the available testcases, however, does not reveal which behaviors specified by the Skill have never been tested. This paper introduces Skill Test Coverage, which measures how completely a Skill's test suite covers its operational test obligations. We define the coverage units, testcase coverage relation, calculation procedure, and claim boundary. Because these units and links are not explicit in natural-language Skill packages, we develop a measurement pipeline that recovers operational obligations, organizes their workflow context, maps testcases using both user prompts and initial resource states, and produces an auditable coverage report. Model-assisted candidate generation is combined with expert review to ensure that the reported coverage remains grounded in the original Skill and testcase evidence. A post-review module then translates confirmed coverage gaps into source-grounded test-improvement recommendations.
