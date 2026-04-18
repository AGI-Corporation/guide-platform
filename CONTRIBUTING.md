# Contributing to G.U.I.D.E. Platform

Thank you for your interest in contributing to the G.U.I.D.E. (Guided Understanding and Intelligent Decision Engine) Platform. By participating, you are helping build ethical, human-centered AI for the benefit of customers and communities worldwide.

## Code of Conduct

All contributors must adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

## How to Contribute

### Reporting Bugs
1. Search existing [Issues](https://github.com/AGI-Corporation/guide-platform/issues) to avoid duplicates.
2. Open a new issue with the `bug` label.
3. Include: steps to reproduce, expected behavior, actual behavior, and environment details.

### Suggesting Features
1. Open an issue with the `enhancement` label.
2. Describe the feature, its motivation, and how it aligns with HCAI principles.
3. Reference the relevant [Wiki](https://github.com/AGI-Corporation/guide-platform/wiki) section if applicable.

### Submitting Pull Requests
1. Fork the repository and create a branch: `git checkout -b feature/your-feature-name`
2. Follow the coding standards below.
3. Ensure all tests pass: `pytest tests/`
4. Submit a PR against the `main` branch with a clear description.
5. Link any related issues using `Closes #<issue-number>`.

## Development Setup

```bash
# Clone the repository
git clone https://github.com/AGI-Corporation/guide-platform.git
cd guide-platform

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Start local development server
uvicorn src.main:app --reload
```

## Coding Standards

- **Language:** Python 3.11+ (backend), TypeScript 5+ (frontend)
- **Style:** PEP 8 for Python; ESLint + Prettier for TypeScript
- **Type Hints:** Required for all Python functions
- **Docstrings:** Google-style docstrings for all public functions
- **Tests:** Minimum 80% code coverage for new features
- **Commits:** Follow [Conventional Commits](https://www.conventionalcommits.org/) format

## Ethical Contribution Guidelines

All contributions must align with the G.U.I.D.E. Platform's HCAI principles:

- **Maintain Agency:** Do not introduce changes that reduce human oversight.
- **Transparency:** All AI decision paths must remain explainable.
- **Bias Mitigation:** New features must include bias impact assessment.
- **Digital Stewardship:** Consider privacy and data ethics in every PR.

## Review Process

PRs are reviewed within 5 business days. Reviewers will check:
1. Code quality and test coverage
2. HCAI ethical alignment
3. Documentation completeness
4. Performance impact

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
