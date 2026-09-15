# Terminology & Conceptual Taxonomy

To prevent semantic confusion and ensure rigorous communication across research papers, documentation, and presentations, this document establishes the formal definitions used throughout the project.

---

## 1. Core Distinctions: Trust vs. Reputation vs. Evidence

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  EVIDENCE                                                                   │
│  Empirical, verifiable records of past task executions, including input      │
│  schemas, returned outputs, execution latency, and verification outcomes.    │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │ Aggregated by third parties
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  REPUTATION                                                                 │
│  A global, aggregate social or network-level summary of historical peer      │
│  ratings. Decoupled from task context; susceptible to Sybil collusion.      │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │ Input to client decision engine
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  TRUST (The Trust Decision)                                                 │
│  A client-specific, context-dependent evaluation of subjective confidence    │
│  that a candidate service will perform a specific task successfully under    │
│  explicit risk constraints.                                                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Definitive Glossary

### 2.1 Agent & Service Definitions
- **Autonomous Client Agent:** An autonomous software entity that initiates, coordinates, and delegates subtasks to external services to achieve an objective without continuous human oversight.
- **Service Agent / Provider:** An external, autonomous computational entity or tool offering specialized task execution endpoints (via API, MCP, or smart contract).
- **Candidate Pool:** The subset of registered service agents whose advertised capabilities match the schema requirements of the current task.

### 2.2 Trust & Reputation Terminology
- **Trust (Decision-Oriented):** The assessed probability and confidence that a candidate service will satisfy the functional and security requirements of a specific task without causing harm. Trust is **subjective to the client agent**, **context-dependent**, and **risk-calibrated**.
- **Reputation (Aggregate Social Signal):** An aggregated metric representing what the wider network or third-party reviewers report about a service. Reputation is **global, non-contextual, and vulnerable to Sybil manipulation**.
- **Task-Specific Trust:** Trust evaluated exclusively over the historical subset of interactions that share high semantic and structural similarity with the current task.

### 2.3 Evidence & Verification Terminology
- **Interaction:** A single discrete transaction wherein a client agent delegates a task payload to a service provider and receives an output payload.
- **Evidence Record:** A structured, immutable data object encapsulating an interaction: task specification, returned result, observed execution metrics, verification verdict, timestamp, and cryptographic signatures.
- **Evidence Quality:** A composite measure of an evidence record's epistemic reliability, determined by sample size, recency (time-decay), verification rigor (deterministic vs. heuristic), and provenance authenticity.
- **Result Verification:** The process of evaluating whether a completed service output satisfies correctness, safety, and schema specifications.
- **Deterministic Verification:** Verification using exact mathematical or algorithmic criteria (e.g., unit test execution, JSON schema validation, cryptographic signature checking).
- **Consensus Verification:** Verification achieved by querying multiple heterogeneous services and comparing results via majority voting or threshold agreement.

### 2.4 Security & Adversarial Terminology
- **Sybil Attack:** An adversarial attack wherein a single entity creates multiple pseudo-identities to manipulate voting, consensus, or reputation scores.
- **Coordinated Feedback Collusion:** A network of Sybil or colluding agents exchanging artificial positive ratings to inflate global reputation scores.
- **Halo Effect / Domain Mismatch:** The false assumption that high performance in one task category (e.g., text translation) implies high performance in an unrelated category (e.g., Python code generation).
- **Exit Scam / Behavioral Drift:** An adversarial strategy where a service exhibits reliable behavior on low-stakes tasks to accumulate trust, followed by intentional failure, data theft, or prompt injection on high-stakes tasks.

### 2.5 Architecture & Protocol Terminology
- **Model Context Protocol (MCP):** An open, vendor-neutral protocol developed by Anthropic enabling AI models to interact with local and remote tools, resources, and execution sandboxes.
- **Retrieval-Augmented Generation (RAG):** The technique of embedding and indexing historical evidence records in a vector space to retrieve the most semantically relevant interaction traces at decision time.
- **Cryptographic State Commitment:** A cryptographic hash (e.g., SHA-256 Merkle root) anchored to an immutable ledger that proves an evidence log existed at a specific time and has not been altered post-hoc.
- **x402 (HTTP 402 Extension):** An autonomous payment standard leveraging the HTTP 402 Payment Required status code to support programmatic micropayments for web and agent services.
