# Improving Join Order Optimization on Gate-Based Quantum Computers via Structured Parameter Initialization

- arXiv ID: `2608.20683v1`
- Authors: Divya Shekar, Ruokun Wu, Dhanvi Bharadwaj, Gokul Subramanian Ravi, Lin Ma
- Published: 2026-08-21
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2608.20683v1) | [pdf](https://arxiv.org/pdf/2608.20683v1)

## Abstract

Join Order Optimization (JOO) is one of the most computationally expensive tasks in relational query optimization due to the exponential growth of possible join plans with increasing query size. Recent work has explored quantum and quantum-inspired approaches for solving JOO by reformulating the problem as a Quadratic Unconstrained Binary Optimization (QUBO) problem suitable for optimization using quantum hardware. However, many existing approaches have limited scalability on current gate-based quantum devices. In addition, little work has investigated the role of initialization strategies in improving the performance of gate-based quantum optimization for database workloads. In this work, we investigate gate-based quantum join order optimization using the Quantum Approximate Optimization Algorithm (QAOA) initialized with Scalable Parameter Initialization for QAOA (SPIQ). SPIQ is used to efficiently identify high-quality initial points in the quantum solution landscape for QAOA executed on a gate-based quantum computer. We evaluate the interaction between QUBO encoding, SPIQ initialization, and gate-based optimization on small-scale join ordering problems involving 3 and 4 relations. Our results show that structured initialization improves optimization stability and increases convergence toward high-quality join plans compared to uninformed initialization approaches. Across these small-scale, simulation-based instances, SPIQ increases the sampling frequency of the optimal join order by up to approximately 5$\times$ and yields final-state energies significantly lower than a randomly initialized QAOA. Overall, this work enhances existing gate-based quantum optimization while providing an initial proof of concept for applying SPIQ initialization to database query optimization workloads.
