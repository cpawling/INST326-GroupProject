from group_project import Checks
import pytest

def test_checks():
    ''' this will test all the checks inside the Checks class'''
    c = Checks()
    assert c.ones([1,1,2,3,4]) == 2
    assert c.twos([1,2,2,2,3]) == 6
    assert c.threes([1,2,3,3,3]) == 9
    assert c.fours([4,4,4,4,1]) == 16
    assert c.fives([1,5,5,5,1]) == 15
    assert c.sixes([1,6,1,6,1]) == 12
    