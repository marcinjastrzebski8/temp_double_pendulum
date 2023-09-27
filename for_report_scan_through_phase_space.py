import matplotlib.pyplot as plt
from abs_draw_bob_paths import Draw_bob
from Save_Pandas import SavePandas
import numpy as np
import pandas as pd

"""
This program was used to generate plots of phase space paths
at various energies
I have used this to categorise the possible outcomes
"""

sys = SavePandas(1,1,1,1)

for ang1 in np.linspace(0.1,np.pi,5):
    for ang2 in np.linspace(0.1,np.pi,10):
        for p1 in np.linspace(0,10,5):
            for p2 in np.linspace(0,10,5):
                z0 = [ang1,ang2,p1,p2]
                sys.Sys.set_initial(z0)
                ham = sys.Sys.En_hamiltonian()
                sys.simulation(7500,0.004,z0)
                sys.save_as('stps%s_%s_%s_%s'%(ang1,ang2,p1,p2))
                sys.Sys.set_initial([0,0,0,0])

                dat = pd.read_pickle('stps%s_%s_%s_%s.csv'%(ang1,ang2,p1,p2))
                x=[]
                y=[]
                for i in range(len(dat['TIME'])):
                    x.append(dat['ANGLE 1'][i])
                    y.append(dat['MOMENTUM 1'][i])
                plt.plot(x,y)
                plt.xlabel(R'$\theta_1$')
                plt.ylabel(R'$p_1$')
                plt.legend(['Hamiltonian = %s'%(ham)])
                plt.savefig('stps%s_%s_%s_%s.png'%(ang1,ang2,p1,p2))
                plt.close()
                    



