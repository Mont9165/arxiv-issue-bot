# Exploring the Effectiveness of Abstract Syntax Tree Patterns for Algorithm Recognition

- arXiv ID: `2605.06098v1`
- Authors: Denis Neumüller, Florian Sihler, Raphael Straub, Matthias Tichy
- Published: 2026-05-07
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.06098v1) | [pdf](https://arxiv.org/pdf/2605.06098v1)

## Abstract

The automated recognition of algorithm implementations can support many software maintenance and re-engineering activities by providing knowledge about the concerns present in the code base. Moreover, recognizing inefficient algorithms like Bubble Sort and suggesting superior alternatives from a library can help in assessing and improving the quality of a system. Approaches from related work suffer from usability as well as scalability issues and their accuracy is not evaluated. In this paper, we investigate how well our approach based on the abstract syntax tree of a program performs for automatic algorithm recognition. To this end, we have implemented a prototype consisting of: A domain-specific language designed to capture the key features of an algorithm and used to express a search pattern on the abstract syntax tree, a matching algorithm to find these features, and an initial catalog of "ready to use" patterns. To create our search patterns we performed a web search using the algorithm name and described key features of the found reference implementations with our domain-specific language. We evaluate our prototype on a subset of the BigCloneEval benchmark containing algorithms like Fibonacci, Bubble Sort, and Binary Search. We achieve an average F1-score of 0.74 outperforming the large language model Codellama which attains 0.35. Additionally, we use multiple code clone detection tools as a baseline for comparison, achieving a recall of 0.62 while the best-performing tool reaches 0.20.
