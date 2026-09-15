# Trust-Aware Service Selection for Autonomous AI Agents

### *An Evidence-Based Trust and Verification Framework*

[![Status: Research Specification](https://img.shields.io/badge/Status-Research--Specification-blue.svg)](#current-project-status)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](#prerequisites)
[![Architecture: Defined](https://img.shields.io/badge/Architecture-Defined-success.svg)](#architecture-overview)
[![Experiment: Simulated](https://img.shields.io/badge/Experiment-Simulated--Ready-orange.svg)](#experimental-design)

---

## 1. Executive Summary

As autonomous AI agents shift from isolated reasoning engines into open, decentralized multi-agent ecosystems, they must autonomously delegate tasks to external service agents (e.g., specialized code execution, data retrieval, mathematical verification, financial querying). However, open service marketplaces are vulnerable to performance degradation, misleading capability claims, and coordinated Sybil manipulation. Current agent architectures rely either on arbitrary service selection or on global, aggregate reputation scores that are easily gamed and blind to task context. **This project introduces a task-specific, evidence-grounded trust and verification framework that enables autonomous AI agents to evaluate, select, verify, and update trust assessments of external service providers based on verifiable historical interaction evidence rather than reputation alone.**

---

## 2. Central Research Question

> **“Can task-specific, verifiable evidence improve autonomous AI-agent service selection compared with reputation-only scoring?”**

### Key Sub-Questions
1. How does conditioning trust decisions on **semantic task similarity** alter malicious-agent selection rates compared to global aggregate reputation?
2. To what extent does **post-execution verification feedback** prevent performance drift and collusive reputation laundering?
3. What is the computational and latency trade-off incurred by combining vector-based evidence retrieval (RAG) and cryptographic state commitments?

---

## 3. Problem Statement

In decentralized or open agent networks, autonomous client agents must select candidate service agents under deep uncertainty:
- **Asymmetric Information:** Service providers publish self-declared capability profiles that cannot be verified prior to invocation.
- **Vulnerability to Sybil and Collusive Inflation:** Bad actors create hundreds of ephemeral virtual identities to exchange artificial positive feedback, artificially inflating global reputation scores at minimal economic cost.
- **Domain Mismatch (Halo Effect):** A service agent with a stellar reputation for generic document summarization may catastrophically fail or introduce security vulnerabilities when assigned complex mathematical proofs or sensitive API integrations.
- **Dynamic Behavioral Drift:** Agents that behave reliably during initial evaluation periods may subsequently degrade, experience intermittent timeouts, or execute exit scams on high-stakes tasks.

---

## 4. Why This Problem Matters

Multi-agent autonomous systems cannot achieve production deployment in mission-critical, enterprise, or financial contexts if delegation is brittle or exploitable:
- **Cascade of Failure:** In composite multi-agent workflows, a single compromised or faulty external tool creates cascading hallucinations that corrupt downstream reasoning steps.
- **Resource Depletion:** Invoking non-functional or stalling endpoints wastes execution budgets, tokens, and wall-clock latency.
- **Empirical Fragility:** Real-world deployments of decentralized agent registries demonstrate that without verifiable task grounding, public agent markets suffer near-total market failure.

---

## 5. Research Gap

| Prior Research Domain | Key Published Works | Primary Mechanism | Critical Operational Boundary & Gap |
|:---|:---|:---|:---|
| **Decentralized Registries** | ERC-8004 Spec (2025), Xiong et al. (2026) | Global on-chain discovery registries and star ratings. | Does not guarantee uptime (85%–97% offline); vulnerable to coordinated Sybils (59%–90% of reviews). |
| **Classical MAS Trust** | REGRET (2002), Beta (2002), EigenTrust (2003), FIRE (2006), TRAVOS (2006) | Statistical Bayesian rating aggregation and recency decay. | Designed for scalar e-commerce ratings; blind to semantic task embeddings, LLM tools, or multimodal outputs. |
| **Context-Aware Reputation** | AgentReputation (Chishti et al. 2026) | 3-tier decentralized context-conditioned reputation cards. | Evaluates marketplace-level cards; does not evaluate client-local verified evidence under adversarial attack. |
| **Agent Provenance** | PROV-AGENT (Souza et al. 2025) | W3C PROV telemetry capturing prompts and tool executions. | Retrospective observability tool; does not perform predictive risk-gated service selection during planning. |
| **LLM Output Verification** | Huang et al. (2024), CRITIC (Gou et al. 2024) | Deterministic tool-interactive output critiquing. | Evaluates single-agent reasoning self-correction; does not address multi-agent service provider selection. |
| **Tool Calling Protocols** | Toolformer (2023), Anthropic MCP (2024) | Standardized JSON-RPC tool discovery and execution. | Operates under the benevolent assumption; assumes all external tools are benign, reliable, and non-adversarial. |

**The Residual Research Gap:**  
A closed-loop, evidence-grounded service selection framework for autonomous AI agents that synthesizes **semantic task matching (vector RAG)**, **deterministic 4-tier output verification**, and **tamper-evident provenance anchoring**, evaluated through a **controlled empirical comparison** against reputation-only selection under adversarial conditions.

*See detailed analysis in [docs/02-research/research-gap-analysis.md](docs/02-research/research-gap-analysis.md), [docs/02-research/literature-matrix.md](docs/02-research/literature-matrix.md), and [docs/02-research/novelty-matrix.md](docs/02-research/novelty-matrix.md).*

---

## 6. Proposed Solution

We propose a multi-layered trust evaluation architecture wherein service selection decisions are made by an autonomous client agent using a six-dimensional evaluation framework:

$$\text{Trust Decision} = \mathcal{F}(\text{Identity}, \text{Capability}, \text{Task-Specific History}, \text{Evidence Quality}, \text{Reputation}, \text{Risk})$$

Rather than relying on reputation as the sole decision variable, our system treats reputation as merely one discounted prior signal, prioritizing **verifiable interaction evidence specific to the requested task domain**.

---

## 7. Architecture Overview

The system design enforces a strict separation of concerns across discovery, assessment, selection, execution, and verification:

```mermaid
flowchart TD
    TI[1. Task Input & Specification] --> SD[2. Service Discovery]
    SD --> SC[3. Service Candidate Pool]
    SC --> EG[4. Task-Specific Evidence Gathering]
    
    subgraph MultiDimEval["5. Multidimensional Trust Assessment"]
        E1[Identity Verification]
        E2[Claimed vs Observed Capability]
        E3[Task-Specific Interaction History]
        E4[Evidence Quality & Recency]
        E5[Decoupled Reputation Signal]
        E6[Task Risk & Stakes Assessment]
        
        E1 --- TE[Trust Evaluation Engine]
        E2 --- TE
        E3 --- TE
        E4 --- TE
        E5 --- TE
        E6 --- TE
    end
    
    EG --> MultiDimEval
    MultiDimEval --> TD{6. Trust Decision}
    
    TD -->|Accept & Dispatch| TE_Exec[7. Task Execution via Service]
    TD -->|Reject / Fallback| FB[Alternative Candidate / Reject Task]
    
    TE_Exec --> RV[8. Result Verification & Validation]
    RV --> EU[9. Tamper-Evident Evidence Update]
    
    subgraph Infrastructure["Supporting Technology Anchors"]
        RAG[RAG: Vector Evidence Retrieval]
        MCP[MCP: Agent Tool Interface]
        BC[Blockchain: Cryptographic Commitments]
    end
    
    EG -.->|Query| RAG
    TE_Exec -.->|Protocol| MCP
    EU -.->|Commit Hash| BC
    EU -->|Feedback Loop| EG
```

---

## 8. Core Workflow

The end-to-end operational lifecycle follows an 8-step closed feedback loop:

1. **Task Ingestion & Risk Scoring:** The client agent receives a goal, extracts the required domain capabilities, and assigns an objective risk tier (Low, Medium, High, Critical).
2. **Service Discovery:** The agent queries local registries or open directory protocols to locate candidate service providers matching the schema interface.
3. **Evidence Retrieval (RAG):** For each candidate, the agent queries its private and shared evidence store via semantic search, retrieving historical records matching the specific task type.
4. **Multi-Factor Trust Assessment:** The Trust Engine evaluates identity validity, capability match, verified success rates on similar tasks, evidence recency, and discounted global reputation against the task's risk threshold.
5. **Selection Gate:** If one or more candidates satisfy the confidence threshold for the risk tier, the optimal service is selected; otherwise, the task is safely rejected or escalated.
6. **Task Dispatch (MCP):** The client agent dispatches execution using standardized Model Context Protocol (MCP) tool bindings.
7. **Result Verification:** The output is routed through a verification module (deterministic testing, consensus checks, or schema validation).
8. **Evidence Anchoring:** The execution metadata, observed latency, and verification outcome are stored locally, indexed in the vector store, and cryptographically anchored (SHA-256 state commitment) to ensure tamper-evidence.

---

## 9. Trust Evaluation Factors

The framework evaluates candidate services using six explicit, non-overlapping dimensions:

```mermaid
flowchart LR
    ID[1. Identity Verification] --> TEE[Trust Evaluation Engine]
    CAP[2. Capability Fit] --> TEE
    HIST[3. Task-Specific History] --> TEE
    QUAL[4. Evidence Quality] --> TEE
    REP[5. Discounted Reputation] --> TEE
    RISK[6. Risk & Stakes] --> RAE[Risk Assessment Layer]
    
    TEE --> Gate{Decision Gate}
    RAE --> Gate
    Gate --> Decision[Accept / Fallback / Reject]
```

1. **Identity:** Cryptographic verification of public keys, decentralized identifiers (DIDs), or registration validity.
2. **Capability:** Match between claimed service interfaces and observed input/output schemas.
3. **Task-Specific History:** Empirical success and failure rates recorded exclusively for tasks within the same semantic domain.
4. **Evidence Quality:** Recency of observations, sample size, verification rigor (e.g., deterministic vs. heuristic), and provenance strength.
5. **Reputation (Discounted):** Third-party or network-wide ratings, discounted to counteract potential Sybil inflation.
6. **Risk & Stakes:** Irreversibility, latency constraints, and potential blast radius of service failure.

---

## 10. Experimental Design

To empirically evaluate the framework, we specify a controlled, reproducible simulation testbed consisting of **30 simulated service agents**:

```text
Total Service Agent Population (N = 30):
├── 20 Reliable Services   (Consistently correct execution, low latency, 95%+ success rate)
├──  5 Unreliable Services (Intermittent faults, high latency variance, stochastic timeouts)
└──  5 Malicious Services  (Adversarial behavior: deceptive outputs, Sybil collusion, silent failure)
```

### Three Comparative Selection Strategies
1. **Random Selection (Null Baseline):** Selects uniformly at random from candidates matching the required capability schema.
2. **Reputation-Only Selection (Industry Baseline):** Selects candidates using aggregate historical ratings (replicating standard decentralized registry mechanisms such as ERC-8004).
3. **Evidence-Based Selection (Proposed Framework):** Selects candidates using task-specific verified interaction history, evidence quality filtering, and risk-weighted confidence thresholds.

---

## 11. Evaluation Metrics

The experimental protocol measures performance across five formalized metrics:

| Metric | Symbol | Definition / Objective | Desirable Direction |
|---|---|---|---|
| **Task Success Rate** | $TSR$ | $\frac{\text{Successfully Verified Tasks}}{\text{Total Assigned Tasks}}$ | $\uparrow$ Higher is better |
| **Malicious-Agent Selection Rate** | $MASR$ | $\frac{\text{Selections of Malicious Agents}}{\text{Total Selection Decisions}}$ | $\downarrow$ Lower is better |
| **False Rejection Rate** | $FRR$ | $\frac{\text{Reliable Services Incorrectly Rejected}}{\text{Total Reliable Opportunities}}$ | $\downarrow$ Lower is better |
| **Verification Cost Overhead** | $VCO$ | Computational and latency expenditure incurred by result verification | $\downarrow$ Lower is better |
| **Selection Decision Latency** | $SDL$ | Wall-clock time (ms) required to query evidence and compute trust | $\downarrow$ Lower is better |

*Note: No experimental values are reported until reproducible runs are executed in the simulation environment.*

---

## 12. Technology Roles & Architectural Separation

Each supporting technology in the stack addresses a specific architectural requirement. None is used as a generic buzzword:

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  RAG (Retrieval-Augmented Generation)                                        │
│  Role: Semantic retrieval of historical interaction records matching the     │
│        current task's domain and embedding context.                          │
│  Solves: Cold-start search over multi-thousand interaction history logs.     │
│  Does NOT solve: Verifying whether the retrieved evidence was truthful.      │
├──────────────────────────────────────────────────────────────────────────────┤
│  MCP (Model Context Protocol)                                                │
│  Role: Standardized, vendor-neutral tool interface exposing trust,           │
│        verification, and execution endpoints to the client LLM.              │
│  Solves: Interoperability across heterogeneous local and remote agents.      │
│  Does NOT solve: Trust evaluation or adversarial behavior detection.         │
├──────────────────────────────────────────────────────────────────────────────┤
│  Blockchain / Decentralized Ledger                                           │
│  Role: Cryptographic timestamping, Merkle root state commitments, and        │
│        tamper-evident audit logs of interaction hashes.                      │
│  Solves: Post-hoc alteration or deletion of negative performance history.   │
│  Does NOT solve: Verification of execution quality or output correctness.    │
├──────────────────────────────────────────────────────────────────────────────┤
│  x402 (HTTP 402 Autonomous Payments)                                         │
│  Role: [FUTURE EXTENSION] Risk-conditioned, programmatic micropayments upon  │
│        verified task completion.                                             │
│  Status: Scoped for Phase 10 / Future Work (Not in current core pipeline).   │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 13. Research Basis & Existing Evidence

Our problem formulation is directly supported by empirical findings in recent academic literature:

> **EXISTING RESEARCH EVIDENCE**  
> **Source:** Xiong, X., Li, Z., Wei, W., Wang, Q., Knottenbelt, W. J., & Wang, Z. (2026). *“Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem.”* arXiv:2606.26028.
>
> In the first empirical study of the ERC-8004 standard across Ethereum, BNB Smart Chain (BSC), and Base:
> - **Endpoint Availability:** Only **3% (Ethereum)**, **4% (BSC)**, and **15% (Base)** of registered agents possessed a valid registration file with at least one reachable, live service endpoint.
> - **Sybil Reviewers:** Coordinated Sybil reviewer behavior accounted for **73.5% (Ethereum)**, **59.2% (BSC)**, and **90.6% (Base)** of all registered feedback accounts.
> - **Reputation Collapse:** Upon removing Sybil-coordinated feedback, the pool of usable ratings collapsed, rendering global reputation signals largely non-functional for reliable autonomous delegation.

This project uses these empirical findings as formal motivation for why reputation-only selection fails and why task-specific, verifiable evidence is essential.

---

## 14. Current Project Status

| Area | Status | Notes |
|---|---|---|
| **Research Question & Framing** | `COMPLETE` | Rigorously scoped; verified against existing literature. |
| **System Architecture & C4 Models** | `COMPLETE` | 10 modular components specified with strict data boundaries. |
| **Mathematical Trust & Evidence Models** | `PROPOSED` | Formally specified; weights to be calibrated empirically. |
| **Threat & Security Modeling** | `COMPLETE` | 14 adversarial threats analyzed with mitigation boundaries. |
| **Codebase Scaffolding (`src/`)** | `IMPLEMENTED` | Pydantic data models, modular simulation engine, test suites. |
| **Controlled Experimentation** | `READY TO RUN` | 30-agent population, 3 strategies, deterministic task generator. |
| **Experimental Results** | `NOT YET RUN` | Result schemas documented; no fabricated data reported. |
| **x402 Payment Integration** | `FUTURE WORK` | Intentionally excluded from core trust-selection boundary. |

---

## 15. Strategic Roadmap

```text
Phase 1: Research Framing & Literature Analysis       [DONE]
Phase 2: Formal System & Threat Modeling             [DONE]
Phase 3: Modular Simulation Engine Scaffolding       [DONE]
Phase 4: Multi-Dimensional Trust & Evidence Engine    [DONE]
Phase 5: Baseline Selection Strategies Implementation [DONE]
Phase 6: Verification & Feedback Pipeline             [DONE]
Phase 7: Controlled Experiment Execution (30 Agents)  [NEXT]
Phase 8: Statistical Analysis & Metric Visualization  [PLANNED]
Phase 9: MCP Protocol & Live Registry Adapter         [PLANNED]
Phase 10: x402 Micropayment & Settlement Integration  [FUTURE WORK]
```

---

## 16. Repository Structure

```text
.
├── README.md                           # Master research overview & documentation gateway
├── LICENSE                             # MIT Open Source License
├── CONTRIBUTING.md                     # Academic & engineering contribution guide
├── CODE_OF_CONDUCT.md                  # Contributor Covenant standard
├── SECURITY.md                         # Responsible disclosure & agent security policy
├── CHANGELOG.md                        # Version progression & milestone tracking
├── project.yaml                        # Machine-readable experiment parameters
├── .env.example                        # Template environment variables (no secrets)
├── .gitignore                          # Exclusions for Python, IDEs, and run artifacts
│
├── .github/                            # Issue templates and pull request standards
│   ├── pull_request_template.md
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       ├── feature_request.md
│       └── research_inquiry.md
│
├── docs/                               # Authoritative documentation tree
│   ├── README.md                       # Documentation index & reading paths
│   ├── 01-overview/                    # Problem, research question, objectives, scope, terminology
│   ├── 02-research/                    # Literature review, research gap, existing evidence, novelty
│   ├── 03-system-design/               # Architecture, trust model, evidence model, threat/security
│   ├── 04-experiment/                  # Experimental design, 30 agents, metrics, protocol, results schema
│   ├── 05-implementation/              # Implementation plan, module breakdown, APIs, MCP, RAG, tests
│   ├── 06-presentation/                # Team handbook, pitches, 50+ judge Q&As, 20 hard questions
│   ├── 07-poster/                      # Poster content, layout, evidence mapping, presentation script
│   └── 08-roadmap/                     # Current status, milestones, and future extensions
│
├── diagrams/                           # Mermaid diagram source files (.mmd)
│   ├── architecture/                   # High-level, system context, trust evaluation, deployment
│   ├── data-flow/                      # Evidence lifecycle, end-to-end data flow
│   ├── sequence/                       # Service selection & verification sequence
│   ├── experiment/                     # Methodology, research logic traceability
│   ├── threat-model/                   # Adversarial threat boundaries
│   └── poster/                         # Poster block architecture
│
├── research/                           # Academic papers, notes, and bibliography
│   ├── bibliography/                   # BibTeX and citation files
│   ├── evidence/                       # Summaries of external empirical studies
│   ├── notes/                          # Research design working notes
│   ├── papers/                         # Literature summaries
│   └── references.bib                  # Master BibTeX reference file
│
├── experiments/                        # Experiment configurations, scenarios, and runs
│   ├── configs/                        # YAML configuration files for simulation runs
│   ├── datasets/                       # Benchmark task definitions
│   ├── scenarios/                      # Agent population configurations (20/5/5)
│   ├── scripts/                        # Experiment execution scripts
│   ├── runs/                           # Raw experiment run output logs [EMPTY]
│   └── results/                        # Processed metrics & visualization data [EMPTY]
│
├── src/                                # Core Python implementation & simulation package
│   ├── __init__.py
│   ├── data_models.py                  # Pydantic schemas (Agent, Task, Evidence, TrustAssessment, etc.)
│   ├── agent/                          # Autonomous client agent execution loop
│   ├── services/                       # Simulated service providers (Reliable, Unreliable, Malicious)
│   ├── trust/                          # Multidimensional trust evaluation engine
│   ├── evidence/                       # Evidence store, extraction, and lifecycle management
│   ├── selection/                      # Selection strategies (Random, Reputation, Evidence-based)
│   ├── verification/                   # Result verification and validation layer
│   ├── rag/                            # Vector retrieval for historical interaction evidence
│   ├── mcp/                            # Model Context Protocol tool interfaces
│   ├── blockchain/                     # Tamper-evident commitment and provenance anchor interface
│   └── experiment/                     # Experiment orchestrator and metric evaluation harness
│
├── tests/                              # Comprehensive test suite
│   ├── unit/                           # Unit tests for models, trust engine, selection, verification
│   ├── integration/                    # Pipeline integration tests
│   ├── system/                         # End-to-end simulated workflow tests
│   └── experiment/                     # Reproducibility and statistical validation tests
│
└── scripts/                            # Operational utility scripts
    ├── setup/                          # Environment setup & dependency checking
    ├── experiment/                     # Simulation launch scripts
    ├── validation/                     # Link integrity & schema validation
    └── documentation/                  # Documentation generation & verification
```

---

## 17. How to Run Locally

### Prerequisites
- Python 3.10 or higher
- Git
- Recommended: Virtual environment (`venv` or `conda`)

### Installation
```bash
# Clone the repository
git clone https://github.com/your-org/trust-aware-agent-service-selection.git
cd trust-aware-agent-service-selection

# Create and activate virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Test Suite
```bash
# Run all unit tests
pytest tests/unit/

# Run integration tests
pytest tests/integration/
```

### Running the Simulation Experiment
```bash
# Run a dry simulation with 30 simulated agents across 100 tasks
python -m src.experiment.runner --config experiments/configs/default_simulation.yaml
```

---

## 18. How to Reproduce Experiments

To ensure scientific replicability, all experimental parameters are deterministically seeded:
1. **Configuration:** Scenarios are defined in `experiments/configs/default_simulation.yaml`.
2. **Seed Control:** Random seeds for task generation, agent latency, and failure injection are fixed (`seed: 42`).
3. **Execution:** The experiment runner executes all three selection strategies against identical task sequences and identical agent states.
4. **Output Verification:** Raw telemetry is output to `experiments/runs/` and processed using `src/experiment/metrics.py`.

See the complete [Experiment Reproducibility Guide](docs/04-experiment/reproducibility.md) for step-by-step instructions.

---

## 19. Team Handbook & Presentation Gateway

This repository is designed so that any team member can confidently present the project to judges, researchers, and engineers:

- **Need a quick pitch?** Read the [30-Second Pitch](docs/06-presentation/30-second-pitch.md) or [2-Minute Explanation](docs/06-presentation/2-minute-explanation.md).
- **Need full presentation slides/script?** Read the [5-Minute Presentation Script](docs/06-presentation/5-minute-presentation.md).
- **Presenting to judges?** Study the [50+ Categorized Judge Q&As](docs/06-presentation/judge-questions.md).
- **Facing tough or adversarial questions?** Review the [Top 20 Hard Questions & Defenses](docs/06-presentation/hard-questions.md).
- **Need the full guide?** Read the master [Team Handbook](docs/06-presentation/team-handbook.md).

---

## 20. Research Integrity Statement

Academic integrity is paramount in this work:
- **No Fabricated Benchmarks:** We do not publish synthetic benchmark claims as empirical facts. If an experiment has not been executed, it is explicitly marked `[EXPERIMENT NOT RUN]`.
- **Existing Evidence vs. Project Results:** External empirical studies (e.g., ERC-8004 findings) are explicitly cited under **EXISTING RESEARCH EVIDENCE** and are never conflated with this project's findings.
- **Hypothesis-Driven:** We do not claim our evidence-based framework is universally superior; we formulate testable hypotheses and rigorously measure trade-offs (including verification overhead and decision latency).

---

## 21. Key Academic References & Research Grounding

This project is grounded in real, verified academic literature and official technical standards. All preprints are explicitly identified as non-peer-reviewed working papers.

### Primary Foundations by Research Family
1. **Agent Identity & Registries:**
   - Xiong, X., Li, Z., Wei, W., Wang, Q., Knottenbelt, W. J., & Wang, Z. (2026). *Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem.* arXiv:2606.26028 [cs.CR]. *(arXiv Preprint)*
   - Ethereum Improvement Proposals. (2025). *ERC-8004: Trustless AI Agent Standard — Identity, Reputation, and Validation Registries.* EIP-8004. *(Official Technical Specification)*
2. **Agent Provenance & Traceability:**
   - Souza, R., Gueroudji, A., DeWitt, S., Rosendo, D., Ghosal, T., Ross, R., Balaprakash, P., & da Silva, R. F. (2025). *PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows.* *2025 IEEE International Conference on eScience (eScience)*, pp. 467–473. DOI: 10.1109/eScience65000.2025.00093. *(Peer-Reviewed Conference)*
3. **Context-Conditioned Agent Reputation:**
   - Chishti, M. S., Oyinloye, D. P., & Li, J. (2026). *AgentReputation: A Decentralized Agentic AI Reputation Framework.* *Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering (FSE 2026)* / arXiv:2605.00073. *(Peer-Reviewed Conference / Preprint)*
4. **Decentralized Agent Networks & Trust:**
   - Zhu, L., Li, Y., Wang, T., Chen, Z., Li, K., Liu, H., Wang, Y., Xu, L., Jiang, P., & Zhang, Z. (2026). *Blockchain Empowered Trustworthy Agent Networks: Foundations, Taxonomy, and Future Directions.* arXiv:2608.04626. *(arXiv Preprint)*
5. **Evidence Credibility & Verifiable Retrieval:**
   - Liu, B., Che, H., & Li, Y. (2026). *TrustRAG: Blockchain-Enhanced RAG via Committee-Based Credibility Scoring.* arXiv:2608.20097. *(arXiv Preprint)*
6. **Classical Multi-Agent Trust Foundations:**
   - Sabater, J., & Sierra, C. (2002). *REGRET: A reputation model for multi-agent systems.* *Autonomous Agents and Multi-Agent Systems*, 5(1), 33–55. DOI: 10.1023/A:1013734109878. *(Peer-Reviewed Journal)*
   - Jøsang, A., & Ismail, R. (2002). *The Beta Reputation System.* *Proceedings of the 15th Bled Electronic Commerce Conference*, pp. 2502–2511. *(Peer-Reviewed Conference)*
   - Kamvar, S. D., Schlosser, M. T., & Garcia-Molina, H. (2003). *The EigenTrust algorithm for reputation management in P2P networks.* *ACM WWW 2003*, pp. 640–651. DOI: 10.1145/775152.775242. *(Peer-Reviewed Conference)*
   - Huynh, T. D., Jennings, N. R., & Shadbolt, N. R. (2006). *An integrated trust and reputation model for open multi-agent systems.* *Autonomous Agents and Multi-Agent Systems*, 13(2), 119–154. DOI: 10.1007/s10458-005-6825-4. *(Peer-Reviewed Journal)*
   - Yu, H., Shen, Z., Miao, C., Leung, C., & Niyato, D. (2013). *A survey of multi-agent trust management systems.* *IEEE Access*, 1, 35–50. DOI: 10.1109/ACCESS.2013.2259837. *(Peer-Reviewed Journal)*
7. **Agent Verification & Output Reliability:**
   - Huang, J., Chen, X., Mishra, S., Zheng, H. S., Yu, A. W., Song, X., & Zhou, D. (2024). *Large Language Models Cannot Self-Correct Reasoning Yet.* *ICLR 2024* / arXiv:2310.01798. *(Peer-Reviewed Conference)*
   - Gou, Z., Shao, Z., Gong, Y., Shen, Y., Yang, Y., Duan, N., & Chen, W. (2024). *CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing.* *ICLR 2024* / arXiv:2305.11738. *(Peer-Reviewed Conference)*
8. **Adversarial Modeling & Sybils:**
   - Douceur, J. R. (2002). *The Sybil Attack.* *IPTPS '01*, Springer LNCS 2429, pp. 251–260. DOI: 10.1007/3-540-45748-8_24. *(Peer-Reviewed Conference)*
   - Hoffman, K., Zage, D., & Nita-Rotaru, C. (2009). *A survey of attack and defense techniques for reputation systems.* *ACM Computing Surveys*, 42(1), Article 1. DOI: 10.1145/1592451.1592452. *(Peer-Reviewed Journal)*
9. **Agent Tool Use & Protocols:**
   - Schick, T., et al. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools.* *NeurIPS 2023*, 36, 68539–68551. *(Peer-Reviewed Conference)*
   - Anthropic. (2024). *Model Context Protocol (MCP) Specification.* https://modelcontextprotocol.io. *(Official Technical Specification)*
10. **Agent Payments (Future Work):**
    - x402 Foundation & Coinbase Developer Platform. (2025). *x402: An Open Standard for Machine-to-Machine Payments over HTTP 402.* https://x402.org. *(Official Protocol Specification)*

### Research Documentation Index
- [Canonical Bibliography & Annotation](docs/02-research/references.md)
- [Complete BibTeX Source](research/references.bib)
- [Structured Literature Matrix](docs/02-research/literature-matrix.md)
- [Research Gap Analysis](docs/02-research/research-gap-analysis.md)
- [Novelty & Prior Art Matrix](docs/02-research/novelty-matrix.md)
- [Claim-to-Evidence Traceability Map](docs/02-research/claim-evidence-map.md)

---

## 22. License & Contributing

This project is licensed under the [MIT License](LICENSE).  
We welcome academic and open-source contributions. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md).

