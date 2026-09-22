# An Iterative LangGraph Agent for Text-to-SQL: Natural Language Access to the Chicago Crime Database

- arXiv ID: `2609.22917v1`
- Authors: Vigneshwar Ravi Rao, Rupesh Swarnakar, Fayeq Jeelani Syed†
- Published: 2026-09-19
- Primary category: `cs.CL`
- Categories: `cs.CL`, `cs.AI`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2609.22917v1) | [pdf](https://arxiv.org/pdf/2609.22917v1)

## Abstract

Non-technical stakeholders frequently cannot write the SQL needed to extract insights from operational databases. We built and evaluated a Text-to-SQL agent that closes this gap end to end: a six-node LangGraph StateGraph checks question relevance, fetches the live schema, generates PostgreSQL, validates it with a dry run, retries on failure, executes the query, and narrates the result set in plain English. The agent uses prompt engineering only; no model was fine-tuned. We evaluated it on the Chicago Crime dataset (approximately 8.5 million records, 22 attributes) against a hand-built benchmark of 100 natural language questions with ground-truth SQL, stratified into 30 Easy, 40 Medium and 30 Hard items. Comparing two prompt revisions of the same agent, the revised system (V2) reached a Valid SQL Rate of 93% (from 87%), an Execution Accuracy of 60% under a hybrid relational equivalence metric (from 47%; 19% from 12% under strict JSON matching), and a mean Synthesis Quality of 4.34 out of 5 (from 3.91). The single largest driver was removing a LIMIT 10 instruction from the system prompt, which had been truncating multi-row answers. Error analysis attributes the residual failures to relevance-checker false rejections, ambiguous question semantics, and free-tier API rate limits rather than to the language generation step. We report no comparison against an external baseline system or a public benchmark; the study is a single-model engineering evaluation.
