import pytest
from removeRowAndCol import removeRowAndCol
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('L , row, col, check', [
    ([ [ 2, 3, 4, 5], [ 8, 7, 6, 5], [ 0, 1, 2, 3] ], 1, 2,  [ [ 2, 3, 5], [ 0, 1, 3] ])
])
def test_removeRowAndCol(L, row, col, check):
    assert removeRowAndCol(L, row, col) == check