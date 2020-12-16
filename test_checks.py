from group_project import Checks
import pytest

def test_checks():
    ''' this will test all the checks inside the Checks class'''
    c = Checks()
    assert c.ones([1,1,2,3,4]) == 2
    assert c.twos([1,2,2,2,3]) == 6