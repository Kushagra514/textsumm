# textsumm

A CLI tool that summarizes text files — word count, sentence count, average sentence length, and top 5 most frequent words.

## Installation
```bash
pip install textsumm
```

## Usage
```bash
textsumm path/to/your/file.txt
```

## Example Output
```
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Metric              ┃ Value             ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ Words               │ 120               │
│ Sentences           │ 10                │
│ Avg sentence length │ 12 words          │
│ Top word #1         │ are (7x)          │
└─────────────────────┴───────────────────┘
```

## Development
```bash
git clone https://github.com/yourusername/textsumm
cd textsumm
poetry install
poetry run pytest tests/ --cov=src/textsumm
```

## License

MIT