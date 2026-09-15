# Detailed Component Design & Specifications

This document specifies the internal architecture, interfaces, data contracts, and failure handling for each of the 10 components in the **Trust-Aware Service Selection Framework**.

---

## Component 1: Autonomous Client Agent (`src/agent/client_agent.py`)

- **Responsibility:** Master orchestrator governing task decomposition, service delegation, and result synthesis.
- **Inputs:** `TaskGoal` (User goal, constraints, deadline).
- **Outputs:** `VerifiedTaskResult` or `ExecutionAbortedException`.
- **Key Methods:**
  - `run_task(task_spec: TaskSpecification) -> TaskResult`
  - `handle_selection_failure(reason: str) -> FallbackAction`
- **Trust Boundary:** **TRUSTED CORE.** Runs in the client's private execution environment.

---

## Component 2: Service Discovery Layer (`src/discovery/`)

- **Responsibility:** Queries public directories, local caches, and on-chain registries (e.g., ERC-8004) to locate candidates advertising the required capabilities.
- **Inputs:** `CapabilityQuery(domain: str, method: str, schema_version: str)`.
- **Outputs:** `List[CandidateServiceMetadata]`.
- **Key Methods:**
  - `discover_candidates(query: CapabilityQuery) -> List[ServiceMetadata]`
  - `probe_reachability(service_endpoint: str) -> bool`
- **Failure Handling:** Filters out non-responsive endpoints immediately (mitigating the 85-97% "ghost agent" phenomenon).
- **Trust Boundary:** **UNTRUSTED.** Metadata received must be validated by the Candidate Store.

---

## Component 3: Service Candidate Store (`src/candidates/`)

- **Responsibility:** Maintains an active in-memory session pool of reachable candidates, caching their public keys, advertised capability cards, and endpoint URIs.
- **Data Structure:** `Dict[ServiceID, ServiceMetadata]` indexed by capability tags.
- **Trust Boundary:** **SEMI-TRUSTED.** Holds unverified candidate claims until evaluated.

---

## Component 4: Evidence Store & Vector Index (`src/evidence/store.py`, `src/rag/retriever.py`)

- **Responsibility:** Persists raw interaction traces, structured verification records, and indexes task representations in vector space for fast semantic retrieval.
- **Storage Subsystems:**
  - *Document Store:* Local relational/embedded database (SQLite / DuckDB) storing full JSON evidence records.
  - *Vector Index:* In-memory or embedded vector index (Chroma / FAISS / NumPy) mapping task domain embeddings to evidence IDs.
- **Key Methods:**
  - `query_task_evidence(service_id: str, task_embedding: List[float], top_k: int = 10) -> List[EvidenceRecord]`
  - `insert_evidence(record: EvidenceRecord) -> None`
- **Trust Boundary:** **TRUSTED STORAGE.** Must be protected by OS file permissions and validated against state commitment roots.

---

## Component 5: Trust Evaluation Engine (`src/trust/evaluator.py`)

- **Responsibility:** Computes multidimensional trust assessments for candidate services on a specific task.
- **Inputs:**
  - `candidate: ServiceMetadata`
  - `task: TaskSpecification`
  - `evidence_records: List[EvidenceRecord]`
  - `risk_assessment: RiskAssessment`
- **Outputs:** `TrustAssessment(confidence: float, expected_success: float, recommendation: DecisionEnum)`.
- **Evaluation Factors:**
  1. Identity validity (valid cryptographic signature or registration).
  2. Capability schema compatibility.
  3. Task-specific historical success rate (weighted by semantic cosine similarity and recency decay).
  4. Evidence quality & sample size confidence.
  5. Discounted global reputation.
- **Trust Boundary:** **TRUSTED CORE.** Algorithmic decision logic executed locally.

---

## Component 6: Risk Assessment Layer (`src/trust/risk.py`)

- **Responsibility:** Evaluates task stakes to determine the required trust confidence threshold $\theta(R)$.
- **Inputs:** `TaskSpecification(stakes: Enum, reversibility: bool, sensitivity: Enum)`.
- **Outputs:** `RiskAssessment(risk_level: float, confidence_threshold: float, verification_strategy: Enum)`.
- **Threshold Mapping:**
  - *Low Risk:* $\theta = 0.50$ (Heuristic check, single service).
  - *Medium Risk:* $\theta = 0.75$ (Deterministic validation).
  - *High / Critical Risk:* $\theta = 0.90$ (Strict deterministic check + cryptographic provenance confirmation).

---

## Component 7: Selection Engine (`src/selection/strategies.py`)

- **Responsibility:** Implements and executes the active selection strategy to rank candidates and select the optimal provider.
- **Supported Strategies:**
  1. `RandomSelectionStrategy`: Uniform random draw from reachable candidates.
  2. `ReputationOnlySelectionStrategy`: Selects candidate with highest raw global reputation score $\rho_i$.
  3. `EvidenceBasedSelectionStrategy`: Ranks candidates by task-specific expected success $\mu_{\text{evidence}}$ subject to confidence threshold $\Omega_i \ge \theta(R)$.
- **Outputs:** `SelectionDecision(selected_service_id: Optional[str], strategy: str, justification: str)`.

---

## Component 8: Task Execution Layer (`src/mcp/tools.py`)

- **Responsibility:** Formats the task payload, injects authentication headers, dispatches the request to the selected service endpoint via Model Context Protocol (MCP) or HTTP/JSON-RPC, and monitors execution timeouts.
- **Inputs:** `ExecutionRequest(service_id: str, endpoint: str, payload: dict, timeout_ms: int)`.
- **Outputs:** `RawExecutionResponse(status_code: int, data: dict, latency_ms: float, error: Optional[str])`.
- **Failure Modes:** Injects automated timeout failures and records transport errors if endpoints hang.

---

## Component 9: Result Verification Layer (`src/verification/verifier.py`)

- **Responsibility:** Evaluates the returned task payload against verifiable correctness criteria.
- **Verification Modes:**
  - *Deterministic Validation:* Executes unit test assertions or mathematical checks on output.
  - *Schema Validation:* Validates JSON schema adherence, type constraints, and required fields.
  - *Consensus Checking:* Queries a quorum of heterogeneous services and verifies output parity.
- **Outputs:** `VerificationRecord(task_id: str, service_id: str, is_success: bool, confidence: float, details: dict)`.
- **Trust Boundary:** **CRITICAL GATE.** Acts as the ground-truth oracle for updating the evidence store.

---

## Component 10: Evidence Update Layer (`src/evidence/lifecycle.py`, `src/blockchain/provenance.py`)

- **Responsibility:** Pairs the raw execution response with the verification record, constructs an immutable `EvidenceRecord`, writes it to local storage, updates vector embeddings, and computes the state commitment hash.
- **Outputs:** `EvidenceCommitment(merkle_root: str, tx_hash: Optional[str], timestamp: int)`.
- **Blockchain Interface:** Periodically commits batch Merkle roots to smart contract storage (simulated or EVM).
