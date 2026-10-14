# Mind your key: An Empirical Study of LLM API Credential Leakage in iOS Apps

- arXiv ID: `2606.12212v1`
- Authors: Pinran Gao, Lingxiang Wang, Ying Zhang, Fan Yang
- Published: 2026-06-10
- Primary category: `cs.SE`
- Categories: `cs.SE`, `cs.CR`
- Links: [abs](http://arxiv.org/abs/2606.12212v1) | [pdf](https://arxiv.org/pdf/2606.12212v1)

## Abstract

The rapid integration of large language models (LLMs) into mobile applications has introduced a new class of credential security risk: leaked credentials that grant unauthorized access to LLM inference services, causing financial damage to developers. Prior work on credential leakage has focused primarily on Android apps; to date, no empirical study has systematically investigated LLM API key leakage in iOS applications.
  We present the first in-depth empirical study of API key leakage in LLM-integrated apps. We construct a high-quality dataset of 444 iOS applications, filtered from 1092 candidates through a standardized process, and develop LLMKeyLens, a dynamic analysis framework that detects LLM API key leakage via traffic interception, provider-specific key extraction, and active validity confirmation, requiring neither source code access nor binary decryption. Our analysis reveals that 282 applications expose exploitable LLM API credentials in network traffic, spanning at least ten providers. We identify three leakage patterns: JWT-based token leakage (48%), unauthenticated backend proxy access (33%), and plaintext API key transmission (19%). To assess remediation, we re-analyzed the same 282 vulnerable applications three months after responsible disclosure; only 28% had remediated the reported vulnerability, while 72% remained exploitable, with persistent issues stemming from unauthenticated backends and broken JWT implementations.
  Our findings show that LLM API key leakage is both prevalent and persistent in the iOS ecosystem, exposing a systemic gap between developer practice and secure integration principles, and suggest that secure LLM integration requires not only developer awareness but also explicit security guidance from providers and platform-level enforcement.
