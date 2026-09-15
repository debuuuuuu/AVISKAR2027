# Annotated Bibliography & References

This document catalogs the verified academic literature, specifications, and primary sources that form the theoretical, empirical, and architectural foundation of the **Trust-Aware Service Selection** framework.

---

## 1. Primary Empirical Anchor

```text
[1] Xiong, X., Li, Z., Wei, W., Wang, Q., Knottenbelt, W. J., & Wang, Z. (2026).
    Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem.
    arXiv preprint arXiv:2606.26028 [cs.CR].
    URL: https://arxiv.org/abs/2606.26028
```
- **Context:** First comprehensive empirical study of the ERC-8004 decentralized agent standard on Ethereum, BSC, and Base.
- **Key Evidence Used:** Documented 3–15% endpoint availability and 59.2–90.6% coordinated Sybil reviewers. Serves as our primary real-world baseline showing why raw reputation fails.

---

## 2. Multi-Agent Systems, Provenance, & Decentralized Trust

```text
[2] Chishti, M. S., Oyinloye, D. P., & Li, J. (2026).
    AgentReputation: A Decentralized Agentic AI Reputation Framework.
    arXiv preprint arXiv:2605.00073 [cs.AI].
    URL: https://arxiv.org/abs/2605.00073
```
- **Context:** Framework exploring decentralized reputation scoring for AI agents.
- **Relevance & Distinction:** Focuses on reputation aggregation across decentralized networks; our project differs by investigating task-specific interaction evidence rather than reputation-only scoring.

```text
[3] Zhu, L., Li, Y., Wang, T., Chen, Z., Li, K., Liu, H., Wang, Y., Xu, L., Jiang, P., Zhang, Z., et al. (2026).
    Blockchain Empowered Trustworthy Agent Networks: Foundations, Taxonomy, and Future Directions.
    arXiv preprint arXiv:2608.04626 [cs.DC].
    URL: https://arxiv.org/abs/2608.04626
```
- **Context:** Survey and architectural taxonomy of blockchain applications for autonomous multi-agent networks.
- **Relevance:** Informs our design of tamper-evident state commitments, smart contract anchors, and decentralized provenance.

```text
[4] IEEE eScience. (2025).
    PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows.
    2025 IEEE International Conference on eScience, pp. 1-10.
    DOI: 10.1109/eScience65000.2025.00093
    URL: https://ieeexplore.ieee.org/document/11181558/
```
- **Context:** Formalizes provenance modeling for multi-agent execution graphs.
- **Relevance:** Informs our Evidence Model data schemas, ensuring full traceability from task input to execution output and verification verdict.

```text
[5] Liu, B., Che, H., & Li, Y. (2026).
    TrustRAG: Blockchain-Enhanced RAG via Committee-Based Credibility Scoring.
    arXiv preprint arXiv:2608.20097 [cs.CR].
    URL: https://arxiv.org/abs/2608.20097
```
- **Context:** Explores combining blockchain credibility anchors with Retrieval-Augmented Generation.
- **Relevance:** Informs our RAG evidence retrieval pipeline, specifically mitigating hallucinated or ungrounded evidence records.

---

## 3. Foundational Multi-Agent Trust Theory

```text
[6] Sabater, J., & Sierra, C. (2002).
    REGRET: A reputation model for multi-agent systems.
    Autonomous Agents and Multi-Agent Systems, 5(1), 33–55.
    DOI: 10.1023/A:1015505024479
```
- **Foundational Impact:** Introduced multi-faceted reputation modeling (direct experience, witness reports, neighborhood credibility) with time decay.

```text
[7] Jøsang, A., & Ismail, R. (2002).
    The beta reputation system.
    Proceedings of the 15th Bled Electronic Commerce Conference, 41, 2502–2511.
```
- **Foundational Impact:** Formulated Bayesian trust updates using Beta probability distributions over binary execution outcomes.

```text
[8] Yu, H., Shen, Z., Miao, C., Leung, C., & Niyato, D. (2013).
    A survey of multi-agent trust management systems.
    IEEE Access, 1, 35–50.
    DOI: 10.1109/ACCESS.2013.2259838
```
- **Foundational Impact:** Taxonomic survey of attack vectors (Sybil attacks, collusive rating, whitewashing) in distributed multi-agent systems.

```text
[9] Marsh, S. (1994).
    Formalising Trust as a Computational Concept.
    Ph.D. Thesis, University of Stirling.
```
- **Foundational Impact:** First formal mathematical conceptualization of trust as a context-dependent computational decision variable.

---

## 4. Protocols & Technical Specifications

```text
[10] Anthropic. (2024).
     Model Context Protocol (MCP) Specification.
     URL: https://modelcontextprotocol.io
```
- **Role:** Industry open standard for AI agent tool and resource invocation.

```text
[11] Merkle, R. C. (1987).
     A Digital Signature Based on a Conventional Encryption Function.
     Advances in Cryptology — CRYPTO '87, Lecture Notes in Computer Science, 293, 369–378.
```
- **Role:** Theoretical basis for cryptographic state commitments and Merkle trees used in evidence anchoring.

```text
[12] IETF. (2024).
     HTTP 402 Payment Required Standard & Agent Extensions (x402).
     Specification RFC Draft.
```
- **Role:** Foundation for planned Phase 10 autonomous payment extensions.
