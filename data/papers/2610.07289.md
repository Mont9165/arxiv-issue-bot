# Catching Developers in the Flow: Low-Latency Agentic Program Repair at Google Scale

- arXiv ID: `2610.07289v1`
- Authors: Celal Ziftci, Spencer Greene, Ray Liu, Livio Dalloro, Lorenzo Dini
- Published: 2026-10-05
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.07289v1) | [pdf](https://arxiv.org/pdf/2610.07289v1)

## Abstract

Manual repair of program failures is time-consuming and disruptive for software developers, particularly during the pre-submit phase where test failures occur within continuous integration systems. While Automated Program Repair has seen significant advancement through Large Language Models, existing state-of-the-art techniques primarily focus on post-submit workflows, operating offline without the low-latency requirements necessary to assist developers in real-time within their flow before they switch context.
  In this paper, we introduce FlowAgent, an AI agent deployed at Google to automatically repair test failures in the pre-submit outer-loop workflow inside continuous integration systems. Integrated into Google's internal developer tools, Critique and Cider,FlowAgent utilizes a ReAct-style generate-and-validate loop, as well as rigorous pre-execution and post-execution abstention filters to ensure high-quality suggestions under strict latency constraints.
  Based on our case studies, FlowAgent is highly effective. First, a manual evaluation conducted on 195 real-world test failures demonstrated 67.18% accuracy in suggesting correct fixes. Following its Google-wide deployment, FlowAgent suggested fixes on 295,508changes, of which developers previewed 65,069 and applied 28,554. Developer feedback from interviews indicate that the agent is useful in suggesting correct fixes, integration of autonomous repair agents into industrial software engineering workflows is received well, while interesting challenges and opportunities still remain.
