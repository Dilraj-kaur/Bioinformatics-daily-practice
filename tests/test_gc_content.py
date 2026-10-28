
import pytest

from python.sequencing.gc_content import calculate_gc_content


def test_gc_content():
    assert calculate_gc_content("ATGC") == 50.0


def test_all_gc():
    assert calculate_gc_content("GGCC") == 100.0


def test_no_gc():
    assert calculate_gc_content("ATAT") == 0.0


def test_lowercase_sequence():
    assert calculate_gc_content("atgc") == 50.0


def test_empty_sequence():
    with pytest.raises(ValueError):
        calculate_gc_content("")


def test_invalid_sequence():
    with pytest.raises(ValueError):
        calculate_gc_content("ATGX")

