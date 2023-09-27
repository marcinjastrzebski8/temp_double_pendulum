import pytest
from Oscillator_class import Oscillator
from System import System
import numpy as np
import math

"""
Check if hamiltonian is being calculated properly.
Expected value was calculated manually.
"""

pend1 = Oscillator(2,3)
pend2 = Oscillator(5,2)
sample_system = System(pend1,pend2)
initial = [1,2,3,4]
sample_system.set_initial(initial)

def test_Hamiltonian():
    assert sample_system.En_hamiltonian()+71.448 <0.001 




