# Improved Join Order Optimization for Database Queries using Hybrid Quantum-Classical Approaches for QUBO Problems

- arXiv ID: `2606.16247v1`
- Authors: Nitin Nayak, Tobias Winker, Umut Çalıkyılmaz, Jinghua Groppe, Sven Groppe
- Published: 2026-06-15
- Primary category: `cs.DB`
- Categories: `cs.DB`
- Links: [abs](http://arxiv.org/abs/2606.16247v1) | [pdf](https://arxiv.org/pdf/2606.16247v1)

## Abstract

Efficient query optimization is crucial for relational database systems, especially for optimizing join orders in complex queries. This work introduces a hybrid approach that integrates Eliminating Cartesian Products (ECP) with splitting the QUBO search space (SQSS) to reduce the size of the QUBO problem, minimizing binary variables and constraints. This improves the performance of the quantum algorithm while lowering hardware requirements.
  We evaluate our method using real-world SQL queries from the ErgastF1 dataset on quantum and classical algorithms, including Quantum Annealing (QA), Simulated Annealing (SA), QAOA, and VQE, implemented on D-Wave's Quantum Annealer and universal gate-based simulators.
  Additionally, we analyze the impact of selectivity and SQSS on QUBO weight distribution and algorithmic performance, highlighting optimization efficiency for QA and SA.
  Experimental results show consistent optimal join orders and enhanced query optimization for various selectivity conditions, and they also highlight the limitations of current quantum hardware for complex queries. This study further confirms the potential of hybrid quantum-classical methods for scalable quantum-enhanced database optimization.
