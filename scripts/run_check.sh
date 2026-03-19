
#!/bin/bash

echo "Running checks ..."
poetry run black src/
poetry run ruff check src/
poetry run mypy src/ --strict
poetry run pytest tests/ -v