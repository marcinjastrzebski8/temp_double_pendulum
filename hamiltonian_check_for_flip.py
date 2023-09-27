import numpy as np
import math
from Save_Pandas import SavePandas
import pandas as pd
from abs_draw_ham import Draw_ham 
"""
I used this to ensure energy is conserved before running the flip program
"""

sim = SavePandas(1,1,0.1,0.1)
sim.simulation(500000,0.002,[3,3,0,0])
sim.save_as('check_hammie')
draw_hammie = Draw_ham()
draw_hammie.get_dataset('check_hammie.csv')
draw_hammie.draw()
draw_hammie.show()