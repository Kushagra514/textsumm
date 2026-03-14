from textsumm.main import analyze, summarize
from unittest.mock import mock_open, patch
import pytest
import typer

def test_word_count():
    result = analyze("hello world foo")
    assert result["word_count"] == 3

def test_sentence_count():
    result = analyze("Hello world. Foo bar. Baz.")
    assert result["sentence_count"] == 3

def test_avg_sentence_length():
    result = analyze("Hello world. Foo bar baz.")
    assert result["avg_sentence_length"] == 2

def test_top_words():
    result = analyze("the the the cat cat dog")
    assert result["top_words"][0] == ("the", 3)

def test_empty_file():
    result = analyze("")
    assert result["word_count"] == 0
    assert result["avg_sentence_length"] == 0

def test_summarize_reads_file(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("Hello world. Foo bar. Baz.")
    summarize(str(f))

def test_summarize_file_not_found():
    with pytest.raises(Exception):
        summarize("nonexistent_file.txt")