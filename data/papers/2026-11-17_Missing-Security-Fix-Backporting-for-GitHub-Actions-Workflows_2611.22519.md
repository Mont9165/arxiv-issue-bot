# Missing Security-Fix Backporting for GitHub Actions Workflows

- arXiv ID: `2611.22519v1`
- Authors: Chengyan Ma, Jieke Shi, Ruidong Han, Weifeng Sun, Yuqing Niu, Yunbo Lyu, Zhou Yang, David Lo
- Published: 2026-11-17
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2611.22519v1) | [pdf](https://arxiv.org/pdf/2611.22519v1)

## Abstract

GitHub natively supports workflow automation through GitHub Actions, now the dominant CI/CD tool on the platform. Yet keeping these workflows secure remains an ongoing burden: maintainers often patch a vulnerability on the default branch but leave the same flaw on the release and maintenance branches that downstream consumers continue to build from. Carrying a known fix onto these divergent branches, called backporting, is rarely done, and this paper presents the first large-scale empirical study quantifying the resulting gap. From a public corpus of GitHub Actions workflow histories, we mine 1,903,191 workflow-modifying commits, scan each before and after with the static scanner zizmor to identify 69,865 security fixes across 24,238 projects, and audit every release branch to check whether each fix was carried over. The gap is pervasive: 224,392 of 474,490 audited release branches remain vulnerable, and deliberate backporting is rare and slow, with only 19,476 of 78,907 already-fixed branches confirmed as plausible backports at a median lag of 243 days. We thus design WorkflowBP, the first technique for automated security-fix backporting of GitHub Actions workflows. WorkflowBP takes a neuro-symbolic approach: it compiles a default-branch fix into a domain-specific representation called the Workflow Semantic Patch (WSP) and applies it to each divergent branch by matching jobs and steps based on their content rather than their position, while an LLM synthesizes the WSP for the most divergent cases the deterministic engine cannot resolve. On 12,000 real unpatched workflow files from our study, WorkflowBP produces a scanner-checked backport for 67.9%. We further submit 176 issues with WorkflowBP-generated backports to real-world projects, 44 of which have been confirmed or fixed by developers.
