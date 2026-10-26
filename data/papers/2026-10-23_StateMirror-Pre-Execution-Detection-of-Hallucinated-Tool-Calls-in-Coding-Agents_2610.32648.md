# StateMirror: Pre-Execution Detection of Hallucinated Tool Calls in Coding Agents

- arXiv ID: `2610.32648v1`
- Authors: Shiwen Shan, Yintong Huo, Zhiying Wu, Yuxin Su
- Published: 2026-10-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2610.32648v1) | [pdf](https://arxiv.org/pdf/2610.32648v1)

## Abstract

Large language model (LLM)-based coding agents may propose invalid actions that are not applicable in the execution environment, such as accessing non-existent paths or missing packages. We term this mismatch hallucinated tool use. A preliminary study of 4,398 agent trajectories reveals that these hallucinations are pervasive and costly, requiring a median of 3 additional interaction steps and 22.4K tokens to recover. Existing frameworks rely on reactive, post-execution feedback, wasting runtime resources. Nevertheless, since an agent's execution environment is grounded in concrete codebase and harness components, many action prerequisites can be extracted and validated prior to execution. To this end, we introduce StateMirror, a lightweight pre-execution detector. StateMirror intercepts actions at the harness boundary, extracts state predicates via AST and command analysis, and deterministically validates them against the live repository. By pinpointing exact environment mismatches before execution, StateMirror preempts invalid actions and subsequent recovery cycles. Evaluation on 2,508 actions shows StateMirror achieves 0.940 precision and 0.817 F1 in detecting such hallucinations, surpassing the strongest LLM judge by 35.3% in F1 while reducing median detection latency from 17.73 s to 1.50 ms with zero token consumption. For practical mitigation, StateMirror's pre-execution feedback enables agents to rectify over 95% of hallucinated tool calls. During live mitigation on 79 tasks, StateMirror reduces agent execution time by 15.8% and token consumption by 11.8% while maintaining task resolution.
