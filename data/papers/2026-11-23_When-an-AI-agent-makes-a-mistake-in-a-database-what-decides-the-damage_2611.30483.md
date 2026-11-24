# When an AI agent makes a mistake in a database, what decides the damage?

- arXiv ID: `2611.30483v1`
- Authors: Abdullah Kaya, Cevheri Bozoglan, Yusuf Gundogdu
- Published: 2026-11-23
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2611.30483v1) | [pdf](https://arxiv.org/pdf/2611.30483v1)

## Abstract

AI agents now run statements against production databases, and several of the incidents that followed deleted production data, which came back only through backups or the provider's help. We ask what decides the damage when such an agent makes a mistake: the model, a guard layer in front of the database, or the database engine itself. The study has two preregistered layers. In Layer A, a frozen library of 22 canonical mistakes is applied by script, with no model involved, to four relational engines under five permission arms and two recovery arms, followed by an engine-native recovery drill (792 cells; 874 drill runs including 10-minute repeats). In Layer B, a minimal tool-calling agent driven by six small open-weight models (4B to 12B parameters, plus one 35B mixture-of-experts model with about 3B active, served locally) works on tasks that contain hazards across nine engines: PostgreSQL, MySQL, SQLite, ClickHouse, Apache Cassandra, MongoDB, Valkey, Apache Kafka and OpenSearch (9,468 trials). A secondary run added MariaDB, Redis and Elasticsearch (2,916 trials); each behaved like its closest core engine. Out of the box, the engines differ less in what a mistake destroys than in what they let you undo. Three of the seven preregistered hypotheses met their decision rule: H2 (for one of nine damage classes) and H3 largely by construction of the arms, and H4 only under its original measure. Four did not; one of them (H5) was uninformative, because in its task the agents never found the credential. The post-hoc analyses (S1-S13) are exploratory and uncorrected for multiple comparisons; on PostgreSQL, MySQL, OpenSearch and ClickHouse the preregistered outcome and original-row loss disagree about G1. We report all of them, with every deviation from the preregistration and its timing.
