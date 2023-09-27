import pytest
import numpy as np
from System import System
from Oscillator_class import Oscillator
"""
A simple set of tests checking if different elements of 
the system can be accessed properly
"""

pend1 = Oscillator(1,1)
pend2 = Oscillator(2,2)
sample = System(pend1,pend2)
sample.set_initial([1,2,3,4])

@pytest.mark.parametrize("test_input,expected",[("sample.first.mass",1),("sample.first.length",1),("sample.second.mass",2),("sample.second.length",2),
("sample.Z",[1,2,3,4])])

def test_eval(test_input, expected):
    assert eval(test_input) == expected