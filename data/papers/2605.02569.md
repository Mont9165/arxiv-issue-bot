# Static Type Checking for Database Access Code

- arXiv ID: `2605.02569v1`
- Authors: Thomas James Kirz, Werner Dietl, Mattias Ulbrich, Stefanie Scherzinger
- Published: 2026-05-04
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.PL`
- Links: [abs](http://arxiv.org/abs/2605.02569v1) | [pdf](https://arxiv.org/pdf/2605.02569v1)

## Abstract

JDBC remains a key technology for database access in Java applications. Since the database dictionary and the Java type system have distinct scopes, developers inevitably need to deal with bugs in SQL-to-Java type mappings. We propose an extension of the Java compiler, based on the established Checker Framework, which allows us to bridge this gap. Our approach verifies statically that the correct Java types are used when setting prepared statement parameters or when getting values from result sets. This allows us to lift a practically important class of runtime errors to compile time. Our approach is sound and, therefore, is guaranteed not to produce false negatives. Our prototype implementation also offers a degraded mode for type-checking legacy software, if developers are only interested in a subset of errors. Our experiments show that our approach detects a wide range of type mismatches in realworld application code and can indeed prevent errors which might otherwise surface as runtime errors. From the perspective of the developer, our approach is extremely lightweight: it processes the unmodified Java code, yet developers may add their own annotations. This allows us to perform type-checking even across method boundaries, whereas commercial developer tools are restricted to local checks. Finally, we show that we can type-check real-world JDBC software with reasonable overhead during compilation.
