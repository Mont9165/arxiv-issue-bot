# Discovery Agents for Real-Time Analytics: Toward Proactive Insight Systems

- arXiv ID: `2605.27571v1`
- Authors: Gaetano Rossiello, Dharmashankar Subramanian
- Published: 2026-05-26
- Primary category: `cs.AI`
- Categories: `cs.AI`, `cs.CL`, `cs.DB`
- Links: [abs](http://arxiv.org/abs/2605.27571v1) | [pdf](https://arxiv.org/pdf/2605.27571v1)

## Abstract

Modern analytics systems are fundamentally reactive, requiring users to define queries over increasingly complex and continuously evolving data. In real-time streaming environments, this paradigm breaks down, as the space of potential insights becomes too large to enumerate manually. We present a multi-agent architecture for autonomous insight discovery over real-time data streams. The system implements a continuous discovery loop in which agents generate hypotheses, compile them into executable analytics, validate generated artifacts, and produce visualizations and deployable applications. The architecture leverages Apache Kafka for event-driven coordination, Apache Flink for stream processing, and large language models to implement specialized agents. A key contribution is a contract-driven design based on typed intermediate artifacts, enabling modularity, observability, lineage, and safer execution of dynamically generated analytics. Through use cases in retail, finance, and public data, we show how this architecture supports a shift from query-driven analytics to proactive, discovery-driven systems.
