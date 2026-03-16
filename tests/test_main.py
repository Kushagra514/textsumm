from textsumm.main import analyze, summarize
from unittest.mock import mock_open, patch
import pytest


@pytest.fixture
def sample_text() -> str:
    return "Artificial intelligence is transforming the world. Machine learning models are being deployed everywhere. These systems can analyze vast amounts of data."


def test_word_count(sample_text: str) -> None:
    result = analyze(sample_text)
    assert result["word_count"] == 21


def test_sentence_count(sample_text: str) -> None:
    result = analyze(sample_text)
    assert result["sentence_count"] == 3


def test_avg_sentence_length(sample_text: str) -> None:
    result = analyze(sample_text)
    assert result["avg_sentence_length"] == 7


def test_word_density(sample_text: str) -> None:
    result = analyze(sample_text)
    assert result["density"] == 100.0


@pytest.mark.parametrize(
    "text,expected_top_word",
    [
        ("the the the cat cat dog", ("the", 3)),
        ("dog dog cat", ("dog", 2)),
        ("hello hello hello world", ("hello", 3)),
    ],
)
def test_top_words(text: str, expected_top_word: tuple[str, int]) -> None:
    result = analyze(text)
    assert result["top_words"][0] == expected_top_word


def test_empty_file() -> None:
    result = analyze("")
    assert result["word_count"] == 0
    assert result["avg_sentence_length"] == 0


def test_summarize_reads_file() -> None:
    mock_content = "Hello world. Foo bar. Baz."
    with patch("builtins.open", mock_open(read_data=mock_content)):
        summarize("fake_file.txt")


def test_summarize_file_not_found() -> None:
    with pytest.raises(Exception):
        summarize("nonexistent_file.txt")
