import pytest
from ambio import align


def test_hamming():
    with pytest.raises(ValueError):
        align.hammingDistance("abcd", "ef")

    assert align.hammingDistance("abcd", "abcd") == 0
    assert align.hammingDistance("abcd", "abef") == 2
    assert align.hammingDistance("abcd", "efgh") == 4


def test_edit():
    assert align.editDistance("sunday", "saturday") == 3
    assert align.editDistance("abcd", "") == 4
    assert align.editDistance("", "abcd") == 4
    assert align.editDistance("", "") == 0
    assert align.editDistance("abcd", "abcd") == 0
    assert align.editDistance("abcd", "efh") == 4
    assert align.editDistance("abcd", "afh") == 3


def test_lcs():
    assert align.LCS("sunday", "saturday") == "suday"
    assert align.LCS("", "hello") == ""
    assert align.LCS("hello", "") == ""
    assert align.LCS("", "") == ""
    assert align.LCS("sunday", "robot") == ""
    assert align.LCS("hello", "hello") == "hello"
    assert align.LCS("123abc456", "kabck") == "abc"
