from ambio.EditDistance import EditDistance


def test_calculate_same():
    d = EditDistance("abcd", "abcd")
    assert d.getDistance() == 0


def test_calculate_close():
    d = EditDistance("abcd", "abef")
    assert d.getDistance() == 2


def test_calculate_different():
    d = EditDistance("abcd", "efgh")
    assert d.getDistance() == 4
