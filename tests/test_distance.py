from ambio.distance import editDistance, generateEditDistanceTable


def test_calculate_same():
    assert editDistance("abcd", "abcd") == 0


def test_calculate_close():
    assert editDistance("abcd", "abef") == 2


def test_calculate_different():
    assert editDistance("abcd", "efgh") == 4
