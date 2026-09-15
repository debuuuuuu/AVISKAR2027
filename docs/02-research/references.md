# Canonical Academic References & Verified Bibliography

This document contains the canonical, verified academic bibliography supporting the **Trust-Aware Service Selection for Autonomous AI Agents** research project. Every entry represents an independently verified source: peer-reviewed journal paper, peer-reviewed conference paper, verified preprint from identifiable researchers, or authoritative protocol specification.

**Academic Transparency Notice:**
Preprints (e.g., arXiv) are explicitly labeled as **arXiv Preprint (Not Peer-Reviewed)** to preserve strict academic integrity. Formal conference and journal publications are labeled with their specific peer-reviewed venue.

---

## Research Family 1: Agent Identity & Decentralized Registries

### [xiong2026trustless] Empirical Fragility of Decentralized Agent Registries
- **Full Title:** *Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem*
- **Authors:** Xihan Xiong, Zelin Li, Wei Wei, Qin Wang, William J. Knottenbelt, Zhipeng Wang
- **Year:** 2026
- **Publication Status:** arXiv Preprint (Not Peer-Reviewed)
- **Venue / Identifier:** [arXiv:2606.26028](https://arxiv.org/abs/2606.26028)
- **Official URL:** https://arxiv.org/abs/2606.26028
- **Core Empirical Finding:** First longitudinal measurement of ERC-8004 across Ethereum, BNB Smart Chain, and Base. Found that only 3.0% (Ethereum), 4.0% (BSC), and 15.0% (Base) of registered agents maintain active endpoints. Coordinated Sybil reviewers constitute 59.2% to 90.6% of all feedback transactions, causing reliable rating pools to collapse under basic Sybil filtering.
- **Scope & Role in Our Work:** Demonstrates that public on-chain identity and star ratings alone are insufficient for autonomous agent decision-making. Motivates our reliance on client-side verification and evidence grounding.

### [erc8004spec] ERC-8004 Standardized Agent Registries
- **Full Title:** *ERC-8004: Trustless AI Agent Standard — Identity, Reputation, and Validation Registries*
- **Authors:** Ethereum Improvement Proposals
- **Year:** 2025
- **Publication Status:** Official Technical Specification
- **Venue / Identifier:** Ethereum Improvement Proposal EIP-8004
- **Official URL:** https://eips.ethereum.org/EIPS/eip-8004
- **Core Contribution:** Specifies EVM standard contracts for Agent Identity (ERC-721 based discovery), Reputation (on-chain feedback scoring), and Validation (third-party cryptographic attestations).
- **Scope & Role in Our Work:** Represents the state of the art in open, permissionless agent discovery. Our framework acts as an evidence-aware client layer above ERC-8004 registries.

---

## Research Family 2: Agent Provenance & Auditability

### [souza2025provagent] Unified Agent Interaction Provenance
- **Full Title:** *PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows*
- **Authors:** Renan Souza, Amal Gueroudji, Stephen DeWitt, Daniel Rosendo, Tirthankar Ghosal, Robert Ross, Prasanna Balaprakash, Rafael Ferreira da Silva
- **Year:** 2025
- **Publication Status:** Peer-Reviewed Conference Paper
- **Venue / Identifier:** *2025 IEEE International Conference on eScience (eScience)*, pp. 467–473, [DOI: 10.1109/eScience65000.2025.00093](https://doi.org/10.1109/eScience65000.2025.00093)
- **Official URL:** https://ieeexplore.ieee.org/document/11181558/
- **Core Empirical Finding:** Extends W3C PROV to track agentic workflow executions (prompts, tool calls, responses) with near real-time provenance capture across HPC, cloud, and edge. Demonstrates error propagation tracking and provenance query response times.
- **Scope & Role in Our Work:** Provides the architectural foundation for structuring interaction history into formal, verifiable provenance graphs (`EvidenceRecord`).

---

## Research Family 3: Context-Conditioned Agent Reputation

### [chishti2026agentreputation] Decentralized Context-Conditioned Agent Reputation
- **Full Title:** *AgentReputation: A Decentralized Agentic AI Reputation Framework*
- **Authors:** Mohd Sameen Chishti, Damilare Peter Oyinloye, Jingyue Li
- **Year:** 2026
- **Publication Status:** Peer-Reviewed Conference Paper / Preprint
- **Venue / Identifier:** *Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering (FSE 2026)* / [arXiv:2605.00073](https://arxiv.org/abs/2605.00073)
- **Official URL:** https://arxiv.org/abs/2605.00073
- **Core Finding:** Solves the competence-transfer problem across heterogeneous agent tasks by establishing "context-conditioned reputation cards" with explicit verification regimes and risk-based escalation policies.
- **Scope & Role in Our Work:** Demonstrates why global scalar scores fail. Closest related work; our project specifically isolates and measures whether local verified evidence provides decision superiority over reputation-card lookup alone under adversarial conditions.

---

## Research Family 4: Decentralized Trust & Agent Networks

### [zhu2026trustworthy] Blockchain-Empowered Trustworthy Agent Networks
- **Full Title:** *Blockchain Empowered Trustworthy Agent Networks: Foundations, Taxonomy, and Future Directions*
- **Authors:** Liehuang Zhu, Yuhang Li, Tianxing Wang, Zhihao Chen, Ke Li, Hongyi Liu, Yajie Wang, Lei Xu, Peng Jiang, Zijian Zhang
- **Year:** 2026
- **Publication Status:** arXiv Preprint (Not Peer-Reviewed)
- **Venue / Identifier:** [arXiv:2608.04626](https://arxiv.org/abs/2608.04626)
- **Official URL:** https://arxiv.org/abs/2608.04626
- **Core Contribution:** Establishes a 5-dimension taxonomy for trust in open agent networks: Entity/Capability Trust, Authorization/Delegation Trust, Information/Provenance Trust, Coordination/Group Trust, and Accountability/Settlement Trust. Clarifies that blockchain enforces auditability, state synchronization, and identity persistence, but cannot perform semantic evaluation.
- **Scope & Role in Our Work:** Informs our architectural boundary: on-chain storage is reserved for immutable hash roots, while semantic verification and trust calculation remain off-chain at the client layer.

---

## Research Family 5: Evidence Credibility & Verifiable Retrieval

### [liu2026trustrag] Credibility Scoring via Committee Consensus
- **Full Title:** *TrustRAG: Blockchain-Enhanced RAG via Committee-Based Credibility Scoring*
- **Authors:** Baixiang Liu, Haotian Che, Yuan Li
- **Year:** 2026
- **Publication Status:** arXiv Preprint (Not Peer-Reviewed)
- **Venue / Identifier:** [arXiv:2608.20097](https://arxiv.org/abs/2608.20097)
- **Official URL:** https://arxiv.org/abs/2608.20097
- **Core Contribution:** Uses domain-expert committee consensus, zero-knowledge proofs, and blockchain commitments to assign verifiable credibility scores to retrieved documents in RAG pipelines.
- **Scope & Role in Our Work:** Informs our evidence store design: retrieved interaction records must have cryptographic authenticity proofs rather than unvalidated text blobs.

---

## Research Family 6: Classical Multi-Agent Trust & Reputation

### [sabater2002regret] The REGRET Model
- **Full Title:** *REGRET: A reputation model for multi-agent systems*
- **Authors:** Jordi Sabater, Carles Sierra
- **Year:** 2002
- **Publication Status:** Peer-Reviewed Journal Paper
- **Venue / Identifier:** *Autonomous Agents and Multi-Agent Systems*, 5(1), pp. 33–55, [DOI: 10.1023/A:1013734109878](https://doi.org/10.1023/A:1013734109878)
- **Official URL:** https://link.springer.com/article/10.1023/A:1013734109878
- **Core Finding:** Deconstructs trust into direct experience, witness reports, and system role reputation, using temporal decay functions to model behavioral drift.
- **Scope & Role in Our Work:** Foundational theoretical basis for our tripartite scoring model ($w_v \cdot V + w_e \cdot E + w_r \cdot R$) and time-decay weighting ($e^{-\lambda \Delta t}$).

### [josang2002beta] The Beta Reputation System
- **Full Title:** *The Beta Reputation System*
- **Authors:** Audun Jøsang, Roslan Ismail
- **Year:** 2002
- **Publication Status:** Peer-Reviewed Conference Paper
- **Venue / Identifier:** *Proceedings of the 15th Bled Electronic Commerce Conference*, pp. 2502–2511
- **Official URL:** https://folk.uio.no/josang/papers/JI2002-Bled.pdf
- **Core Finding:** Uses Beta probability distributions $(\alpha, \beta)$ to represent statistical expectations of agent reliability while formally expressing epistemic uncertainty.
- **Scope & Role in Our Work:** Mathematical basis for our confidence discounting in cold-start scenarios and low-sample evaluations.

### [kamvar2003eigentrust] Distributed Reputation via EigenTrust
- **Full Title:** *The EigenTrust algorithm for reputation management in P2P networks*
- **Authors:** Sepandar D. Kamvar, Mario T. Schlosser, Hector Garcia-Molina
- **Year:** 2003
- **Publication Status:** Peer-Reviewed Conference Paper
- **Venue / Identifier:** *Proceedings of the 12th International Conference on World Wide Web (WWW '03)*, pp. 640–651, [DOI: 10.1145/775152.775242](https://doi.org/10.1145/775152.775242)
- **Official URL:** https://dl.acm.org/doi/10.1145/775152.775242
- **Core Finding:** Computes global trust vector through principal eigenvector iteration over normalized peer feedback matrices; demonstrates resilience to non-colluding rogue peers.
- **Scope & Role in Our Work:** Represents the classic global consensus reputation baseline in distributed systems.

### [huynh2006fire] Multi-Dimensional Evidence Integration (FIRE)
- **Full Title:** *An integrated trust and reputation model for open multi-agent systems*
- **Authors:** Trung Dong Huynh, Nicholas R. Jennings, Nigel R. Shadbolt
- **Year:** 2006
- **Publication Status:** Peer-Reviewed Journal Paper
- **Venue / Identifier:** *Autonomous Agents and Multi-Agent Systems*, 13(2), pp. 119–154, [DOI: 10.1007/s10458-005-6825-4](https://doi.org/10.1007/s10458-005-6825-4)
- **Official URL:** https://link.springer.com/article/10.1007/s10458-005-6825-4
- **Core Finding:** Combines interaction trust, role-based trust, witness reputation, and certified reputation; empirically proves multi-source evidence outperforms any single information channel.
- **Scope & Role in Our Work:** Directly justifies combining direct execution verification records with historical interaction evidence and registry signals.

### [teacy2006travos] Probabilistic Trust under Witness Inaccuracy (TRAVOS)
- **Full Title:** *TRAVOS: An probabilistic trust and reputation model for open multi-agent systems*
- **Authors:** W. T. Luke Teacy, Jigar Patel, Nicholas R. Jennings, Michael Luck
- **Year:** 2006
- **Publication Status:** Peer-Reviewed Journal Paper
- **Venue / Identifier:** *Autonomous Agents and Multi-Agent Systems*, 12(2), pp. 183–210, [DOI: 10.1007/s10458-006-5952-y](https://doi.org/10.1007/s10458-006-5952-y)
- **Official URL:** https://link.springer.com/article/10.1007/s10458-006-5952-y
- **Core Finding:** Beta-distribution framework that estimates the probability that third-party witnesses are untruthful, dynamically discounting unverified opinions.
- **Scope & Role in Our Work:** Justifies down-weighting external reputation ($w_r$) in favor of directly verified evidence ($w_v$) when risk is high.

### [yu2013survey] Multi-Agent Trust Management Survey
- **Full Title:** *A survey of multi-agent trust management systems*
- **Authors:** Han Yu, Zhiqi Shen, Chunyan Miao, Cyril Leung, Dusit Niyato
- **Year:** 2013
- **Publication Status:** Peer-Reviewed Journal Paper
- **Venue / Identifier:** *IEEE Access*, 1, pp. 35–50, [DOI: 10.1109/ACCESS.2013.2259837](https://doi.org/10.1109/ACCESS.2013.2259837)
- **Official URL:** https://ieeexplore.ieee.org/document/6517112
- **Core Finding:** Taxonomic review of computational trust across multi-agent environments; concludes context-blind trust models consistently fail when task complexity and risk vary.
- **Scope & Role in Our Work:** Comprehensive survey establishing that context-awareness is mandatory in dynamic multi-agent trust systems.

---

## Research Family 7: Adversarial Multi-Agent Systems & Sybil Attacks

### [douceur2002sybil] The Sybil Attack
- **Full Title:** *The Sybil Attack*
- **Authors:** John R. Douceur
- **Year:** 2002
- **Publication Status:** Peer-Reviewed Conference Paper
- **Venue / Identifier:** *International Workshop on Peer-to-Peer Systems (IPTPS '01)*, LNCS 2429, pp. 251–260, [DOI: 10.1007/3-540-45748-8_24](https://doi.org/10.1007/3-540-45748-8_24)
- **Official URL:** https://link.springer.com/chapter/10.1007/3-540-45748-8_24
- **Core Finding:** Proves that without centralized identity verification or severe resource costs, distributed peer-to-peer networks cannot prevent an adversary from forging arbitrarily many identities.
- **Scope & Role in Our Work:** Informs threat vector T-01 (Sybil identity flooding) and explains why on-chain registry counts cannot be equated with trustworthiness.

### [hoffman2009survey] Attack and Defense in Reputation Systems
- **Full Title:** *A survey of attack and defense techniques for reputation systems*
- **Authors:** Kevin Hoffman, David Zage, Cristina Nita-Rotaru
- **Year:** 2009
- **Publication Status:** Peer-Reviewed Journal Paper
- **Venue / Identifier:** *ACM Computing Surveys (CSUR)*, 42(1), Article 1, pp. 1–31, [DOI: 10.1145/1592451.1592452](https://doi.org/10.1145/1592451.1592452)
- **Official URL:** https://dl.acm.org/doi/10.1145/1592451.1592452
- **Core Finding:** Systematically categorizes attacks on reputation engines (self-promotion, slandering, ballot stuffing, whitewashing, on-off oscillations).
- **Scope & Role in Our Work:** Guides our threat model and the adversarial behaviors implemented in our simulation benchmark (e.g., collusive rating boosters and deceptive providers).

### [resnick2000reputation] Structural Economics of Reputation
- **Full Title:** *Reputation systems*
- **Authors:** Paul Resnick, Richard Zeckhauser, Eric Friedman, Karen Kuwabara
- **Year:** 2000
- **Publication Status:** Peer-Reviewed Journal Paper
- **Venue / Identifier:** *Communications of the ACM*, 43(12), pp. 45–48, [DOI: 10.1145/355112.355122](https://doi.org/10.1145/355112.355122)
- **Official URL:** https://dl.acm.org/doi/10.1145/355112.355122
- **Core Finding:** Details the fundamental economic challenges of reputation systems: cheap pseudonym creation, under-provision of honest feedback, and vulnerability to strategic exit.
- **Scope & Role in Our Work:** Motivates our architectural requirement for local client evidence persistence rather than relying exclusively on altruistic public feedback.

---

## Research Family 8: Agent Verification & Output Reliability Limits

### [huang2024selfcorrect] Limits of LLM Intrinsic Self-Correction
- **Full Title:** *Large Language Models Cannot Self-Correct Reasoning Yet*
- **Authors:** Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou
- **Year:** 2024
- **Publication Status:** Peer-Reviewed Conference Paper
- **Venue / Identifier:** *The Twelfth International Conference on Learning Representations (ICLR 2024)* / [arXiv:2310.01798](https://arxiv.org/abs/2310.01798)
- **Official URL:** https://arxiv.org/abs/2310.01798
- **Core Empirical Finding:** Rigorously proves that LLMs cannot reliably self-correct reasoning errors without external ground truth or feedback. In many cases, unassisted self-critique leads to performance degradation.
- **Scope & Role in Our Work:** Proves that an agent cannot verify external service outputs through pure internal LLM self-reflection; external deterministic verification protocols are fundamentally required.

### [gou2024critic] External Tool-Interactive Verification (CRITIC)
- **Full Title:** *CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing*
- **Authors:** Zhibin Gou, Zhihong Shao, Yeyun Gong, Yelong Shen, Yujiu Yang, Nan Duan, Weizhu Chen
- **Year:** 2024
- **Publication Status:** Peer-Reviewed Conference Paper
- **Venue / Identifier:** *The Twelfth International Conference on Learning Representations (ICLR 2024)* / [arXiv:2305.11738](https://arxiv.org/abs/2305.11738)
- **Official URL:** https://arxiv.org/abs/2305.11738
- **Core Empirical Finding:** Shows that LLM outputs can be reliably verified and corrected when augmented with external computational tools (code execution, schema validators, search engines).
- **Scope & Role in Our Work:** Directly supports our 4-tier verification engine (schema validation, formal assertion execution, cross-execution consensus, execution trace analysis).

---

## Research Family 9: Agent Tool Use & Standardized Protocols

### [schick2023toolformer] LLM Tool Invocation (Toolformer)
- **Full Title:** *Toolformer: Language Models Can Teach Themselves to Use Tools*
- **Authors:** Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom
- **Year:** 2023
- **Publication Status:** Peer-Reviewed Conference Paper
- **Venue / Identifier:** *Advances in Neural Information Processing Systems (NeurIPS 2023)*, 36, pp. 68539–68551
- **Official URL:** https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e40e79ad3ab5250403f2bfa99-Abstract-Conference.html
- **Core Finding:** Demonstrates that LLMs can self-teach API tool calling through self-supervised data generation, improving arithmetic, date parsing, and search performance.
- **Scope & Role in Our Work:** Establishes the foundational model of agent tool invocation. Toolformer solves *how to invoke tools*, but assumes tools are benign and permanent; our work addresses *which tool to select when tools are untrusted*.

### [mcp2024specification] Model Context Protocol Specification
- **Full Title:** *Model Context Protocol (MCP) Specification*
- **Authors:** Anthropic
- **Year:** 2024
- **Publication Status:** Official Technical Specification
- **Venue / Identifier:** Technical Specification
- **Official URL:** https://modelcontextprotocol.io
- **Core Contribution:** Standardizes client-host-server communication for tool discovery, resource provision, and execution over JSON-RPC.
- **Scope & Role in Our Work:** Adopted as the interoperability communication standard between agents and candidate services; our trust-aware framework operates as an intelligent middleware layer above MCP.

---

## Research Family 10: Autonomous Agent Payments & Economic Settlement (Future Work)

### [x402spec] Open Payment Standard for Autonomous Agents
- **Full Title:** *x402: An Open Standard for Machine-to-Machine and Agent-to-Agent Payments over HTTP 402*
- **Authors:** x402 Foundation and Coinbase Developer Platform
- **Year:** 2025
- **Publication Status:** Official Protocol Specification
- **Venue / Identifier:** Protocol Specification
- **Official URL:** https://x402.org
- **Core Contribution:** Standardizes cryptographic payment negotiation and on-chain settlement for autonomous HTTP requests using HTTP status code 402.
- **Scope & Role in Our Work:** Scoped strictly as future work (Phase 4), defining how verified interaction outcomes can trigger automated smart contract escrow releases.
