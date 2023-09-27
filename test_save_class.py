import pytest
from Save_Pandas import SavePandas
import pandas as pd

"""
Test if pandas are being saved properly
"""

Save = SavePandas(1,2,1,1)
Save.simulation(10000,0.001,[0,3,0,0])

Save.save_as('check')

check = pd.read_pickle('check.csv')

def test_SavePandas():
    assert check['PENDULUM INFO'][0] == {'m1':1,'m2':2,'l1':1,'l2':1}

print(check)