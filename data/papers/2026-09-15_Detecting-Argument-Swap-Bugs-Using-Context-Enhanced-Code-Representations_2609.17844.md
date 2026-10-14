# Detecting Argument-Swap Bugs Using Context-Enhanced Code Representations

- arXiv ID: `2609.17844v1`
- Authors: Subrata Das, Ali Aman, Muhammad Asaduzzaman, Kawser Wazed Nafi, Salimur Choudhury
- Published: 2026-09-15
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.17844v1) | [pdf](https://arxiv.org/pdf/2609.17844v1)

## Abstract

Names of source code elements convey rich semantic information and have been widely used in software engineering tasks such as bug detection, code completion, type prediction, and code classification. Prior studies exploit lexical similarity between method arguments and formal parameter names to detect bugs caused by incorrectly ordered arguments, typically relying on establishing mappings between method calls and their corresponding definitions. However, such mappings are often difficult to obtain in dynamically typed languages like Python. In this paper, we present BugProbe, a learning-based approach for detecting incorrectly ordered arguments in Python method calls that does not require call-to-definition mappings. Our approach leverages multiple sources of contextual information, including local context and argument usage context, and combines name-based similarity with machine learning to construct expressive representations of method arguments. We collect a new dataset of 132,739 Python source files from the top-1,000 starred GitHub repositories, yielding 3,371,244 synthetic training examples, and contribute a curated benchmark of 55 real-world argument-swap bugs manually verified from commit histories. We evaluate our approach on this dataset and show that it achieves high accuracy and consistently outperforms a state-of-the-art baseline across standard evaluation metrics. These results demonstrate that effective detection of argument-ordering bugs is possible without relying on explicit call-to-definition resolution, making the approach well suited for dynamically typed language settings.
