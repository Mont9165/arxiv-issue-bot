# Does AI-Assisted Development Homogenize Software? An Empirical Study of Code Similarity, Quality, and Evolution

- arXiv ID: `2610.24093v1`
- Authors: Luciano Marchezan, Romain Lefeuvre, Kevin Delcourt, Benoit Combemale, Houari Sahraoui
- Published: 2026-10-16
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2610.24093v1) | [pdf](https://arxiv.org/pdf/2610.24093v1)

## Abstract

AI-assisted software development is evolving from interactive LLM assistance toward agentic systems that autonomously perform software engineering tasks, yet the effects of this shift remain insufficiently understood. We present an empirical study of 50 long-lived Java and Python open-source projects across three eras: pre-LLM, potentially LLM-assisted, and detected agentic development. Using snapshots from Software Heritage, we examine code similarity, software quality, and software evolution. Similarity is measured semantically through embedding-based cosine similarity and syntactically through CodeBLEU*. Quality is assessed with SonarQube metrics covering maintainability, complexity, reliability, and security. Evolution is characterized by annualized growth rates of LOC, functions, classes, files, and statements, and by commit activity in the three months preceding each snapshot. Results show no consistent evidence of increased similarity as semantic and syntactic similarity decreased significantly in Java for both the LLM and agentic eras relative to the pre-LLM era, while Python showed no significant differences. Software quality remained largely stable, although the agentic era showed significantly lower code-smell and SQALE index densities. Structural growth was generally lower in the agentic era, particularly for files, whereas development activity increased moderately in Java, especially in commits and added lines. These findings challenge the assumption that LLM- and agent-assisted development necessarily homogenizes code, degrades quality, or accelerates growth.
