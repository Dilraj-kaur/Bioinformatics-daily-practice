
import pytest

from python.sequencing.fasta_parser import parse_fasta


def make_fasta(tmp_path, content):
    """Create a temporary FASTA file for testing."""
    filepath = tmp_path / "example.fasta"
    filepath.write_text(content, encoding="utf-8")
    return filepath


def test_single_sequence(tmp_path):
    path = make_fasta(tmp_path, ">seq1\nATGC\n")
    assert parse_fasta(path) == {"seq1": "ATGC"}


def test_multiline_sequence(tmp_path):
    path = make_fasta(tmp_path, ">seq1\nATGC\nGGCC\n")
    assert parse_fasta(path) == {"seq1": "ATGCGGCC"}


def test_multiple_sequences(tmp_path):
    path = make_fasta(tmp_path, ">seq1\nATGC\n>seq2\nGGCC\n")
    assert parse_fasta(path) == {
        "seq1": "ATGC",
        "seq2": "GGCC",
    }


def test_lowercase_sequence(tmp_path):
    path = make_fasta(tmp_path, ">seq1\natgc\n")
    assert parse_fasta(path) == {"seq1": "ATGC"}


def test_sequence_before_header(tmp_path):
    path = make_fasta(tmp_path, "ATGC\n>seq1\nGGCC\n")
    with pytest.raises(ValueError, match="before FASTA header"):
        parse_fasta(path)


def test_missing_identifier(tmp_path):
    path = make_fasta(tmp_path, ">\nATGC\n")
    with pytest.raises(ValueError, match="no identifier"):
        parse_fasta(path)


def test_duplicate_identifier(tmp_path):
    path = make_fasta(tmp_path, ">seq1\nATGC\n>seq1\nGGCC\n")
    with pytest.raises(ValueError, match="Duplicate"):
        parse_fasta(path)


def test_empty_sequence(tmp_path):
    path = make_fasta(tmp_path, ">seq1\n>seq2\nATGC\n")
    with pytest.raises(ValueError, match="Empty sequence"):
        parse_fasta(path)


def test_invalid_dna_base(tmp_path):
    path = make_fasta(tmp_path, ">seq1\nATGQ\n")
    with pytest.raises(ValueError, match="Invalid DNA bases"):
        parse_fasta(path)

