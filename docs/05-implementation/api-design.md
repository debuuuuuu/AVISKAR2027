# API Design & Interface Specification [PROPOSED API]

> **IMPORTANT: PROPOSED INTERFACE NOTICE**  
> The REST and JSON-RPC endpoints specified below represent the **PROPOSED API SPECIFICATION** for the network service adapter layer connecting external agents to the TrustAware framework.

---

## 1. REST API Endpoints Overview

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| `POST` | `/api/v1/services/discover` | Query candidate services matching capability schema | Bearer Token |
| `POST` | `/api/v1/trust/evaluate` | Compute multidimensional trust assessment for a candidate | Bearer Token |
| `POST` | `/api/v1/tasks/verify` | Submit task result to the Result Verification Layer | Internal / Mutual TLS |
| `POST` | `/api/v1/evidence/record` | Ingest a verified interaction record into evidence store | Internal / Mutual TLS |
| `GET` | `/api/v1/provenance/commitments` | Retrieve historical state commitment roots | Public |

---

## 2. Detailed Endpoint Specifications

### 2.1 Discover Candidate Services
- **Endpoint:** `POST /api/v1/services/discover`
- **Method:** `POST`
- **Authentication:** `Authorization: Bearer <client_jwt>`
- **Request Body:**
  ```json
  {
    "domain": "math_computation",
    "required_methods": ["solve_linear_system"],
    "max_acceptable_latency_ms": 1000
  }
  ```
- **Response Body (`200 OK`):**
  ```json
  {
    "candidates": [
      {
        "service_id": "service_rel_01",
        "endpoint_uri": "https://service01.agentnet.org/mcp",
        "advertised_capabilities": ["math_computation", "linear_algebra"],
        "raw_reputation_score": 0.89,
        "is_reachable": true
      }
    ],
    "total_found": 1
  }
  ```
- **Errors:** `400 Bad Request` (invalid schema), `503 Service Unavailable` (registry offline).

---

### 2.2 Evaluate Candidate Trust
- **Endpoint:** `POST /api/v1/trust/evaluate`
- **Method:** `POST`
- **Authentication:** `Authorization: Bearer <client_jwt>`
- **Request Body:**
  ```json
  {
    "candidate_id": "service_rel_01",
    "task": {
      "task_id": "task_4081",
      "domain": "math_computation",
      "risk_level": "HIGH",
      "description": "Calculate eigenvalues for 10x10 matrix"
    }
  }
  ```
- **Response Body (`200 OK`):**
  ```json
  {
    "candidate_id": "service_rel_01",
    "trust_assessment": {
      "expected_success_rate": 0.965,
      "confidence_omega": 0.89,
      "discounted_reputation": 0.445,
      "risk_threshold": 0.90,
      "recommendation": "ACCEPT",
      "justification": "Sufficient high-confidence historical evidence (14 verified records in domain)."
    }
  }
  ```

---

### 2.3 Verify Task Result
- **Endpoint:** `POST /api/v1/tasks/verify`
- **Method:** `POST`
- **Authentication:** Mutual TLS (mTLS)
- **Request Body:**
  ```json
  {
    "task_id": "task_4081",
    "service_id": "service_rel_01",
    "task_specification": {
      "domain": "math_computation",
      "expected_output_type": "float_array"
    },
    "raw_response": {
      "data": { "eigenvalues": [4.5, 2.1, 0.8] },
      "latency_ms": 118
    }
  }
  ```
- **Response Body (`200 OK`):**
  ```json
  {
    "task_id": "task_4081",
    "verification_record": {
      "is_success": true,
      "rigor_score": 1.0,
      "verification_mode": "DETERMINISTIC",
      "execution_time_ms": 12.4,
      "provenance_hash": "a5f8b9e1c4...3d7"
    }
  }
  ```
