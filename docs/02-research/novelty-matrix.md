# Novelty Matrix: Systematic Comparison with Prior Systems and Frameworks

This document presents a multi-dimensional feature comparison between the proposed **Trust-Aware Service Selection Framework** and foundational, contemporary systems across academic literature and industry specifications.

To preserve academic integrity, prior systems are marked **honestly** based on their published capabilities. A checkmark (`✓`) indicates the system provides native, documented support for that capability. A partial checkmark (`◐`) indicates partial, indirect, or constrained support. An empty mark (`✗`) indicates the capability is outside the system's defined design scope or not supported.

Prior systems are grouped by their **Research Family** to emphasize their intended problem domains.

---

## 1. Feature Comparison Matrix

| Research Family | System / Framework | Agent Identity | Capability Info | General Reputation | Task-Specific Reputation | Interaction Evidence | Evidence Verification | Continuous Evidence Update | Risk Assessment | Service Selection | Controlled Experiment | Provenance Lineage | Decentralization |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Classical Trust** | **REGRET** *(Sabater & Sierra 2002)* | ◐ | ✗ | ✓ | ◐ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ |
| **Classical Trust** | **Beta Reputation** *(Jøsang & Ismail 2002)* | ◐ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | ◐ | ✓ | ✗ | ✗ |
| **Classical Trust** | **EigenTrust** *(Kamvar et al. 2003)* | ◐ | ✗ | ✓ | ✗ | ◐ | ✗ | ✓ | ✗ | ◐ | ✓ | ✗ | ✓ |
| **Classical Trust** | **FIRE** *(Huynh et al. 2006)* | ◐ | ◐ | ✓ | ◐ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ |
| **Classical Trust** | **TRAVOS** *(Teacy et al. 2006)* | ◐ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ |
| **Agent Tool Use** | **Toolformer** *(Schick et al. 2023)* | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ◐ | ✓ | ✗ | ✗ |
| **Agent Tool Use** | **Anthropic MCP** *(2024)* | ◐ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ◐ | ✗ |
| **Verification** | **CRITIC** *(Gou et al. 2024)* | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ |
| **Provenance** | **PROV-AGENT** *(Souza et al. 2025)* | ✓ | ◐ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ | ✓ | ✓ | ✗ |
| **Identity / Registry**| **ERC-8004** *(Ethereum standard 2025)* | ✓ | ✓ | ✓ | ◐ | ✗ | ◐ | ◐ | ✗ | ✗ | ✗ | ◐ | ✓ |
| **Decentralized Trust**| **Zhu et al. Taxonomy** *(2026)* | ✓ | ✓ | ✓ | ◐ | ◐ | ◐ | ◐ | ◐ | ✗ | ✗ | ✓ | ✓ |
| **Context Reputation** | **AgentReputation** *(Chishti et al. 2026)* | ✓ | ✓ | ✓ | ✓ | ◐ | ✓ | ✓ | ✓ | ◐ | ◐ | ◐ | ✓ |
| **Verifiable RAG** | **TrustRAG** *(Liu et al. 2026)* | ◐ | ✗ | ◐ | ✗ | ✓ | ✓ | ◐ | ◐ | ✗ | ✓ | ✓ | ✓ |
| **Proposed Framework**| **Our Trust-Aware Framework** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** | **✓** |

---

## 2. Dimension Definitions and Scoring Criteria

1. **Agent Identity:** Does the system assign unique, cryptographically verifiable, or standardized identifiers to agents?
   - `✓`: Cryptographic DIDs, EVM public keys, or standard persistent IDs.
   - `◐`: Ephemeral session IDs or unauthenticated string names.
   - `✗`: No agent identity tracking.

2. **Capability Information:** Can the system represent, discover, or index machine-readable agent capabilities?
   - `✓`: Structured capability manifests (JSON schema, input/output typing, semantic tags).
   - `◐`: Free-form text descriptions or static role tags.
   - `✗`: No capability representation.

3. **General Reputation:** Does the system compute or aggregate global peer reputation?
   - `✓`: Formal scalar or vector aggregation of historical feedback across participants.
   - `◐`: Ad-hoc scoring or unweighted average rating.
   - `✗`: No reputation aggregation.

