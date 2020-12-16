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
    assert c.three_of_a_kind([1,1,1,2,3]) == 8
    assert c.four_of_a_kind([1,4,4,4,4]) == 17
    assert c.smallstraight([1,2,3,4,6]) == 16
    assert c.largestraight([2,3,4,5,6]) == 40
    assert c.full_house([1,1,1,5,5]) == 25
    assert c.chance([6,6,6,6,6]) == 30
    assert c.Yahtzee([3,3,3,3,3]) == 50
    assert c.Yahtzee([1,3,2,1,6]) == 0
    
    
    