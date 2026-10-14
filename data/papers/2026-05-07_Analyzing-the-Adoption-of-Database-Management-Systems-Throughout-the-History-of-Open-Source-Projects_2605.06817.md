# Analyzing the Adoption of Database Management Systems Throughout the History of Open Source Projects

- arXiv ID: `2605.06817v1`
- Authors: Camila A. Paiva, Raquel Maximino, Frederico Paiva, Rafael Accetta Vieira, Nicole Espanha, João Felipe Pimentel, Igor Wiese, Marco Aurélio Gerosa, Igor Steinmacher, Leonardo Murta, Vanessa Braganholo
- Published: 2026-05-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.06817v1) | [pdf](https://arxiv.org/pdf/2605.06817v1)

## Abstract

Database Management Systems (DBMSs) are widely used to store, retrieve, and manage the data handled by modern applications. Although prior work has studied the co-evolution of DBMSs and application source code, less is known about DBMS adoption, co-use, and replacement in real systems. This paper presents a historical study of DBMS usage in 362 popular open-source Java projects hosted on GitHub. We investigated the adoption of the top DBMSs ranked by DB-Engines, covering relational and non-relational systems. Using source-code heuristics, we analyzed DBMS popularity, stability, migration patterns, co-occurrence, and the role of Object-Relational Mappers (ORMs). Our findings show that MySQL and PostgreSQL are the most popular DBMSs in our corpus. Among non-relational DBMSs, Redis and MongoDB are the most frequently used and tend to remain stable after adoption. In contrast, systems such as HyperSQL are more often replaced as projects evolve. We also observed frequent co-use of multiple DBMSs, suggesting patterns of polyglot persistence in which projects combine systems to handle different data needs. Finally, we found that ORM frameworks are commonly used to mediate interactions between applications and DBMSs. Overall, our study provides empirical evidence on how DBMSs are adopted, combined, and replaced over time, offering guidance for developers, architects, educators, and DBMS vendors.
