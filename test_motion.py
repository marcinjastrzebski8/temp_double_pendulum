import pytest
import numpy as np
from System import System
from Oscillator_class import Oscillator
"""
A set of tests checking if the method motion() of System
calculates the functions f1-f4 properly
Expected values have been computed manually.
"""

pend1 = Oscillator(2,3)
pend2 = Oscillator(5,2)
sample = System(pend1,pend2)
sample.set_initial([1,2,3,4])
sample.motion(sample.Z)
f = sample.f
A1 = sample.A1
A2 = sample.A2
print(f)

@pytest.mark.parametrize("test_input,expected",[("f[0]",-0.0048),("f[1]",0.2039),("f[2]",-176.7339),("f[3]",-90.9048)])

def test_eval(test_input,expected):
    assert abs(eval(test_input) - expected) < 0.0001 