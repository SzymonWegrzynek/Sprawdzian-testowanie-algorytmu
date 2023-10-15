import os

import pytest

from src.main import czynnikiPierwsze


def testCzynnikiPierwsze():
    assert czynnikiPierwsze(20) == [2, 2, 5]
    assert czynnikiPierwsze(1) == "return"
    assert czynnikiPierwsze(2) == [2]
    assert czynnikiPierwsze(17) == [17]
    assert czynnikiPierwsze(60) == [2, 2, 3, 5]
    assert czynnikiPierwsze(144) == [2, 2, 2, 2, 3, 3]
