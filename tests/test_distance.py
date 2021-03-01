import pytest
from ambio import align


def test_hamming_not_same_length():
    with pytest.raises(ValueError):
        align.hammingDistance("abcd", "ef")


def test_hamming_same():
    assert align.hammingDistance("abcd", "abcd") == 0


def test_hamming_close():
    assert align.hammingDistance("abcd", "abef") == 2


def test_hamming_different():
    assert align.hammingDistance("abcd", "efgh") == 4
