from ambio import match


def test_naive_match():
    assert match.naiveExactMatch("aa", "abcdefèoaadifha") == 8
    assert match.naiveExactMatch("abc", "abcdefgh") == 0
    assert match.naiveExactMatch("fgh", "abcdefgh") == 5
    assert match.naiveExactMatch("aa", "auiosdhfèodfh") == -1
    assert match.naiveExactMatch("", "audhsf") == -1
    assert match.naiveExactMatch("fj", "") == -1
    assert match.naiveExactMatch("", "") == -1
