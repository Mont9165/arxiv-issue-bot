# Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models

- arXiv ID: `2604.21860v1`
- Authors: Naheed Rayhan, Sohely Jahan
- Published: 2026-04-23
- Primary category: `cs.CR`
- Categories: `cs.CR`, `cs.AI`
- Links: [abs](http://arxiv.org/abs/2604.21860v1) | [pdf](https://arxiv.org/pdf/2604.21860v1)

## Abstract

Large language models (LLMs) are increasingly integrated into sensitive workflows, raising the stakes for adversarial robustness and safety. This paper introduces Transient Turn Injection(TTI), a new multi-turn attack technique that systematically exploits stateless moderation by distributing adversarial intent across isolated interactions. TTI leverages automated attacker agents powered by large language models to iteratively test and evade policy enforcement in both commercial and open-source LLMs, marking a departure from conventional jailbreak approaches that typically depend on maintaining persistent conversational context. Our extensive evaluation across state-of-the-art models-including those from OpenAI, Anthropic, Google Gemini, Meta, and prominent open-source alternatives-uncovers significant variations in resilience to TTI attacks, with only select architectures exhibiting substantial inherent robustness. Our automated blackbox evaluation framework also uncovers previously unknown model specific vulnerabilities and attack surface patterns, especially within medical and high stakes domains. We further compare TTI against established adversarial prompting methods and detail practical mitigation strategies, such as session level context aggregation and deep alignment approaches. Our study underscores the urgent need for holistic, context aware defenses and continuous adversarial testing to future proof LLM deployments against evolving multi-turn threats.
