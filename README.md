# textsumm

A fast, lightweight CLI tool that summarizes any text file in seconds.
Get word count, sentence count, average sentence length, and the top 5 most frequent words — all in a clean formatted table.

## Features

- Word count
- Sentence count
- Average sentence length
- Top 5 most frequent words
- Clean rich table output in your terminal
- Structured logging for every operation
- Meaningful error messages for empty files and wrong file types

## Installation
```bash
pip install textsumm-kushagra
```

## Usage
```bash
textsumm path/to/your/file.txt
```

### Example
```bash
textsumm report.txt
```

### Output
```
2026-03-15 11:44:22 [info] starting analysis filepath=report.txt
2026-03-15 11:44:22 [info] file read successfully filepath=report.txt
2026-03-15 11:44:22 [info] analysis complete word_count=120

               Text Summary
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Metric              ┃ Value             ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ Words               │ 120               │
│ Sentences           │ 10                │
│ Avg sentence length │ 12 words          │
│ Top word #1         │ are (7x)          │
│ Top word #2         │ the (6x)          │
│ Top word #3         │ that (4x)         │
│ Top word #4         │ intelligence (3x) │
│ Top word #5         │ and (3x)          │
└─────────────────────┴───────────────────┘
```

## Error Handling
```bash
# Empty file
textsumm empty.txt
Error: empty.txt is empty

# Wrong file type
textsumm document.pdf
Error: only .txt files are supported

# File not found
textsumm missing.txt
File not found: missing.txt
```

## Development Setup

Clone the repo and install dependencies:
```bash
git clone https://github.com/Kushagra514/textsumm
cd textsumm
poetry install
```

Run the tool locally:
```bash
poetry run textsumm path/to/file.txt
```

Run tests:
```bash
poetry run pytest tests/ -v
```

Run tests with coverage:
```bash
poetry run pytest tests/ --cov=src/textsumm --cov-report=term-missing
```

Format and lint:
```bash
poetry run black src/
poetry run ruff check src/
```

Type check:
```bash
poetry run mypy src/ --strict
```

## Project Structure
```
textsumm/
├── src/
│   └── textsumm/
│       ├── __init__.py
│       └── main.py        # CLI entry point, core logic, custom exceptions
├── tests/
│   ├── __init__.py
│   └── test_main.py       # pytest test suite (97% coverage)
├── pyproject.toml         # project config and dependencies
├── poetry.lock            # locked dependency versions
└── README.md
```

## Dependencies

| Package | Purpose |
|---------|---------|
| typer | CLI framework |
| rich | Terminal formatting |
| structlog | Structured logging |

## License

MIT