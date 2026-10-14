# DexterSQL: Deep Schema Exploration and Rule-based Correction for Text-to-SQL Generation

- arXiv ID: `2608.11889v1`
- Authors: Anik Pramanik, Murat Kantarcioglu, Vincent Oria, Shantanu Sharma
- Published: 2026-08-12
- Primary category: `cs.DB`
- Categories: `cs.DB`, `cs.AI`, `cs.CL`, `cs.IR`
- Links: [abs](http://arxiv.org/abs/2608.11889v1) | [pdf](https://arxiv.org/pdf/2608.11889v1)

## Abstract

Prompting-based (\textit{i}.\textit{e}., non-fine-tuning) Text-to-SQL methods, where underlying large language model parameters are not changed for the task, face three problems: (\textit{i})~relying on coarse-grained schema information that may not reveal the fine-grained relationships needed to distinguish ambiguous columns, (\textit{ii})~not capturing recurring SQL-generation failures, and (\textit{iii})~suffering from omission, hallucination, or misplacement of conditions in complex questions.
  This paper develops \textsc{DexterSQL}, a prompting/non-fine-tuning-based Text-to-SQL system that improves SQL generation with three novel components: (\textit{i})~\emph{deep schema explorator} that identifies ambiguous columns, analyzes their individual and joint data distributions to uncover their relationships and the distinct role of each, (\textit{ii})~\emph{database-agnostic rule creator} that mines mismatches between generated and gold SQL only on the training database and converts them into database-agnostic corrective rules that capture recurring LLM failure patterns; and (\textit{iii})~\emph{multi-path SQL generation} that introduces a dependency-tree-based intermediate representation that uses the question's sentence structure to guide its decomposition into an SQL skeleton for final SQL generation.
  \textsc{DexterSQL} achieves a higher accuracy compared to the state-of-the-art using both open-source/weight and closed-source/weight models. Particularly, \textsc{DexterSQL}'s shows a high improvement of at least 2.7\% using an open-weight model (GPT-OSS-120B) on BIRD-Dev, with total accuracy 67.6\%. \textsc{DexterSQL} also shows better improvement of at least 0.9\% using closed-weight models, with total accuracy 71.6\% and 72.2\% on BIRD-Dev with GPT-4o and GPT-5.2.
