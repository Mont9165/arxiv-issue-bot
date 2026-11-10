# Safe by Accident: Crash-Testing LLM-Written Code

- arXiv ID: `2611.10585v1`
- Authors: Afridi Mahmud, Md. As-Aid Rahman, Rifat Shahriyar
- Published: 2026-11-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2611.10585v1) | [pdf](https://arxiv.org/pdf/2611.10585v1)

## Abstract

Evaluations of LLM-written code run it once, in one environment, and credit the code with whatever passes. We show that this credit can belong to the environment. We crashed LLM-written backend code just before each database, file and email call, re-ran it as an operator would, and judged the result under two transaction modes of Python's sqlite3: the default, in which the library quietly opens a transaction, and autocommit, in which it does not. Across 9,100 solutions from ten models on 24 backend tasks, more than half (54%) of the database code that survives every crash in the default mode is left half-updated in autocommit mode. This holds for every model, and it hides in ordinary code, including with conn: blocks that look like transactions but open none. Telling the model that its connection is in autocommit mode does not change what the local code models write, while the API models' unsafe share falls by 30 points. Asking for crash safety helps every model, and strong models repair nearly all unsafe code, but often write safe code only when asked. Thus, much of the crash safety that LLM-written database code appears to have is borrowed from the library rather than designed into it, and a second test under a less forgiving configuration reveals the difference.