4. **Task-Specific Reputation:** Does the system differentiate performance across distinct task domains?
   - `✓`: Explicit domain-conditioned reputation models (e.g., separate scores for math, code, retrieval).
   - `◐`: Role-based or context-tagged ratings with coarse granularity.
   - `✗`: Global scalar score applied uniformly to all task types.

5. **Interaction Evidence:** Does the system maintain detailed, queryable records of historical executions?
   - `✓`: Granular records capturing input prompt, output payload, latency, timestamp, and task context.
   - `◐`: Binary success/failure counters or aggregate metrics only.
   - `✗`: No execution evidence stored.

6. **Evidence Verification:** Does the system verify the empirical correctness of execution outputs?
   - `✓`: Deterministic programmatic validation (schema validation, unit assertions, multi-agent consensus).
   - `◐`: Subjective user feedback, witness votes, or third-party attestations without execution replay.
   - `✗`: Assumes outputs are valid without testing.

7. **Continuous Evidence Update:** Does the system automatically update its trust knowledge after each interaction?
   - `✓`: Closed-loop dynamic ingestion of post-execution verification results into the trust store.
   - `◐`: Periodic batch updates or manual recalculations.
   - `✗`: Static or one-time configuration.

8. **Risk Assessment:** Does the system evaluate the risk profile of the incoming task before making decisions?
   - `✓`: Mathematical risk-gating based on task criticality, cost, failure impact, and uncertainty.
   - `◐`: Static thresholding or rule-based escalation.
   - `✗`: Risk-agnostic service selection.

9. **Service Selection:** Does the system implement an autonomous decision engine to pick the optimal candidate?
   - `✓`: Formal multi-criteria selection algorithm balancing trust, risk, cost, and historical evidence.
   - `◐`: Heuristic ranking (e.g., argmax reputation) without risk constraints.
   - `✗`: Pure manual, random, or static round-robin selection.

10. **Controlled Experiment:** Has the framework been validated in controlled experiments against alternative baselines?
    - `✓`: Controlled empirical evaluation with reproducible benchmark metrics and defined baselines.
    - `◐`: Case study, qualitative demo, or preliminary simulation without full baseline suite.
    - `✗`: Conceptual proposal without empirical validation.

11. **Provenance Lineage:** Are interaction histories and evidence traceable via standardized provenance models?
    - `✓`: W3C PROV-compliant lineage graphs or cryptographic hash chains.
    - `◐`: Timestamped audit logs without formal relational graph structures.
    - `✗`: Ephemeral execution traces discarded after runtime.

12. **Decentralization:** Can the architecture operate without a single centralized gatekeeper?
    - `✓`: Decentralized ledger anchoring, peer-to-peer verification, or local client autonomy.
    - `◐`: Hybrid architecture with centralized coordinator but distributed components.
    - `✗`: Requires a single centralized trusted server or marketplace operator.

---

## 3. Honest Architectural Positioning

### 3.1 What AgentReputation Does Well vs. Our Addition
- **AgentReputation's Strength:** Beautifully formalizes context-conditioned reputation cards and 3-layer architecture for decentralized marketplaces.
- **Our Addition:** AgentReputation assumes client agents consume market-wide reputation cards. Our framework addresses the **adversarial client perspective**: when 60%–90% of market feedback is generated by Sybils (as proven by Xiong et al.), an agent must rely on its own **locally verified interaction evidence** and deterministic verifiers, treating public cards merely as a discounted prior.

### 3.2 What PROV-AGENT Does Well vs. Our Addition
- **PROV-AGENT's Strength:** Excellent W3C PROV-compliant telemetry capture for multi-agent LLM systems across complex infrastructure.
- **Our Addition:** PROV-AGENT is an **observability framework** (retrospective). We leverage its provenance structure to build a **predictive decision engine** that uses past provenance records to guide future service selection.

### 3.3 What Toolformer / MCP Do Well vs. Our Addition
- **Toolformer / MCP Strength:** Perfect standard for invoking tools and declaring JSON schemas.
- **Our Addition:** Toolformer and MCP assume tools are benign and reliable. We supply the **trust and risk intelligence middleware** that intercepts tool discovery, filters unreliable or malicious endpoints, and verifies outputs before ingestion.
