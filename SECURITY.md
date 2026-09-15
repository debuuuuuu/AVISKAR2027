# Security Policy

## Supported Versions

| Version | Supported | Notes |
|---|---|---|
| `0.1.x` | :white_check_mark: | Active Research & Simulation Specification |
| `< 0.1.0` | :x: | Deprecated initial drafts |

## Reporting a Vulnerability

We take the security and integrity of autonomous agent interactions seriously. If you discover a vulnerability within our trust model, cryptographic commitment logic, or simulation sandbox:

1. **Do NOT file a public GitHub issue.**
2. Email your findings confidentially to the maintainers or repository lead.
3. Include:
   - Detailed description of the vulnerability or threat vector.
   - Proof-of-concept simulation scenario or minimal reproduction script.
   - Assessment of potential impact on client agent decision integrity.
4. We commit to acknowledging receipt within 48 hours and providing a remediation timeline.

## Agent Security & Sandboxing Principles

- **No Arbitrary Code Execution:** The simulated environment isolates service agent execution and forbids arbitrary system shell commands.
- **Strict Verification Boundaries:** Client agents must not assume external tool outputs are trusted prior to passing through the verification layer.
- **Cryptographic Provenance:** Historical interaction records must be hashed and committed to prevent retro-active state poisoning.
