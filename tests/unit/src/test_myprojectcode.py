import pytest

from src.myprojectcode import is_even


@pytest.mark.parametrize(
    "n, even",
    [
        (0, True),
        (1, False),
        (2, True),
        (3, False),
        (4, True),
        (5, False),
        (25, False),
        (125, False),
        (1000, True),
        (10520, True),
        (33333, False),
        (312333, False),
        (4554323, False),
        (21235444, True),
        (1244442123, False),
    ],
)
def test_is_even(n: int, even: bool) -> None:
    # pytest tests/unit/src/test_myprojectcode.py::test_is_even --disable-pytest-warnings

    assert is_even(n) == even


# pytest tests/unit/src/test_myprojectcode.py --disable-pytest-warnings
