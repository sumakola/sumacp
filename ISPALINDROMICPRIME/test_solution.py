import pytest
from ispalindromicprime import ispalindromicprime
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('x, check', [
    (11, True),
    (101,  True),
    (131, True),
    (181, True),
    (23, False),
    (29, False)
])
def test_solution(x, check):
    assert ispalindromicprime(x) == check