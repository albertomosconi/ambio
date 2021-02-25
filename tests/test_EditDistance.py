from ambio.EditDistance import EditDistance


def test_calculate_same():
    d = EditDistance("abcd", "abcd")
    assert d.calculate() == 0


def test_calculate_close():
    d = EditDistance("abcd", "abef")
    assert d.calculate() == 2


def test_calculate_different():
    d = EditDistance("abcd", "efgh")
    assert d.calculate() == 4
