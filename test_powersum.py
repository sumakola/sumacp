import pytest
from powersum import powersum
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('n', 'k', 'check' [
    (3, 4, 98),
    (2, -1, 0),
    (1, 0, 1),
    (2, 6, 65),
    (0, 5, 0)
])
def test_powersum(n, k, check):
    assert powersum(n, k) == check
