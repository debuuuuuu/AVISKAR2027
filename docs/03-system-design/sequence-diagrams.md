# Sequence Diagrams & Protocol Lifecycles

This document provides detailed sequence diagrams capturing synchronous and asynchronous message exchanges during candidate discovery, trust evaluation, execution, verification, and failure recovery.

---

## 1. Happy Path: Successful Selection, Execution, & Evidence Anchoring

```mermaid
sequenceDiagram
    autonumber
    actor User as User / Goal Initiator
    participant CA as Client Agent
    participant SR as Service Registry
    participant RAG as RAG / Evidence Store
    participant TE as Trust Evaluation Engine
    participant BC as Blockchain Anchor
    participant SP as Selected Service Provider
    participant VL as Verification Layer

    User->>CA: Submit Task Goal (Specification + Risk Level)
    CA->>SR: Discover Candidates (Domain, Required Capability)
    SR-->>CA: Return Candidate Pool [S1, S2, ..., Sn]
    
    loop For Each Candidate S_i
        CA->>RAG: Query Past Task-Specific Evidence(S_i, TaskDomain)
        RAG-->>CA: Return Top-K Evidence Records + Quality Scores
        opt High-Stakes Task
            CA->>BC: Verify Commitment Hash(EvidenceRecords)
            BC-->>CA: Commitment Provenance Confirmed
        end
        CA->>TE: Evaluate Multi-Dimensional Trust(Identity, History, EvidenceQuality, Reputation, Risk)
        TE-->>CA: Return Trust Assessment(Confidence, RiskScore, Decision)
    end

    CA->>CA: Selection Strategy: Rank Candidates & Select Best S*
    alt Accept Best Candidate
        CA->>SP: Dispatch Task Execution via MCP Tool Call
        SP-->>CA: Return Raw Task Execution Result
        CA->>VL: Verify Result(TaskSpec, RawResult)
        VL-->>CA: Verification Record (Pass/Fail, QualityMetrics)
        CA->>RAG: Append New Interaction & Verification Record
        CA->>BC: Anchor Evidence State Commitment Hash
        CA->>User: Deliver Verified Task Result
    else Reject All Candidates (No Candidate Exceeds Trust Threshold)
        CA->>User: Abort or Escalate (Refuse Execution to Prevent Harm)
    end
```

---

## 2. Unhappy Path: Service Timeout & Fallback Execution

```mermaid
sequenceDiagram
    autonumber
    participant CA as Client Agent
    participant SP1 as Primary Candidate (Unreliable Service)
    participant VL as Verification Layer
    participant ES as Evidence Store
    participant SP2 as Secondary Fallback Service

    CA->>SP1: Dispatch Execution (Timeout Budget: 2000ms)
    Note over SP1: Service hangs or drops packet
    CA->>CA: Timer Expires (2000ms elapsed)
    CA->>VL: Record Timeout Failure for SP1
    VL-->>ES: Log Execution Timeout (Pass=False, Latency=2000ms)
    Note over ES: SP1 Trust Score immediately penalized
    CA->>SP2: Dispatch Fallback Execution
    SP2-->>CA: Return Execution Payload
    CA->>VL: Verify Output(SP2)
    VL-->>ES: Log Success for SP2
    CA-->>CA: Synthesize Final Task Result
```

---

## 3. Adversarial Path: Malicious Output Interception

```mermaid
sequenceDiagram
    autonumber
    participant CA as Client Agent
    participant MalService as Malicious Service (High Sybil Reputation)
    participant VL as Verification Layer
    participant ES as Evidence Store

    CA->>MalService: Dispatch High-Risk Mathematical Task
    MalService-->>CA: Return Malicious Payload (Poisoned values / Prompt injection)
    CA->>VL: Route Payload to Verification Sandbox
    Note over VL: Deterministic unit tests fail; prompt injection detected
    VL-->>CA: Verification Verdict: FAILURE (Confidence: 1.0, Flags: ["INJECTION_DETECTED"])
    CA->>ES: Record Tamper-Evident Negative Evidence
    CA->>CA: Blacklist MalService from Session & Abort Task
```
