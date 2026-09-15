# Research Limitations & Explicit Assumptions

A hallmark of rigorous academic research is transparently documenting the boundaries, assumptions, and limitations of the proposed approach. This document outlines the explicit constraints governing the current stage of this project.

---

## 1. Simulation Testbed Limitations

### 1.1 Population Size ($N = 30$)
- **Constraint:** The controlled simulation environment is configured with 30 simulated service agents (20 Reliable, 5 Unreliable, 5 Malicious).
- **Limitation:** While 30 agents provide sufficient heterogeneity to benchmark comparative selection dynamics, real-world decentralized ecosystems contain thousands of registered agents with long-tail distributions.
- **Future Direction:** Scaling tests to $N = 100$ and $N = 1000$ to observe asymptotic retrieval and decision latency.

### 1.2 Synthetic Behavioral Models
- **Constraint:** Simulated agents execute parameterized behavioral profiles (e.g., probability of timeout, deterministic error injection, Sybil feedback loops).
- **Limitation:** Synthetic agent behavior approximates, but cannot fully replicate, the full complexity of human-engineered adversarial attacks, zero-day prompt injection exploits, or complex multi-step Byzantine collusion.

---

## 2. Theoretical & Methodological Limitations

### 2.1 The Verifier Trust Boundary ("Who Verifies the Verifier?")
- **Limitation:** The entire evidence feedback loop relies on the premise that the Result Verification Layer correctly evaluates task outputs.
- **Vulnerability:** If the verification logic contains bugs, incorrect test cases, or is compromised by an adversary, the evidence store will ingest false positive or false negative records, poisoning future trust evaluations.
- **Current Mitigation:** The framework restricts high-confidence verification to deterministic domains (e.g., unit test execution, schema validation, mathematical proofs) and treats heuristic LLM-as-a-judge verification with lower epistemic weight.

### 2.2 The Cold-Start Challenge
- **Limitation:** When a newly registered service joins the network, or when an established service is evaluated on an entirely novel task domain with zero historical records, $\sum w_k \approx 0$.
- **Implication:** The framework must either:
  1. Default to conservative rejection on high-stakes tasks, creating market entry barriers for new providers.
  2. Fall back to capability introspection and discounted reputation, temporarily exposing the client agent to increased risk.
- **Mitigation:** Introducing progressive risk-tiered sandboxing: new services are only permitted to execute low-stakes, non-critical tasks until empirical evidence accumulates.

### 2.3 Verification Latency and Cost Overhead
- **Limitation:** Querying vector stores (RAG), computing multi-dimensional trust scores, and executing post-task verification checks incurs measurable wall-clock latency and computational overhead.
- **Trade-off:** For micro-latency or zero-stakes tasks (e.g., retrieving public stock quotes), the cost of verification may exceed the cost of the task itself.

### 2.4 Domain Scope of Verification
- **Limitation:** Some tasks are inherently non-deterministic or subjective (e.g., open-ended creative copywriting, philosophical summarization). Deterministic verification cannot evaluate subjective quality with certainty.
- **Scope:** Our framework is primarily optimized for verifiable tasks (computational, code generation, API querying, schema transformation, mathematical reasoning).

---

## 3. Explicit Assumptions Matrix

| Assumption ID | Description | Impact if Violated |
|---|---|---|
| **A1: Local Storage Integrity** | The client agent's local runtime environment and SQLite/DuckDB evidence store are not compromised. | Complete failure of trust evaluation integrity if an adversary gains root execution on the client host. |
| **A2: Stable Semantic Embeddings** | The embedding model used for task domain vectorization produces consistent semantic similarity scores across task variants. | Mismatched evidence retrieval if embeddings drift or fail to capture domain nuances. |
| **A3: Identifiable Identity Anchor** | Candidate services possess a stable cryptographic public key or identifier across interaction sessions. | Inability to track historical performance if agents continuously whitewash identities at zero economic cost. |
