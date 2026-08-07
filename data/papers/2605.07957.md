# Similar Pattern Annotation via Retrieval Knowledge for LLM-Based Test Code Fault Localization

- arXiv ID: `2605.07957v1`
- Authors: Golnaz Gharachorlu, Mahsa Panahandeh, Lionel C. Briand, Ruifeng Gao, Ruiyuan Wan
- Published: 2026-05-08
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2605.07957v1) | [pdf](https://arxiv.org/pdf/2605.07957v1)

## Abstract

Software failures remain a major challenge in modern software development, and identifying the code elements responsible for failures is a time-consuming debugging task. While extensive research has focused on fault localization in the system under test (SUT), failures can also originate from faulty system test scripts. This problem, known as Test Code Fault Localization (TCFL), has received significantly less attention despite its importance in continuous integration (CI) environments where large test suites are executed frequently. TCFL is particularly challenging because it typically operates under black-box conditions, relies on limited diagnostic signals such as error messages and partial logs, and involves large system-level test scripts that expand the fault localization search space. In this paper, we propose SPARK, a framework that integrates accumulated debugging knowledge from continuous integration (CI) environments into Large Language Model (LLM)-based TCFL. Given a newly observed failing test case, SPARK retrieves similar fault-labeled test cases from a debugging knowledge corpus and selectively annotates suspicious lines of the failing test based on their similarity to previously observed fault patterns. These annotations guide the LLM's reasoning while maintaining scalability and avoiding the prompt-length explosion common to naive retrieval-augmented approaches. We evaluate SPARK on three industrial datasets containing real-world faulty Python test cases from different software products. The results show that SPARK consistently improves fault localization effectiveness compared to the existing LLM-based TCFL baseline while maintaining comparable inference cost and token usage. In particular, the approach advances the state of the art by identifying more correct faulty locations in complex test cases containing multiple faults.
