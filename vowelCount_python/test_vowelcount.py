import pytest
from vowelcount import vowelcount
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('x, check', [
    ("Suma", 2),
    ("Taehyung", 3),
    ("Jungkook", 3),
    ("Namjoon", 3),
    ("Suga", 2),
    ("J-Hope", 2),
    ("Jin", 1),
    ("Jimin", 2),
    ("BTS",0)

    
])
def test_vowelcount(x, check):
    assert vowelcount(x) == check