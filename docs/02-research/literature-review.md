# Literature Review: Trust, Reputation, and Verification in Multi-Agent Systems

This literature review analyzes foundational and recent academic research across multi-agent reputation systems, decentralized AI ecosystems, verifiable computation, and agent tool invocation.

---

## 1. Decentralized AI Agent Registries & Empirical Trust

### Paper 1: The Empirical Fragility of Decentralized Agent Registries
- **Title:** *Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem*
- **Authors:** Xihan Xiong, Zelin Li, Wei Wei, Qin Wang, William J. Knottenbelt, Z. Wang
- **Year & Source:** 2026, arXiv:2606.26028 [cs.CR]
- **Research Problem:** Whether decentralized agent standards (specifically ERC-8004) deliver trustless, reliable agent discovery and reputation in practice.
- **Methodology:** Complete longitudinal on-chain analysis and active network probing across Ethereum, BNB Smart Chain, and Base.
- **Key Findings:** Only 3% to 15% of registered agents expose reachable, functional service endpoints. Coordinated Sybil reviewers represent 59.2% to 90.6% of feedback activity, leading to complete reputation collapse upon Sybil filtering.
- **Relevance to Our Project:** Directly motivates our core problem statement. Proves empirically that on-chain star ratings cannot be relied upon by autonomous agents.
- **Limitation of the Paper:** Analyzed existing registry failures but did not propose an algorithmic selection decision framework to mitigate them.
- **How Our Project Differs:** We formulate an evidence-based trust evaluation and verification feedback framework specifically designed to protect client agents from selecting such non-functional or Sybil-manipulated services.

---

## 2. Multi-Agent Reputation Models

### Paper 2: The REGRET Multi-Agent Reputation Model
- **Title:** *REGRET: A reputation model for multi-agent systems*
- **Authors:** Jordi Sabater, Carles Sierra
- **Year & Source:** 2002, *Autonomous Agents and Multi-Agent Systems*, 5(1), 33–55
- **Research Problem:** How autonomous agents can evaluate peer reliability using direct interaction history, witness information, and system role reputation.
- **Methodology:** Formal graph-theoretic and statistical modeling of direct, witness, and neighborhood reputation with recency weighting.
- **Key Findings:** Decoupling direct experience from witness reports prevents single-source deception; time-decay functions are essential to track changing agent reliability.
- **Relevance to Our Project:** Provides theoretical foundations for separating direct evidence from third-party reputation.
- **Limitation:** Developed for simple e-commerce software agents; does not address modern LLM agents, semantic task domain matching, or Sybil collusion in permissionless networks.
- **How Our Project Differs:** We integrate semantic task similarity (via vector embeddings / RAG), explicit risk constraints, and post-execution verification feedback.

### Paper 3: The Beta Reputation System
- **Title:** *The Beta Reputation System*
- **Authors:** Audun Jøsang, Roslan Ismail
- **Year & Source:** 2002, *Proceedings of the 15th Bled Electronic Commerce Conference*
- **Research Problem:** Formulating a mathematically rigorous trust calculation based on Bayesian probability distributions.
- **Methodology:** Beta probability density functions $(\alpha, \beta)$ tracking binary positive/negative outcomes to calculate expectation values and certainty.
- **Key Findings:** The Beta distribution provides a clean mathematical foundation for updating trust dynamically while explicitly quantifying uncertainty based on sample size.
- **Relevance to Our Project:** Informs our evidence quality model, where sample size and observation confidence modulate the trust gate.
- **Limitation:** Assumes independent, identically distributed binary outcomes across all tasks; blind to task complexity or domain shifts.
- **How Our Project Differs:** Our trust model conditions the Beta prior on semantic task domain vectors, preventing successful simple tasks from validating complex or high-risk tasks.

---

## 3. Multi-Agent Trust Management Surveys

### Paper 4: Multi-Agent Trust Management Survey
- **Title:** *A Survey of Multi-Agent Trust Management Systems*
- **Authors:** Han Yu, Zhiqi Shen, Chunyan Miao, Cyril Leung, Dusit Niyato
- **Year & Source:** 2013, *IEEE Access*, 1, 35–50
- **Research Problem:** Comprehensive taxonomy of computational trust models across decentralized, distributed, and peer-to-peer agent networks.
- **Methodology:** Systematic taxonomic review analyzing direct trust, witness trust, security threats (Sybil, collusive inflation, whitewashing), and defense mechanisms.
- **Key Findings:** Trust models that fail to incorporate context and task specificity invariably suffer from vulnerability to domain-shift exploitation.
- **Relevance to Our Project:** Highlights that task context and risk level are essential dimensions of any robust trust decision.
- **Limitation:** Pre-dates modern generative AI agents, neural embeddings, and foundation model tool use.
- **How Our Project Differs:** Applies multi-agent trust principles specifically to modern autonomous LLM-agent tool selection and execution workflows.

---

## 4. Autonomous Agent Tool Selection & Interoperability

### Paper 5: Tool-Augmented Language Agents
- **Title:** *Toolformer: Language Models Can Teach Themselves to Use Tools*
- **Authors:** Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom
- **Year & Source:** 2023, *Advances in Neural Information Processing Systems (NeurIPS 2023)*
- **Research Problem:** Enabling LLMs to determine when and how to invoke external computational tools to enhance reasoning.
- **Methodology:** Self-supervised data generation and fine-tuning on API call generation and response parsing.
- **Key Findings:** External tool invocation drastically improves performance on mathematical, temporal, and retrieval tasks.
- **Limitation:** Assumes all external tools are benign, static, local APIs; provides zero trust evaluation, adversary mitigation, or verification logic.
- **How Our Project Differs:** We focus on the adversarial, open multi-agent environment where external tools are hosted by unvetted third parties who may fail or behave maliciously.

### Specification 6: Model Context Protocol (MCP)
- **Title:** *Model Context Protocol Specification*
- **Authors:** Anthropic
- **Year & Source:** 2024, https://modelcontextprotocol.io
- **Technical Contribution:** Standardized JSON-RPC protocol defining Client-Host-Server architecture for tool discovery, resource provision, and sampling.
- **Relevance to Our Project:** Used as the standardized protocol layer connecting client agents to candidate service endpoints.
- **Limitation:** MCP is purely a communication standard; it does not implement security verification, trust evaluation, or reputation mechanisms.
- **How Our Project Differs:** We build the trust and verification intelligence layer that sits on top of MCP tool calls.

---

## 5. Comparative Synthesis Matrix

| Literature Stream | Primary Strengths | Identified Gap | Our Framework's Contribution |
|---|---|---|---|
| **Decentralized Registries (ERC-8004)** | Open discovery, decentralized identity on EVM. | High Sybil collusion, 85-97% endpoint unreachability, ungrounded feedback. | Grounding selection on verifiable task evidence; treating on-chain feedback as an untrusted prior. |
| **Classical Multi-Agent Trust (REGRET, Beta)** | Rigorous Bayesian statistics and recency weighting. | Blind to semantic task domains; designed for simple static e-commerce agents. | Embedding-based semantic task filtering (RAG) and multidimensional risk-gated decision boundaries. |
| **LLM Tool Selection (Toolformer, MCP)** | Standardized tool invocation protocols. | Completely assumes benevolent, reliable tool providers; zero security/trust modeling. | Threat modeling 14 adversarial vectors; implementing post-execution verification and feedback. |
