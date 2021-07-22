import pytest
from additiveprime import isAdditivePrime
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('x, check', [
    (2,  True),
    (3, True),
    (5,  True),
    (7, True),
    (11, True),
    (98, False),
    (123, False),
    (111, False),
    (23, True)
])
def test_additiveprime(x, check):
    assert isAdditivePrime(x) == check