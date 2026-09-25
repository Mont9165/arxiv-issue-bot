# Human-AI Collaboration for Multi-Line Task Adjustment Using Local Large Language Models and a Digital Twin

- arXiv ID: `2609.29061v1`
- Authors: Teng-Hsien Ko, Chin-Te Lin
- Published: 2026-09-24
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.29061v1) | [pdf](https://arxiv.org/pdf/2609.29061v1)

## Abstract

Automation systems must adapt to changing tasks, equipment states, and staffing conditions while providing evidence for human review. This study presents a multi-line task-adjustment system integrating a local large language model, a digital twin, and human decision-making. A Propose-Verify-Decide workflow translates operator intent into structured requirements, generates a bounded set of candidate strategies, and checks semantics, simulation execution, and operational constraints. Linked records preserve traceability from requests to verification evidence and decisions. Thirty fixed test records were evaluated using four virtual surgical-instrument sorting lines: 28 assessed the workflow and two assessed model generation. Eighteen workflow cases met expectations; autonomous strategy-workflow success was 3/10, and correct rejection of invalid inputs was 7/8. All four cases that passed preceding checks, produced complete evidence, and reached final engineering review (CP6) passed that review. Together with the correct blocking of strategies that failed throughput constraints, this supports the effectiveness of staged screening and confirmation within the tested setting. Mean placement-validation pass rate across eight simulation evidence records was 97.50%. Mean times to the first reviewable response and simulation verification, excluding startup, were 12.94 and 164.39 s, respectively. Remaining failures involved semantic distortion, incomplete evidence, and missed invalid inputs. The results demonstrate a traceable strategy-review workflow, but do not establish overall reliability or long-term stability. Broader testing and physical evaluation are needed to assess generalizability.
