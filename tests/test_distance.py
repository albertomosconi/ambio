import pytest
from ambio.distance import hammingDistance, editDistance, generateEditDistanceTable


def test_hamming_not_same_length():
    with pytest.raises(ValueError):
        hammingDistance("abcd", "ef")


def test_hamming_same():
    assert hammingDistance("abcd", "abcd") == 0


def test_hamming_close():
    assert hammingDistance("abcd", "abef") == 2


def test_hamming_different():
    assert hammingDistance("abcd", "efgh") == 4


def test_edit_empty():
    assert editDistance("abcd", "") == 4


def test_edit_same():
    assert editDistance("abcd", "abcd") == 0


def test_edit_close():
    assert editDistance("abcd", "abe") == 2


def test_edit_different():
    assert editDistance("abcd", "efgh") == 4
