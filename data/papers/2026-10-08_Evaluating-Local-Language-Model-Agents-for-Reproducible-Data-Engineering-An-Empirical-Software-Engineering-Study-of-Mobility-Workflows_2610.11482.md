# Evaluating Local Language Model Agents for Reproducible Data Engineering: An Empirical Software Engineering Study of Mobility Workflows

- arXiv ID: `2610.11482v1`
- Authors: Jorge García-Carrasco, Javier Sanchis, Alejandro Reina-Reina, Alejandro Maté, Juan Trujillo
- Published: 2026-10-08
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.AI`, `cs.DB`, `cs.LG`
- Links: [abs](http://arxiv.org/abs/2610.11482v1) | [pdf](https://arxiv.org/pdf/2610.11482v1)

## Abstract

Context: Large language model (LLM) agents are increasingly used as software and data-engineering assistants, yet evidence about locally deployable open-weight agents remains limited. Existing evaluations often emphasize textual responses or isolated code generation rather than the validity of complete engineering artifacts.
  Objectives: We evaluate whether local LLM agents can produce correct and reproducible data-engineering artifacts, quantify the effect of a closed-loop workspace condition, and examine trade-offs in model scale, architecture, quantization, runtime, tool use, and failure.
  Methods: We introduce a benchmark of fifteen mobility-workflow tasks covering data discovery, connectors, transport-feed processing, semantic enrichment, feature engineering, validation, visualization, and reporting. Deterministic checkers assess generated scripts, tables, structured files, figures, and reports. Ten local configurations are evaluated in one-shot and closed-loop conditions, with five repetitions per model, mode, and task, yielding 1,500 scored attempts on a consumer-grade GPU.
  Results: Among models larger than two billion parameters, the workspace condition increases pass rates by 26.7-52.0 percentage points over one-shot generation. The strongest configuration reaches 85.3% artifact-level success, and a quantized 9-billion-parameter model reaches 69.3% with an approximately 6.5 GB memory footprint. Gains are largest when intermediate artifacts expose errors the agent can inspect and repair.
  Conclusion: Local open-weight agents can support a meaningful subset of software-intensive data-engineering work, but reliability depends on model capability, task verifiability, and deterministic validation. The benchmark provides a reproducible method for evaluating complete agent configurations before adoption in engineering workflows.
