import pytest

from src.main import primeFactors
from src.main import inputLine
from src.main import printResult


@pytest.fixture
def ints() -> list[int]:
    return [2, 2, 5]


def testPrimeFactors() -> None:
    assert primeFactors(20) == [2, 2, 5]
    assert primeFactors(1) is None
    assert primeFactors(2) == [2]
    assert primeFactors(17) == [17]
    assert primeFactors(60) == [2, 2, 3, 5]
    assert primeFactors(144) == [2, 2, 2, 2, 3, 3]


def testInputLine(ints: list[int]) -> None:
    pass


def testPrintResult(ints: list[int]) -> None:
    pass


if __name__ == "__main__":
    pytest.main()
