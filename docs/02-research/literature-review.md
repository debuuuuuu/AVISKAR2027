# Comprehensive Literature Review: Trust, Reputation, and Verification in Autonomous Agent Systems

This literature review presents a systematic, critical analysis of verified academic foundations, preprints, and official technical specifications supporting the **Trust-Aware Service Selection for Autonomous AI Agents** research project.

To preserve academic honesty, every cited work is classified into its appropriate **Research Family**, with its **Publication Status** explicitly recorded (Peer-Reviewed Journal, Peer-Reviewed Conference, arXiv Preprint, or Official Specification). Preprints are evaluated as working papers rather than peer-reviewed archival publications.

---

## 1. Agent Identity, Decentralized Registries, and Empirical Ecosystem Measurement

### 1.1 The ERC-8004 Standardized Agent Ecosystem
- **Specification:** *ERC-8004: Trustless AI Agent Standard — Identity, Reputation, and Validation Registries* (Ethereum Improvement Proposals, 2025).
- **Publication Status:** Official Technical Specification (EIP-8004).
- **Core Contribution:** ERC-8004 establishes standard EVM smart contracts enabling autonomous AI agents to maintain portable on-chain identities (ERC-721/universal IDs), record publicly verifiable execution attestations (Validation Registry), and submit decentralized feedback scores (Reputation Registry).
- **Operational Reality & Empirical Vulnerability:** While ERC-8004 establishes the infrastructure for permissionless agent discovery, it enforces no guarantees regarding service reachability, runtime availability, or semantic output correctness. Anyone can register an agent contract without deploying a working server.

### 1.2 The Empirical Fragility of Decentralized Agent Registries
- **Key Paper:** Xiong, X., Li, Z., Wei, W., Wang, Q., Knottenbelt, W. J., & Wang, Z. (2026). *Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem.* arXiv:2606.26028 [cs.CR].
- **Publication Status:** arXiv Preprint (Not Peer-Reviewed).
- **Methodology:** Xiong et al. conducted the first longitudinal measurement study of ERC-8004 on-chain data across Ethereum, BNB Smart Chain (BSC), and Base through May 2026, combining smart contract transaction graph analysis with automated endpoint connection probing.
- **Key Findings:**
  1. **Extreme Endpoint Inactivity:** Only **3.0%** of registered agents on Ethereum, **4.0%** on BSC, and **15.0%** on Base exposed reachable, valid JSON-RPC service endpoints. Over 85% to 97% of registered agents were completely dormant or non-functional.
  2. **Rampant Coordinated Sybils:** Sybil reviewer clusters represented **73.5%** of all feedback on Ethereum, **59.2%** on BSC, and **90.6%** on Base.
  3. **Reputation Collapse:** Removing Sybil-flagged feedback caused the reliable rating pool to collapse for the majority of agents on two of the three chains.
- **Relevance & Distinction:** Xiong et al. provides the primary empirical motivation for our project. Their paper performs an *observational measurement audit* of the ERC-8004 registry breakdown. Our project addresses the *solution space*: engineering a client-side selection and verification framework that prevents autonomous agents from falling victim to non-functional endpoints and Sybil-manipulated rating pools.

---

## 2. Classical Multi-Agent Trust and Computational Reputation Systems

Decades before modern large language models, the multi-agent systems (MAS) community formalized computational trust and reputation in open distributed networks.

### 2.1 Foundational Trust Formulations: REGRET and the Beta Reputation System
- **REGRET Model:** Sabater, J., & Sierra, C. (2002). *REGRET: A reputation model for multi-agent systems.* *Autonomous Agents and Multi-Agent Systems*, 5(1), 33–55 (Peer-Reviewed Journal).
  - Sabater and Sierra established the fundamental distinction between **direct experience** (interactions between the agent and provider), **witness reputation** (reports from third-party peers), and **system role reputation**. REGRET introduced recency-weighted exponential decay functions to model behavioral drift.
- **Beta Reputation System:** Jøsang, A., & Ismail, R. (2002). *The Beta Reputation System.* In *Proceedings of the 15th Bled Electronic Commerce Conference*, pp. 2502–2511 (Peer-Reviewed Conference).
  - Jøsang and Ismail provided mathematical rigor using Beta probability density functions $(\alpha, \beta)$ to map binary positive/negative outcomes into statistical expectation values while explicitly quantifying epistemic uncertainty as a function of sample count.

