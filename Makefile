test:
	poetry run pytest tests/ -v

lint:
	poetry run ruff check src/

format:
	poetry run black src/

typecheck:
	poetry run mypy src/ --strict

check: format lint typecheck test