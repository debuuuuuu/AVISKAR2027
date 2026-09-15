# Team Presentation Handbook: Everything You Need to Know

> **PURPOSE OF THIS HANDBOOK**  
> This handbook is written for every member of the team. Even if you did not write the code or if the lead researcher is not physically in the room, **this document gives you everything you need to understand, present, and defend this project before any audience** (judges, professors, researchers, or engineers).

---

## Table of Contents

- [A. What the Project Is](#a-what-the-project-is)
- [B. Why We Made It](#b-why-we-made-it)
- [C. The Problem](#c-the-problem)
- [D. The Research Gap](#d-the-research-gap)
- [E. The Research Question](#e-the-research-question)
- [F. Objectives](#f-the-objectives)
- [G. How the System Works (End-to-End)](#g-how-the-system-works-end-to-end)
- [H. What Each Architecture Component Does](#h-what-each-architecture-component-does)
- [I. What RAG Does (And What It Doesn't Do)](#i-what-rag-does-and-what-it-doesnt-do)
- [J. What MCP Does (And What It Doesn't Do)](#j-what-mcp-does-and-what-it-doesnt-do)
- [K. What Blockchain Does (And What It Doesn't Do)](#k-what-blockchain-does-and-what-it-doesnt-do)
- [L. Why Reputation Alone Is Not Enough](#l-why-reputation-alone-is-not-enough)
- [M. What Evidence Means in This Framework](#m-what-evidence-means-in-this-framework)
- [N. What Verification Means in This Framework](#n-what-verification-means-in-this-framework)
- [O. What the Experiment Is](#o-what-the-experiment-is)
- [P. Why 30 Agents?](#p-why-30-agents)
- [Q. Why 20 Reliable, 5 Unreliable, 5 Malicious?](#q-why-20-reliable-5-unreliable-5-malicious)
- [R. Why These Three Selection Strategies?](#r-why-these-three-selection-strategies)
- [S. What Each Evaluation Metric Means](#s-what-each-evaluation-metric-means)
- [T. What We Can Legally and Scientifically Claim](#t-what-we-can-legally-and-scientifically-claim)
- [U. What We CANNOT Claim (Never Say This)](#u-what-we-cannot-claim-never-say-this)
- [V. Future Work & Extensions](#v-future-work--extensions)
- [W. Suggested Team Responsibility Matrix](#w-suggested-team-responsibility-matrix)

---

## A. What the Project Is

**Title:** Trust-Aware Service Selection for Autonomous AI Agents  
**Subtitle:** An Evidence-Based Trust and Verification Framework

It is a software and research framework that gives autonomous AI agents a brain for **choosing external services safely**. When an AI agent needs to delegate a task to an outside service (like a code runner, a math calculator, or a database query tool), our framework evaluates candidate services using **verified, task-specific past performance** rather than just trusting star ratings or self-advertisements.

---

## B. Why We Made It

AI agents are no longer working alone. In modern architectures, an "orchestrator" agent breaks down a big goal and delegates pieces to external third-party tools. But in an open, decentralized internet of agents, **you have no idea who is on the other end**. An external agent might be slow, broken, or actively malicious (trying to inject prompt exploits or steal data). We built this to give agents a disciplined, automated security and trust gatekeeper.

---

## C. The Problem

1. **Unverifiable Claims:** External services put up "Agent Cards" claiming they are 99% accurate, but talk is cheap.
2. **Fake Star Ratings (Sybil Attacks):** An attacker can create 500 fake bot accounts and give their own malicious service 5-star ratings. In real decentralized registries (ERC-8004), research shows up to **90.6% of reviewers are coordinated Sybils**!
3. **The Halo Effect (Domain Mismatch):** A service might have a 5-star rating because it’s great at translating Spanish, but if you assign it a Python code execution task, it might completely fail. General reputation doesn’t tell you if an agent is good at *this specific task*.
4. **Behavioral Drift:** An agent that worked yesterday might be degraded or compromised today.

---

## D. The Research Gap

Existing solutions fall into two bad extremes:
- **Centralized Whitelists (like Apple App Store):** Safe, but destroys decentralization and cannot scale to millions of autonomous micro-agents.
- **On-Chain Reputation (like ERC-8004):** Open and decentralized, but totally vulnerable to Sybil collusion and completely blind to task context.

**Our Gap:** Nobody had built a controlled framework that evaluates external agents using **semantic task-specific verified interaction evidence** combined with **risk-calibrated confidence gates**.

---

## E. The Research Question

> **“Can task-specific, verifiable evidence improve autonomous AI-agent service selection compared with reputation-only scoring?”**

---

## F. The Objectives

1. Formulate a multi-dimensional trust model (Identity, Capability, Task History, Evidence Quality, Reputation, Risk).
2. Build a clean 10-component system architecture with strict boundaries.
3. Build a reproducible simulation testbed with 30 agents (20 Reliable, 5 Unreliable, 5 Malicious).
4. Run controlled experiments comparing Random Selection, Reputation-Only Selection, and Evidence-Based Selection.
5. Quantify trade-offs across 5 core metrics (Success Rate, Malicious Selection, False Rejection, Latency, and Verification Cost).

---

## G. How the System Works (End-to-End)

Follow this 8-step story:
1. **Task Ingestion:** The client agent gets a task and determines the domain and risk level (Low, Medium, or High Stakes).
2. **Discovery:** Finds candidate agents that claim they can handle the task.
3. **Evidence Retrieval (RAG):** Looks into its evidence database using vector search to find past interactions with these candidates *in this specific task domain*.
4. **Trust Assessment:** Evaluates past verified success rates, discounts global reputation, and checks evidence freshness.
5. **Selection Decision:** If a candidate passes the risk threshold, select it. If none are trustworthy enough, **safely reject** to avoid harm!
6. **Execution (MCP):** Sends the task parameters via standardized Model Context Protocol tools.
7. **Result Verification:** The output is tested in a sandbox (unit tests, math checks, schema validation).
8. **Evidence Update:** The verification result is stored in the local database and a cryptographic fingerprint is anchored to the blockchain for tamper-evidence.

---

## H. What Each Architecture Component Does

1. **Autonomous Client Agent:** The boss/orchestrator coordinating the workflow.
2. **Discovery Layer:** Searches the directory for matching services.
3. **Candidate Store:** Temporary memory holding candidate metadata.
4. **Evidence Store:** Local database (SQLite/DuckDB) holding verified interaction history.
5. **Trust Evaluation Engine:** The math brain calculating trust scores.
6. **Risk Assessment Layer:** Sets how strict the trust threshold must be based on task stakes.
7. **Selection Engine:** Ranks candidates and picks the winner.
8. **Task Execution Layer:** Sends the request over the wire using MCP.
9. **Result Verification Layer:** Tests the returned output to see if it actually works.
10. **Evidence Update Layer:** Records the outcome and hashes it for blockchain provenance.

---

## I. What RAG Does (And What It Doesn't Do)

- **What RAG Does:** RAG (Retrieval-Augmented Generation) uses vector embeddings to search through thousands of historical interaction logs and pull out only the ones that match *the current task's domain*.
- **What RAG Does NOT Do:** RAG does *not* magically make evidence true. If a stored record was faked, RAG will still retrieve it. Verification is what guarantees truth.

---

## J. What MCP Does (And What It Doesn't Do)

- **What MCP Does:** Model Context Protocol (Anthropic standard) provides a standard language and JSON-RPC format for agents to call external tools.
- **What MCP Does NOT Do:** MCP provides **zero trust or security**. It's just a communication cable. Calling a bad agent over MCP will still get you poisoned data.

---

## K. What Blockchain Does (And What It Doesn't Do)

- **What Blockchain Does:** It acts as a tamper-evident audit log. We batch hashes of interaction logs into a Merkle root and store the 32-byte root on-chain. This proves that past logs haven't been secretly edited or deleted.
- **What Blockchain Does NOT Do:** Blockchain does *not* make bad data good. Putting a bad result on a blockchain just makes it permanently recorded bad data. Also, we **do NOT store full logs on-chain** (too expensive and leaks privacy).

---

## L. Why Reputation Alone Is Not Enough

Because global reputation is just an average star rating:
1. It is easily faked by cheap Sybil bots.
2. It suffers from the **Halo Effect**: being good at text writing doesn't mean you're good at executing Python scripts.
3. It measures *popularity*, not *verified correctness*.

---

## M. What Evidence Means in This Framework

Evidence is **concrete, empirical data from past executions**:
- What was the task input?
- What was the service's returned output?
- How many milliseconds did it take?
- Did it pass deterministic unit tests?
- Who verified it, and what is the cryptographic hash?

---

## N. What Verification Means in This Framework

Verification is **testing the output before you trust it**:
- If it's code: run unit tests in an isolated sandbox.
- If it's math: check against an exact math solver.
- If it's data: validate JSON schema and field constraints.
- If it's open-ended: run a consensus check across multiple agents.

---

## O. What the Experiment Is

We built a controlled simulation to compare three strategies across **100 deterministic tasks**:
- **Strategy 1 (Random Selection):** Picks any candidate at random (Null Baseline).
- **Strategy 2 (Reputation-Only Selection):** Picks whoever has the highest star rating (ERC-8004 Baseline).
- **Strategy 3 (Evidence-Based Selection):** Our proposed framework using task-specific evidence and risk gates.

---

## P. Why 30 Agents?

30 agents is a standard, manageable synthetic population size for research prototypes. It provides enough diversity to test competition and collusion while remaining fast to simulate and analyze. Future work will scale to 100 and 1,000 agents.

---

## Q. Why 20 Reliable, 5 Unreliable, 5 Malicious?

- **20 Reliable (66.7%):** Represents an open market where the majority of services intend to work normally.
- **5 Unreliable (16.7%):** Represents real-world infrastructure issues (cloud timeouts, high latency, random server errors).
- **5 Malicious (16.7%):** Represents adversaries trying to game the system with Sybil rating rings and poisoned outputs on high-stakes tasks.

This distribution matches standard Byzantine fault tolerance and security research models.

---

## R. Why These Three Selection Strategies?

- You need **Random** to know what happens if you do nothing.
- You need **Reputation-Only** to test how current industry standards (like ERC-8004) hold up against Sybil attacks.
- You need **Evidence-Based** to prove whether our proposed approach actually makes a difference.

---

## S. What Each Evaluation Metric Means

1. **Task Success Rate ($TSR$):** Did the task get completed correctly? (Higher is better).
2. **Malicious-Agent Selection Rate ($MASR$):** How often did the system accidentally pick a bad guy? (Lower is better).
3. **False Rejection Rate ($FRR$):** How often did the system reject a good agent because it was being too paranoid? (Lower is better).
4. **Verification Cost Overhead ($VCO$):** How much time and CPU did we spend testing outputs? (Lower is better).
5. **Selection Decision Latency ($SDL$):** How many milliseconds did the agent spend thinking and searching before picking? (Lower is better).

---

## T. What We Can Legally and Scientifically Claim

- We CAN claim that empirical research (Xiong et al. 2026) proves existing decentralized registries suffer from 59–90% Sybil manipulation.
- We CAN claim we designed a formal multi-dimensional trust framework integrating task-specific evidence, RAG retrieval, and verification feedback.
- We CAN claim our simulation testbed is fully designed, seed-controlled, and ready for reproducible benchmarking.

---

## U. What We CANNOT Claim (Never Say This!)

- **NEVER SAY:** "Our framework is 100% accurate" or "We achieve 99% success rate" (we haven't run the physical benchmark yet!).
- **NEVER SAY:** "We are the first to combine blockchain and AI" (hyperbolic and untrue).
- **NEVER SAY:** "Blockchain verifies the AI output" (blockchain only stores hashes; our verification layer checks the output).
- **NEVER SAY:** "We implemented autonomous crypto payments" (x402 is future work).

If asked for numbers, always say:
> *"Our experimental framework and data schemas are fully specified and ready to execute. We do not report synthetic or fabricated numbers; we will publish empirical figures once reproducible multi-seed runs are completed."*

---

## V. Future Work & Extensions

1. **x402 Micropayments:** Programmatic escrow release conditional on verified execution.
2. **Zero-Knowledge Machine Learning (zkML):** Cryptographic execution proofs as zkML provers become faster.
3. **Cross-Fleet Collaborative Evidence:** Secure sharing of encrypted interaction evidence across different client agent companies.

---

## W. Suggested Team Responsibility Matrix

| Team Role | Primary Responsibility | Best Person To Answer |
|---|---|---|
| **Research Lead** | Problem statement, research question, literature review, ERC-8004 findings | "Why did you choose this problem?" & "What is novel?" |
| **System Architect** | 10 components, sequence diagrams, data flow, trust boundaries | "How does the system work?" & "Walk me through the architecture." |
| **AI / RAG Engineer** | Vector embeddings, semantic domain matching, retrieval thresholds | "How does RAG help trust?" & "How do you avoid hallucinations?" |
| **Security & Blockchain** | Threat modeling (14 threats), Merkle trees, Sybil defense, MCP tools | "How do you prevent Sybil attacks?" & "Why use blockchain?" |
| **Experimentation Lead** | 30 agents (20/5/5), 3 strategies, 5 metrics, seed control, statistical plan | "How is the experiment set up?" & "What do your metrics measure?" |
