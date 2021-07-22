import pytest
from isadditiveprime import isadditiveprime
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('x, check', [
    (2, True),
    (3,  True),
    (5, True),
    (7,  True),
    (23, True),
    (98, False),
    (111, False),
    (129, False)

    
])
def test_additiveprime(x, check):
    assert isadditiveprime(x) == check