# Agentic Generation of AST Transformation Rules for Fixing Breaking Updates

- arXiv ID: `2606.24446v1`
- Authors: Frank Reyes, Benoit Baudry, Martin Monperrus
- Published: 2026-06-23
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2606.24446v1) | [pdf](https://arxiv.org/pdf/2606.24446v1)

## Abstract

Modern software projects depend on third-party libraries that evolve continuously, introducing breaking API changes that prevent client code from compiling after a dependency update. When the same library update breaks multiple projects, existing repair approaches generate project-specific patches that cannot be reused, requiring each affected project to be repaired independently. We present BigBag, an agentic framework that generates fixing transformations: structured, executable programs that encode the repair logic at the API level and transfer to any client broken by the same update. We evaluate BigBag on 157 compilation failure breaking dependency updates from the BUMP benchmark, across eight configurations combining four large language models and two AST transformation engines (Spoon and JavaParser). The best configuration achieves a compilable transformation rate of 94.3% and a fix rate of 78.6%. Generated transformations transfer across projects, achieving a cross-project fix rate of 33.3% overall and 80% or above for breaking updates where all clients invoke the affected API element uniformly. These results show that agentic generation of reusable fixing transformations is a viable approach to scalable repair of breaking updates.
