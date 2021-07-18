import pytest
from removeRowAndCol import removeRowAndCol
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('L , row, col, check', [
    ([ [ 2, 3, 4, 5], [ 8, 7, 6, 5], [ 0, 1, 2, 3] ], 1, 2,  [ [ 2, 3, 5], [ 0, 1, 3] ]),
    ([ [ 1,2,3], [7, 6, 5], [ 9, 10, 11] ], 2, 2,  [ [ 1, 2], [ 7, 6] ]),
    ([ [ 1,2], [7, 6] ], 0, 0, None),
    ([1], 0, 0, None)
])
def test_removeRowAndCol(L, row, col, check):
    assert removeRowAndCol(L, row, col) == check