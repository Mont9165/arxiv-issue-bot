# A Model-Driven Approach to Database Migration with a Unified Data Model

- arXiv ID: `2604.22415v1`
- Authors: María J. Ortín, José R. Hoyos, Jesus García-Molina
- Published: 2026-04-24
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2604.22415v1) | [pdf](https://arxiv.org/pdf/2604.22415v1)

## Abstract

Database migration is a key task in software modernization, increasingly involving transformations across heterogeneous data models such as relational and NoSQL systems. Existing approaches are typically designed for specific source-target combinations, which limits their applicability in multi-model environments.
  This paper proposes a generic database migration approach based on the U-Schema unified data model, which acts as a pivot representation. By defining mappings between each data model and U-Schema, the approach reduces the number of required transformations and enables schema conversion across heterogeneous paradigms. Trace information is generated during schema transformation to capture correspondences between source and target elements, and is subsequently used to guide data migration in a decoupled manner.
  The approach has been implemented and evaluated through experiments covering schema-level validation, data-level semantic preservation, and performance analysis. The results show that the migration pipeline achieves high structural preservation under round-trip reconstruction, produces document schemas consistent with the intended design decisions, and preserves query behavior across a variety of access patterns, including joins, aggregations, and nested structures. Performance results demonstrate the feasibility of the approach for datasets of increasing size.
  The evaluation focuses on relational-to-document migration using both synthetic datasets and the Northwind benchmark. While this scenario provides a concrete instantiation, the approach is designed to support multiple data models within a unified framework.
