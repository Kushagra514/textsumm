# textsumm

A fast, lightweight CLI tool that summarizes any text file in seconds.
Get word count, sentence count, average sentence length, and the top 5 most frequent words — all in a clean formatted table.

## Features

- Word count
- Sentence count
- Average sentence length
- Top 5 most frequent words
- Clean rich table output in your terminal

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

## Project Structure
```
textsumm/
├── src/
│   └── textsumm/
│       ├── __init__.py
│       └── main.py        # CLI entry point and core logic
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

## License

MIT
