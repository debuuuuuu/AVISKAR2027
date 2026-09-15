# Model Context Protocol (MCP) Tool Specification [PROPOSED MCP INTERFACE]

> **IMPORTANT: PROPOSED INTERFACE NOTICE**  
> The tool declarations specified below represent the **PROPOSED MCP INTERFACE** exposed to the Autonomous Client Agent LLM. They follow the Anthropic Model Context Protocol (MCP) JSON-RPC specification.

---

## 1. Overview of Exposed MCP Tools

The framework exposes five core tools to enable the client LLM to query trust, verify execution, and manage evidence:

1. `verify_agent`: Validates candidate identity and cryptographic signatures.
2. `get_task_specific_trust`: Computes evidence-grounded trust for a candidate on a specific task domain.
3. `check_risk`: Evaluates objective task stakes and determines the required confidence threshold.
4. `verify_result`: Validates a raw execution response against task criteria.
5. `record_interaction`: Commits a verified interaction record to the evidence store.

---

## 2. Detailed Tool Specifications

---

### Tool 1: `verify_agent`
- **Purpose:** Checks whether a candidate service agent possesses a valid, unrevoked cryptographic identity, reachable endpoint, and authentic registration.
- **Input Schema:**
  ```json
  {
    "type": "object",
    "properties": {
      "service_id": { "type": "string", "description": "Candidate service identifier" },
      "public_key": { "type": "string", "description": "Ed25519 public key hex string" },
      "endpoint_uri": { "type": "string", "format": "uri" }
    },
    "required": ["service_id", "public_key", "endpoint_uri"]
  }
  ```
- **Output Schema:**
  ```json
  {
    "type": "object",
    "properties": {
      "is_valid": { "type": "boolean" },
      "is_reachable": { "type": "boolean" },
      "registration_status": { "type": "string", "enum": ["ACTIVE", "REVOKED", "UNREGISTERED"] },
      "error_message": { "type": ["string", "null"] }
    },
    "required": ["is_valid", "is_reachable", "registration_status"]
  }
  ```
- **Failure Modes:** Network timeout probing endpoint; invalid cryptographic key format.
- **Authorization:** Client agent local session token.
- **Idempotency:** **Idempotent.**
- **Side Effects:** None.
- **Auditability:** Logged to client debug log.
- **Security Considerations:** Protects against spoofed or defunct service registrations.

---

### Tool 2: `get_task_specific_trust`
- **Purpose:** Queries the RAG evidence store and Trust Evaluation Engine to compute expected performance on a specific task domain.
- **Input Schema:**
  ```json
  {
    "type": "object",
    "properties": {
      "service_id": { "type": "string" },
      "task_domain": { "type": "string" },
      "task_description": { "type": "string" },
      "risk_level": { "type": "string", "enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"] }
    },
    "required": ["service_id", "task_domain", "task_description", "risk_level"]
  }
  ```
- **Output Schema:**
  ```json
  {
    "type": "object",
    "properties": {
      "service_id": { "type": "string" },
      "expected_success_rate": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
      "evidence_confidence_omega": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
      "discounted_reputation": { "type": "number" },
      "evidence_records_found": { "type": "integer" },
      "recommendation": { "type": "string", "enum": ["ACCEPT", "REJECT", "FALLBACK_CAUTION"] }
    },
    "required": ["service_id", "expected_success_rate", "evidence_confidence_omega", "recommendation"]
  }
  ```
- **Failure Modes:** Evidence store lock; vector embedding model failure.
- **Authorization:** Client agent runtime internal.
- **Idempotency:** **Idempotent** for static evidence database state.
- **Side Effects:** Read-only vector search and computation.
- **Auditability:** Query vector and returned score logged to audit trail.
- **Security Considerations:** Vector search uses sanitized task descriptions to prevent prompt injection inside RAG retrieval queries.

---

### Tool 3: `check_risk`
- **Purpose:** Assesses the objective risk level and required acceptance threshold $\theta(R)$ for a proposed task.
- **Input Schema:**
  ```json
  {
    "type": "object",
    "properties": {
      "task_domain": { "type": "string" },
      "is_reversible": { "type": "boolean" },
      "financial_value_usd": { "type": "number", "default": 0.0 },
      "data_sensitivity": { "type": "string", "enum": ["PUBLIC", "INTERNAL", "CONFIDENTIAL", "RESTRICTED"] }
    },
    "required": ["task_domain", "is_reversible", "data_sensitivity"]
  }
  ```
- **Output Schema:**
  ```json
  {
    "type": "object",
    "properties": {
      "risk_tier": { "type": "string", "enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"] },
      "risk_score": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
      "required_confidence_threshold": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
      "mandatory_verification_mode": { "type": "string", "enum": ["DETERMINISTIC", "SCHEMA", "CONSENSUS"] }
    },
    "required": ["risk_tier", "risk_score", "required_confidence_threshold", "mandatory_verification_mode"]
  }
  ```
- **Idempotency:** **Idempotent.**
- **Side Effects:** None.
- **Security Considerations:** Prevents the client LLM from hallucinating an arbitrary risk level by enforcing deterministic rules.

---

### Tool 4: `verify_result`
- **Purpose:** Submits an unverified service execution output to the Verification Layer for sandboxed correctness validation.
- **Input Schema:**
  ```json
  {
    "type": "object",
    "properties": {
      "task_id": { "type": "string" },
      "service_id": { "type": "string" },
      "task_domain": { "type": "string" },
      "expected_criteria": { "type": "object" },
      "raw_output": { "type": "object" }
    },
    "required": ["task_id", "service_id", "task_domain", "expected_criteria", "raw_output"]
  }
  ```
- **Output Schema:**
  ```json
  {
    "type": "object",
    "properties": {
      "is_success": { "type": "boolean" },
      "rigor_score": { "type": "number" },
      "execution_time_ms": { "type": "number" },
      "flags": { "type": "array", "items": { "type": "string" } },
      "verification_hash": { "type": "string" }
    },
    "required": ["is_success", "rigor_score", "execution_time_ms", "verification_hash"]
  }
  ```
- **Failure Modes:** Sandboxed test timeout; out-of-memory exception.
- **Side Effects:** Spawns isolated subprocess.
- **Security Considerations:** Sandboxed execution prevents malicious output payloads from executing arbitrary shell commands.

---

### Tool 5: `record_interaction`
- **Purpose:** Persists a completed, verified interaction record into the local evidence store and updates the vector embedding index.
- **Input Schema:**
  ```json
  {
    "type": "object",
    "properties": {
      "task_id": { "type": "string" },
      "service_id": { "type": "string" },
      "task_domain": { "type": "string" },
      "task_description": { "type": "string" },
      "verification_verdict": { "type": "boolean" },
      "verification_rigor": { "type": "number" },
      "latency_ms": { "type": "number" },
      "provenance_hash": { "type": "string" }
    },
    "required": ["task_id", "service_id", "task_domain", "verification_verdict", "provenance_hash"]
  }
  ```
- **Output Schema:**
  ```json
  {
    "type": "object",
    "properties": {
      "evidence_id": { "type": "string" },
      "indexed_in_rag": { "type": "boolean" },
      "pending_commitment_root": { "type": "string" }
    },
    "required": ["evidence_id", "indexed_in_rag"]
  }
  ```
- **Failure Modes:** Disk full; database constraint violation.
- **Side Effects:** Writes to SQLite database; updates in-memory vector index.
- **Auditability:** Complete interaction stored permanently in local audit database.
- **Security Considerations:** Atomic database transactions prevent partial state corruption.
