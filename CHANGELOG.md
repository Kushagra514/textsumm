# Changelog

All notable changes to textsumm will be documented here.

## [0.2.0] - 2025-03-24

### Added
- GitHub Actions CI — auto runs pytest, mypy, ruff on every push and PR
- Published to TestPyPI as textsumm-kushagra v0.2.0
- Semantic versioning with semver
- GitHub profile README


## [0.1.0] - 2025-01-01

### Added
- Core CLI tool — word count, sentence count, avg sentence length, word density, top 5 words
- Poetry setup with pyproject.toml and dependency groups
- Type hints with strict mypy
- Structured logging with structlog
- Custom exception hierarchy — TextSummError, EmptyFileError, InvalidFileTypeError
- pytest suite with 97% coverage
- Pre-commit hooks — black, ruff, mypy
- Makefile with make check command
- Bash scripts — analyse.sh and run_checks.sh