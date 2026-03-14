import typer
from rich.console import Console
from rich.table import Table
from collections import Counter
import re

app = typer.Typer()
console = Console()


def analyze(text: str) -> dict:
    words = re.findall(r"\b\w+\b", text.lower())
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    word_count = len(words)
    sentence_count = len(sentences)
    avg_length = round(word_count / sentence_count) if sentence_count else 0
    top_words = Counter(words).most_common(5)
    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "avg_sentence_length": avg_length,
        "top_words": top_words,
    }


@app.command()
def summarize(filepath: str):
    try:
        with open(filepath, "r") as f:
            text = f.read()
    except FileNotFoundError:
        console.print(f"[red]File not found: {filepath}[/red]")
        raise typer.Exit(1)

    stats = analyze(text)

    table = Table(title="Text Summary")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("Words", str(stats["word_count"]))
    table.add_row("Sentences", str(stats["sentence_count"]))
    table.add_row("Avg sentence length", str(stats["avg_sentence_length"]) + " words")
    for i, (word, count) in enumerate(stats["top_words"]):
        table.add_row(f"Top word #{i+1}", f"{word} ({count}x)")

    console.print(table)


if __name__ == "__main__":
    app()
