import pytest
from my_app_testing.calculations import fyb


@pytest.mark.parametrize("i,e", [
    (fyb(5), [0, 1, 1, 2, 3]),
    (fyb(3), [0, 1, 1])])
def test_eval(i, e):
    assert i == e