# Verifying Isolation Levels of Database Implementations for Free Using Separation Logic

- arXiv ID: `2607.15877v1`
- Authors: Anders Alnor Mathiasen, Amin Timany, Lars Birkedal
- Published: 2026-07-17
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2607.15877v1) | [pdf](https://arxiv.org/pdf/2607.15877v1)

## Abstract

Modern databases are highly concurrent and provide transactions as a mean of grouping several database operations into atomically applied units. Database vendors and software engineers use isolation levels to describe the consistency guarantees of transactions. The popular isolation levels give weak guarantees, with intricate semantics, to optimize performance of applications. The problem of assuring that database implementations actually implement the isolation level guarantees that application developers build their systems upon has received a great deal of attention from the testing community. But until now, there exists no method for formally verifying that a database implementation actually implements the isolation level that database vendors says it provides. In this paper, we present a method for verifying that a database implements an isolation level: we derive isolation levels directly, as formalized in transactional consistency models by the database community, from the structure of separation logic specifications. By doing so, we consider all program executions that a database and arbitrary clients of the database could produce. The result is a so-called free theorem meaning that any database implementation, whose operations are verified against a specific set of separation logic specifications, actually implements its isolation level. As all proofs in this paper are mechanized in the Rocq proof assistant and build upon a detailed semantic model of program execution, we believe this contribution raises the bar for the achievable robustness of databases.