### 2.2 Global Consensus vs. Local Trust: EigenTrust, FIRE, and TRAVOS
- **EigenTrust:** Kamvar, S. D., Schlosser, M. T., & Garcia-Molina, H. (2003). *The EigenTrust algorithm for reputation management in P2P networks.* In *Proceedings of the 12th International Conference on World Wide Web (WWW '03)*, pp. 640–651 (Peer-Reviewed Conference).
  - Demonstrated that global reputation can be mathematically computed via principal eigenvector iterations over normalized peer satisfaction matrices, isolating non-colluding rogue peers in P2P file-sharing networks. However, Kamvar et al. noted that global consensus is vulnerable to collusive rings of malicious peers.
- **FIRE Model:** Huynh, T. D., Jennings, N. R., & Shadbolt, N. R. (2006). *An integrated trust and reputation model for open multi-agent systems.* *Autonomous Agents and Multi-Agent Systems*, 13(2), 119–154 (Peer-Reviewed Journal).
  - Integrated interaction trust, role-based trust, witness reputation, and certified reputation, empirically proving that combining heterogeneous evidence channels substantially outperforms any single trust metric.
- **TRAVOS:** Teacy, W. T. L., Patel, J., Jennings, N. R., & Luck, M. (2006). *TRAVOS: An probabilistic trust and reputation model for open multi-agent systems.* *Autonomous Agents and Multi-Agent Systems*, 12(2), 183–210 (Peer-Reviewed Journal).
  - Formulated a Bayesian framework that evaluates the historical reporting accuracy of third-party witnesses, dynamically discounting ungrounded or deceitful witness opinions.
- **Comprehensive Survey:** Yu, H., Shen, Z., Miao, C., Leung, C., & Niyato, D. (2013). *A survey of multi-agent trust management systems.* *IEEE Access*, 1, 35–50 (Peer-Reviewed Journal).
  - Concluded that computational trust models that operate in a *context-blind* manner inevitably fail when deployed across variable risk environments.

### 2.3 Boundaries of Classical Trust Systems
Classical MAS trust systems were designed for structured, low-dimensional transactions (e.g., e-commerce goods, distributed compute cycles). They operate on scalar ratings (e.g., $[0, 1]$ or 1–5 stars) attached to an agent identity. They cannot evaluate natural language prompts, semantic domain shifts, complex JSON payloads, or non-deterministic foundation model outputs. Our framework adapts their mathematical rigor (Bayesian updating, recency decay, witness discounting) to modern semantic embeddings and programmatic output verification.

---

## 3. Context-Conditioned Agent Reputation

### 3.1 The Competence-Transfer Problem and AgentReputation
- **Key Paper:** Chishti, M. S., Oyinloye, D. P., & Li, J. (2026). *AgentReputation: A Decentralized Agentic AI Reputation Framework.* In *Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering (FSE 2026)* / arXiv:2605.00073 (Peer-Reviewed Conference / Preprint).
- **Core Problem:** In multi-agent AI ecosystems, agent capabilities are highly multidimensional. A coding agent possessing high reliability on basic Python unit tests may exhibit severe vulnerabilities when tasked with smart contract security auditing. General scalar reputation creates a false sense of security through **unwarranted competence transfer**.
- **Architecture:** AgentReputation proposes a 3-layer decentralized architecture:
  1. *Functional Layer:* Task execution across heterogeneous agent environments.
  2. *Services Layer:* Reputation computation using "context-conditioned reputation cards."
  3. *Blockchain Layer:* Tamper-proof persistence of verified reputation cards.
- **Policy Engine:** Dynamically adjusts verification rigor and access permissions based on task risk.
- **Distinction from Our Project:** AgentReputation is the closest contemporary baseline. However, AgentReputation focuses on marketplace-wide reputation cards published to a shared registry. Our framework addresses the **adversarial client perspective**: given that 60%–90% of registry reviewers may be Sybils (Xiong et al.), client agents must prioritize **locally verified interaction evidence** over public reputation cards. Furthermore, our project conducts a controlled comparative benchmark isolating the exact performance difference between reputation-card lookup and evidence-grounded selection under attack.

---

## 4. Agent Provenance and Interaction Auditability

### 4.1 PROV-AGENT and W3C Provenance in Agentic Workflows
- **Key Paper:** Souza, R., Gueroudji, A., DeWitt, S., Rosendo, D., Ghosal, T., Ross, R., Balaprakash, P., & da Silva, R. F. (2025). *PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows.* In *2025 IEEE International Conference on eScience (eScience)*, pp. 467–473 (Peer-Reviewed Conference).
- **Core Contribution:** Extends the W3C PROV standard (Missier et al., 2013) to capture agent prompts, tool invocations, and multi-agent interaction lineages. Demonstrates near real-time provenance tracking across HPC, cloud, and edge infrastructures to analyze error propagation and workflow reliability.
- **Scope Boundary:** PROV-AGENT is an **observability and diagnostic framework**. It records execution lineage after the fact to facilitate debugging and accountability. It does not perform predictive trust scoring, compute risk-gated thresholds, or execute autonomous service selection during agent planning.
- **Our Integration:** We adopt PROV-AGENT's formal provenance data structures for our `EvidenceRecord`, ensuring that every service execution generates a cryptographically hashed, W3C-compatible provenance trail anchored to on-chain state roots.

---

## 5. Output Verification, Agent Reliability, and LLM Self-Correction Limits

### 5.1 The Impossibility of Unassisted LLM Self-Correction
- **Key Paper:** Huang, J., Chen, X., Mishra, S., Zheng, H. S., Yu, A. W., Song, X., & Zhou, D. (2024). *Large Language Models Cannot Self-Correct Reasoning Yet.* In *The Twelfth International Conference on Learning Representations (ICLR 2024)* (Peer-Reviewed Conference).
- **Empirical Proof:** Huang et al. evaluated multiple foundation models on common reasoning benchmarks and showed that without external ground-truth feedback, LLMs struggle to self-correct reasoning errors. In many scenarios, intrinsic prompting (asking an LLM to "review and correct your reasoning") causes performance to stagnate or even degrade.
- **Scientific Consequence for Agent Selection:** Proves that an autonomous client agent cannot reliably verify external service responses simply by prompting itself to evaluate whether the answer "looks correct." External, deterministic verification is mathematically and architecturally necessary.

### 5.2 External Tool-Interactive Verification: The CRITIC Framework
- **Key Paper:** Gou, Z., Shao, Z., Gong, Y., Shen, Y., Yang, Y., Duan, N., & Chen, W. (2024). *CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing.* In *The Twelfth International Conference on Learning Representations (ICLR 2024)* (Peer-Reviewed Conference).
- **Core Contribution:** Shows that when LLMs interact with external execution tools (code interpreters, test assertions, formal schema validators), verification and self-correction accuracy improve dramatically.
- **Role in Our Project:** Directly validates our **4-tier deterministic verification engine**: Tier 1 (Schema Validation), Tier 2 (Assertion & Code Test Execution), Tier 3 (Cross-Execution Multi-Agent Consensus), and Tier 4 (Execution Trace Audit).

---

## 6. Adversarial Agent Modeling, Sybil Attacks, and Reputation Manipulation

### 6.1 Foundational Attack Models
- **The Sybil Attack:** Douceur, J. R. (2002). *The Sybil Attack.* In *First International Workshop on Peer-to-Peer Systems (IPTPS '01)*, LNCS 2429, pp. 251–260 (Peer-Reviewed Conference).
  - Established that in decentralized networks without centralized gatekeepers or high computational cost barriers, a single adversary can fabricate an arbitrary number of identities to dominate consensus, voting, or reputation.
- **Reputation System Attack Taxonomy:** Hoffman, K., Zage, D., & Nita-Rotaru, C. (2009). *A survey of attack and defense techniques for reputation systems.* *ACM Computing Surveys*, 42(1), Article 1 (Peer-Reviewed Journal).
  - Formalized attack methodologies: self-promotion, ballot stuffing, bad-mouthing, whitewashing (discarding tarnished identities), and on-off oscillation (building high trust on trivial tasks, then exploiting it on high-value targets).
- **Economic Vulnerabilities:** Resnick, P., Zeckhauser, R., Friedman, E., & Kuwabara, K. (2000). *Reputation systems.* *Communications of the ACM*, 43(12), 45–48 (Peer-Reviewed Journal).
  - Analyzed cheap pseudonyms and the public-good dilemma of feedback provision, explaining why public reputation is consistently undersupplied and vulnerable to exit fraud.
- **Our Defense Architecture:** We explicitly model these adversarial behaviors in our 30-agent benchmark population (5 collusive Sybil boosters, 5 deceptive providers), proving that client-side verifiable evidence prevents on-off attacks and Sybil-inflated service exploitation.

---

## 7. Decentralized Agent Networks & Trustworthy RAG

### 7.1 Trust Taxonomy and Blockchain Boundaries
- **Key Paper:** Zhu, L., Li, Y., Wang, T., Chen, Z., Li, K., Liu, H., Wang, Y., Xu, L., Jiang, P., & Zhang, Z. (2026). *Blockchain Empowered Trustworthy Agent Networks: Foundations, Taxonomy, and Future Directions.* arXiv:2608.04626 (arXiv Preprint).
- **Contribution:** Formulates a 5-dimension taxonomy of trust in open agent networks. Critically emphasizes that blockchain provides shared state, identity binding, and non-repudiable audit logs, but cannot execute semantic verification of complex AI outputs.
- **Our Boundary:** Respects this exact division of labor: blockchain is utilized strictly for state commitment and provenance anchoring; semantic trust evaluation remains at the client agent layer.

### 7.2 Evidence Credibility in RAG Pipelines
- **Key Paper:** Liu, B., Che, H., & Li, Y. (2026). *TrustRAG: Blockchain-Enhanced RAG via Committee-Based Credibility Scoring.* arXiv:2608.20097 (arXiv Preprint).
- **Contribution:** Demonstrates that vector knowledge retrieval must be guarded with committee credibility scoring and cryptographic commitments to prevent retrieval poisoning.
- **Our Integration:** Informs our Vector Evidence Store (`EvidenceStore`), ensuring that historical interaction evidence indexed for semantic retrieval contains verified execution hashes.

---

## 8. Agent Tool Use and Standardized Interoperability

### 8.1 Tool-Augmented LLMs and Standard Protocols
- **Toolformer:** Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., Cancedda, N., & Scialom, T. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools.* *NeurIPS 2023*, 36, 68539–68551 (Peer-Reviewed Conference).
  - Pioneered self-supervised tool call learning for LLMs. However, Toolformer operates under the assumption that all tools are trusted, local, and permanent.
- **Model Context Protocol (MCP):** Anthropic (2024). *Model Context Protocol Specification* (Official Technical Specification).
  - Open JSON-RPC standard for discovering and executing external tools and data sources. MCP specifies the communication wire format, but includes zero trust scoring, provider security auditing, or output verification.
- **Our Middleware Positioning:** Our framework acts as an **evidence-based trust intelligence layer** wrapped around standard MCP endpoints, transforming passive tool invocation into secure, risk-gated service selection.

---

## 9. Autonomous Agent Economic Settlement (Future Work)

### 9.1 The x402 Payment Standard
- **Specification:** x402 Foundation and Coinbase Developer Platform (2025). *x402: An Open Standard for Machine-to-Machine and Agent-to-Agent Payments over HTTP 402* (Official Protocol Specification).
- **Content:** Reclaims HTTP status code 402 (*Payment Required*) to enable autonomous software agents to negotiate micro-settlements using cryptographic wallet headers.
- **Scope Boundary:** Scoped strictly as **future work** (Phase 4). In our current research testbed, service selection and verification are evaluated without financial settlement. In Phase 4, verified execution outcomes will trigger smart contract escrow payouts.

---

## 10. Thematic Literature Synthesis Table

| Research Theme | Seminal / Key Works | Publication Venues | How It Supports Our Research |
|:---|:---|:---|:---|
| **1. Autonomous Agents & Tool Use** | Schick et al. (2023), Anthropic MCP (2024) | NeurIPS 2023, Official Tech Spec | Defines agent tool discovery and execution protocols; motivates our trust middleware. |
| **2. Multi-Agent Trust & Reputation** | Sabater & Sierra (2002), Jøsang & Ismail (2002), Kamvar et al. (2003) | AAMAS 2002, Bled 2002, WWW 2003 | Mathematical foundation for Bayesian trust updating, recency decay, and certainty modeling. |
| **3. Task- / Context-Aware Trust** | Huynh et al. (2006), Chishti et al. (2026) | AAMAS 2006, ACM FSE 2026 | Solves competence-transfer failure; motivates context conditioning and semantic task matching. |
| **4. Identity & Registry Verification** | ERC-8004 Specification (2025), Xiong et al. (2026) | EIP Standard, arXiv:2606.26028 | Provides empirical proof that on-chain registries suffer from 85%+ endpoint downtime and Sybil rings. |
| **5. Agent Provenance & Auditability** | Souza et al. (2025), Missier et al. (2013) | IEEE eScience 2025, EDBT 2013 | Establishes W3C PROV structure for our interaction evidence records and execution traces. |
| **6. Output Verification & Reliability** | Huang et al. (2024), Gou et al. (2024) | ICLR 2024, ICLR 2024 | Proves LLMs cannot self-correct without external tools; justifies our 4-tier verification engine. |
| **7. Adversarial Agents & Sybil Attacks** | Douceur (2002), Hoffman et al. (2009), Resnick et al. (2000) | IPTPS 2001, ACM CSUR 2009, CACM 2000 | Guides our STRIDE threat model and the adversarial behaviors in our 30-agent benchmark testbed. |
| **8. Decentralized Agent Trust** | Zhu et al. (2026) | arXiv:2608.04626 | 5-dimension taxonomy bounds blockchain role to immutable audit trails and shared identity. |
| **9. Evidence Credibility & RAG** | Liu et al. (2026), Gao et al. (2023) | arXiv:2608.20097, arXiv:2312.10997 | Informs vector evidence store design; ensures retrieved historical evidence is authenticated. |
| **10. Agent Payments (Future Work)** | x402 Specification (2025) | Official Protocol Spec | Scoped strictly as future work connecting verification outcomes to automated payment escrow. |
