from yahtzee_game import Checks
from yahtzee_game import Score
import pytest

def test_checks():
    ''' this will test all the checks inside the Checks class'''
    c = Checks()
    assert c.ones([1,1,2,3,4]) == 2
    assert c.ones([2,2,2,2,2]) == 0
    assert c.twos([1,2,2,2,3]) == 6
    assert c.twos([1,1,1,1,1]) == 0
    assert c.threes([1,2,3,3,3]) == 9
    assert c.threes([2,2,2,2,2]) == 0
    assert c.fours([4,4,4,4,1]) == 16
    assert c.fours([2,2,2,2,2]) == 0
    assert c.fives([1,5,5,5,1]) == 15
    assert c.fives([2,2,2,2,2]) == 0
    assert c.sixes([1,6,1,6,1]) == 12
    assert c.sixes([2,2,2,2,2]) == 0
    assert c.three_of_a_kind([1,1,1,2,3]) == 8
    assert c.three_of_a_kind([1,2,3,1,2]) == 0
    assert c.four_of_a_kind([1,4,4,4,4]) == 17
    assert c.four_of_a_kind([1,3,2,6,1]) == 0
    assert c.smallstraight([1,2,3,4,6]) == 16
    assert c.smallstraight([1,1,1,3,3]) == 0
    assert c.largestraight([2,3,4,5,6]) == 40
    assert c.full_house([1,1,1,5,5]) == 25
    assert c.full_house([1,2,3,4,5]) == 0
    assert c.chance([6,6,6,6,6]) == 30
    assert c.chance([1,1,2,6,3]) == 13
    assert c.Yahtzee([3,3,3,3,3]) == 50
    assert c.Yahtzee([1,3,2,1,6]) == 0

def test_score():
    ''' this will test all the scoring inside the Score class'''
    s = Score()
    assert s.add_upper_score(3, 6, 9, 12, 15, 18) == 63
    assert s.add_upper_score(0,0,0,0,0,0) == 0
    assert s.add_upper_bonus(63) == 35
    assert s.add_upper_bonus(62) == 0
    assert s.add_upper_bonus(0) == 0
    assert s.add_upper_bonus(160) == 35
    assert s.get_upper_score(50, 0) == 50
    assert s.get_upper_score(64, 35) == 99