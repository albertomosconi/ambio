import pytest
from ambio import algs


def test_hamming_not_same_length():
    with pytest.raises(ValueError):
        algs.hammingDistance("abcd", "ef")


def test_hamming_same():
    assert algs.hammingDistance("abcd", "abcd") == 0


def test_hamming_close():
    assert algs.hammingDistance("abcd", "abef") == 2


def test_hamming_different():
    assert algs.hammingDistance("abcd", "efgh") == 4
