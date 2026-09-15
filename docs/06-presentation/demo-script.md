# Interactive Simulation Demo Script (9-Step Walkthrough)

This script provides an interactive step-by-step demonstration walkthrough that any team member can run and narrate during a project demonstration.

---

## 1. Demo Objectives

The demonstration illustrates the complete 9-step lifecycle of the **Trust-Aware Service Selection Framework**:
1. Ingestion of a high-stakes task.
2. Discovery of candidate services (including Sybil-inflated malicious agents).
3. Task-specific evidence retrieval via RAG.
4. Multidimensional trust calculation and risk gating.
5. Selection decision (and why Strategy 3 rejects the Sybil attacker where Strategy 2 falls for it).
6. Service execution via MCP.
7. Sandboxed result verification.
8. Evidence store update and state commitment hashing.
9. Demonstration of trust update: how future selection decisions change based on verified history.

---

## 2. Step-by-Step Command & Narration Guide

### Step 1: Agent Receives Task
- **Action:** Run the interactive demo scenario script:
  ```bash
  python scripts/experiment/demo_walkthrough.py --scenario high_stakes_math
  ```
- **Presenter Narration:**  
  *"The client agent receives a high-stakes mathematical task: 'Solve eigenvalues for matrix X'. The Risk Assessment Layer calculates a Risk Score of $R = 0.85$ (High Stakes), which automatically sets the mandatory confidence threshold to $\theta = 0.90$."*

### Step 2: Discovery of Candidate Services
- **Terminal Output:**
  ```text
  [DISCOVERY] Discovered 3 candidate services:
    - Candidate A (service_rel_03): Claimed capability: math_computation | Public Rating: 4.6/5.0
    - Candidate B (service_mal_02): Claimed capability: math_computation | Public Rating: 4.95/5.0 (Sybil Inflated)
    - Candidate C (service_unrel_01): Claimed capability: math_computation | Public Rating: 3.2/5.0
  ```
- **Presenter Narration:**  
  *"Notice that Candidate B appears to be the best service on the network with a 4.95 star rating. If we were using standard reputation-only selection (ERC-8004), the agent would immediately pick Candidate B."*

### Step 3: Task-Specific Evidence Gathering (RAG)
- **Terminal Output:**
  ```text
  [RAG QUERY] Embedding task domain 'math_computation'...
  [EVIDENCE STORE] Querying historical records matching embedding:
    - Candidate A: Found 8 historical verified records in 'math_computation' (100% success rate).
    - Candidate B: Found 12 historical records in 'text_summarization' (100% success), but ZERO records in 'math_computation'.
  ```
- **Presenter Narration:**  
  *"This is where our framework shines. Our RAG engine searches historical interactions specifically for 'math_computation'. It discovers that Candidate B's entire reputation was built on text summarization! In math, it has zero verified evidence."*

### Step 4 & 5: Trust Evaluation & Selection Decision
- **Terminal Output:**
  ```text
  [TRUST EVALUATION]
    - Candidate A: Expected Success: 0.96 | Confidence Omega: 0.88 | Risk Threshold: 0.85 -> [PASS]
    - Candidate B: Expected Success: 0.25 (Reputation Discounted) | Confidence Omega: 0.05 -> [REJECT]
  [SELECTION DECISION] Selected Candidate A (service_rel_03).
  ```
- **Presenter Narration:**  
  *"Candidate B's ungrounded reputation is discounted, and its low domain confidence fails the high-stakes risk gate. Candidate A is selected because it has verified empirical evidence in this domain."*

### Step 6 & 7: Service Execution & Result Verification
- **Terminal Output:**
  ```text
  [MCP EXECUTION] Dispatched task to service_rel_03 via tools/call...
  [MCP RESPONSE] Received response in 114 ms.
  [VERIFICATION] Running deterministic unit tests inside subprocess sandbox...
  [VERIFICATION VERDICT] PASS (Rigor: 1.0, Error: None, Verification Hash: 9f8a2c...)
  ```
- **Presenter Narration:**  
  *"The task runs via MCP. Before the client agent accepts the answer, our Result Verification Layer tests the output in an isolated subprocess. The tests pass with 100% confidence."*

### Step 8 & 9: Evidence Update & Future Trust Evolution
- **Terminal Output:**
  ```text
  [EVIDENCE UPDATE] Logged verified record to SQLite evidence DB.
  [VECTOR INDEX] Updated semantic index for service_rel_03.
  [STATE COMMITMENT] Generated Merkle Root for batch: 0x7c3e1b8... committed to ledger.
  [FUTURE DECISION] service_rel_03 confidence in 'math_computation' increased from 0.88 to 0.91.
  ```
- **Presenter Narration:**  
  *"The result is stored, the vector index is updated, and a cryptographic fingerprint is anchored for provenance. For the next task in this domain, the agent has even higher confidence in Candidate A. We have completed the closed feedback loop!"*
