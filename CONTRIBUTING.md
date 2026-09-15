# Contributing to Trust-Aware Service Selection

Thank you for your interest in contributing to this research framework. We welcome academic collaboration, code enhancements, empirical evaluations, and documentation improvements.

## Code of Conduct

All contributors are expected to uphold our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure an inclusive, respectful, and harassment-free environment.

## Research Integrity Standards

Because this is an active scientific research project, all contributors must adhere to strict research integrity guidelines:
1. **Never Fabricate Experimental Data:** Do not commit synthetic benchmark numbers, charts, or evaluation outcomes claiming to represent real experimental results.
2. **Distinguish Existing Evidence from Project Findings:** External empirical findings (such as the ERC-8004 study) must be explicitly cited as **EXISTING RESEARCH EVIDENCE**.
3. **No Unsubstantiated Hype:** Avoid unverified claims such as "revolutionary," "first," or "superior" unless supported by empirical comparisons.
4. **Reproducibility First:** Any proposed algorithm or simulation parameter change must include seed-controlled tests ensuring exact mathematical replicability.

## How to Contribute

### 1. Reporting Bugs & Inconsistencies
- Check existing GitHub issues before filing.
- Use the [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md).
- Include exact steps to reproduce, environment information, and error logs.

### 2. Proposing Research Inquiries & Features
- Use the [Research Inquiry Template](.github/ISSUE_TEMPLATE/research_inquiry.md) or [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.md).
- Clearly explain the theoretical basis, architectural motivation, and potential trade-offs.

### 3. Submitting Pull Requests
1. Fork the repository and create your branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Write clean, modular, and type-annotated Python code matching existing conventions (`src/`).
3. Add or update unit tests under `tests/unit/`.
4. Ensure all tests pass:
   ```bash
   pytest tests/
   ```
5. Update relevant documentation in `docs/` and diagrams in `diagrams/` if your change affects system architecture or data schemas.
6. Submit a pull request following the [Pull Request Template](.github/pull_request_template.md).

## Development Setup

```bash
# Clone your fork
git clone https://github.com/<your-username>/trust-aware-agent-service-selection.git
cd trust-aware-agent-service-selection

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Or .\venv\Scripts\activate on Windows

# Install dependencies in editable mode
pip install -r requirements.txt
```

## Review Process

- All PRs require review from a maintainer before merge.
- Linting and unit test suites must pass cleanly.
