import pytest

from src.main import primeFactors

def test_prime_factors():
    assert primeFactors(20) == [2, 2, 5]
    assert primeFactors(1) is None
    assert primeFactors(2) == [2]
    assert primeFactors(17) == [17]
    assert primeFactors(60) == [2, 2, 3, 5]
    assert primeFactors(144) == [2, 2, 2, 2, 3, 3]

if __name__ == "__main__":
    pytest.main()
