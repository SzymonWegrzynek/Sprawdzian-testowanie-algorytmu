import pytest
from _pytest.capture import CaptureFixture
from _pytest.monkeypatch import MonkeyPatch

from src.main import primeFactors, inputLine, printResult


@pytest.fixture
def ints() -> list[int]:
    return [2, 2, 5]


def testPrimeFactors(ints: list[int]) -> None:
    assert primeFactors(ints)


def testPrimeFactors() -> None:
    assert primeFactors(1) is None


def testPrimeFactors() -> None:
    assert primeFactors(2) == [2]


def testPrimeFactors() -> None:
    assert primeFactors(17) == [17]


def testPrimeFactors() -> None:
    assert primeFactors(60) == [2, 2, 3, 5]


def testPrimeFactors() -> None:
    assert primeFactors(144) == [2, 2, 2, 2, 3, 3]


def testInputLineInvalidInput(monkeypatch: MonkeyPatch) -> None:
    userInput = "abc\n"
    monkeypatch.setattr('builtins.input', lambda _: userInput)
    with pytest.raises(ValueError):
        inputLine()


def testPrintResultEmptyList(capsys: CaptureFixture) -> None:
    factors = []
    printResult(factors)
    captured = capsys.readouterr()
    assert captured.out == ""
