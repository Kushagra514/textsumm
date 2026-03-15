import typer
from rich.console import Console
from rich.table import Table
from collections import Counter
import re
from typing import TypedDict
import structlog


app = typer.Typer()
console = Console()
log=structlog.get_logger()

class TextSummError(Exception):
    """ Base exception for textsumm errors."""
    pass

class EmptyFileError(TextSummError):
    """Raised when the file exists but contains no text."""
    pass

class InvalidFileTypeError(TextSummError):
    """Raised when the file is not a text file."""
    pass

class AnalysisResult(TypedDict):
    word_count: int
    sentence_count: int
    avg_sentence_length: int
    top_words: list[tuple[str, int]]

def analyze(text: str) -> AnalysisResult:
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
def summarize(filepath: str) -> None:
    log.info("starting analysis", filepath=filepath)
    try:
        if not filepath.endswith(".txt"):
            raise InvalidFileTypeError(f"{filepath} is not a .txt file")
        with open(filepath, "r") as f:
            text = f.read()
        log.info("file read successfully",filepath=filepath)

        if not text.strip():
            raise EmptyFileError(f"{filepath} is empty")

    except FileNotFoundError:
        log.error("file not found",filepath=filepath)
        console.print(f"[red]File not found: {filepath}[/red]")
        raise typer.Exit(1)
    except EmptyFileError:
        log.error("empty file",filepath=filepath)
        console.print(f"[red]File not found: {filepath} is empty[/red]")
        raise typer.Exit(1)
    except InvalidFileTypeError:
        log.error("invalid file type",filepath=filepath)
        console.print(f"[red]Error: only .txt files are supported[/red]")
        raise typer.Exit(1)

    stats = analyze(text)
    log.info("analysis complete", word_count=stats["word_count"])

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
