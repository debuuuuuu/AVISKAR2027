# 2-Minute Presentation & Persona-Tailored Explanations

---

## 1. The Standard 2-Minute Script (Timed for ~2 Minutes)

"Good morning/afternoon, judges and colleagues.

Today, AI agents are evolving from single chatbots into complex multi-agent workflows. An orchestrator agent breaks down a problem and delegates subtasks to external service agents—whether for running Python code, querying databases, or solving math proofs.

However, when an agent selects an external service in an open marketplace, it faces deep uncertainty. Recent empirical research on decentralized agent registries like ERC-8004 revealed that over 85% of registered agents have broken endpoints, and up to 90.6% of reviewers engage in coordinated Sybil collusion to artificially pump 5-star ratings. Even worse, global star ratings suffer from the 'Halo Effect': an agent that is great at text summarization might completely fail or inject backdoors when assigned mathematical optimization.

Our central research question is: **'Can task-specific, verifiable evidence improve autonomous AI-agent service selection compared with reputation-only scoring?'**

To answer this, we built a trust and verification framework based on six dimensions: **Identity, Capability, Task-Specific History, Evidence Quality, Reputation, and Risk**.

Here is how our system works:
1. When a task arrives, the client agent extracts the domain and assesses the risk stakes.
2. Using RAG, it retrieves historical interaction records specific to that exact task domain.
3. It evaluates candidate trust against a risk-calibrated confidence threshold, discounting public reputation to protect against Sybil inflation. If no candidate passes the threshold on a high-stakes task, it safely rejects execution to prevent catastrophic harm.
4. When a selected service executes, our Result Verification Layer tests the output in an isolated sandbox.
5. The verified result updates our local evidence store, and a cryptographic state commitment is anchored to the blockchain for tamper-evident provenance.

We evaluate this using a controlled simulation of 30 agents—20 reliable, 5 unreliable, and 5 malicious—comparing our Evidence-Based approach against Random Selection and Reputation-Only baselines across 5 key metrics: Task Success Rate, Malicious Selection Rate, False Rejection Rate, Verification Cost, and Decision Latency.

Thank you, and we welcome your questions."

---

## 2. Persona-Tailored Explanations

### Persona A: "Explain This Project to a Professor"
> *"Our project addresses the decision problem of service selection under uncertainty in open multi-agent systems. We challenge the prevailing assumption in decentralized registries (like ERC-8004) that scalar reputation is an adequate signal for delegation. Drawing from subjective logic and Bayesian decision theory, we formalize a multi-dimensional trust framework where task domain semantics modulate the epistemic weight of historical interaction evidence. We evaluate this via a controlled 30-agent simulation comparing our evidence-grounded approach against reputation-only and null baselines across five formalized operational metrics."*

### Persona B: "Explain This Project to a Non-Technical Judge"
> *"Imagine you need to hire a contractor to rewire your house's electrical system. If you just look at online star ratings, you might hire someone with five stars who got those ratings from writing product reviews or having their friends post fake feedback. You want to see their actual electrical license and verified evidence of past electrical work. Our framework does this for AI agents: instead of trusting fake internet ratings, the AI checks verified past work for that exact job before hiring an external service."*

### Persona C: "Explain This Project to an AI Researcher"
> *"In multi-agent architectures, orchestrators routinely invoke external tools. Current systems like Toolformer or standard MCP assume tools are benign, static functions. We model the adversarial reality: unvetted external agents exhibiting performance drift, prompt injection, and collusive reputation laundering. We use dense vector embeddings of task specifications to perform RAG over historical execution traces, allowing the agent to evaluate expected success specifically conditioned on task domain semantics and objective failure stakes."*

### Persona D: "Explain This Project to a Software Engineer"
> *"Think of this as a secure, risk-aware service mesh and circuit-breaker for LLM tool invocation. We sit between the client agent and external MCP service endpoints. Before making a remote RPC call, we query a local SQLite/vector store for past execution telemetry matching the schema. We calculate a risk-gated confidence score, enforce timeouts, sandbox the returned payload with unit tests, and anchor SHA-256 Merkle roots to an EVM contract for immutable auditing. If an endpoint fails or poisons data, our feedback loop immediately penalizes its selection priority."*
