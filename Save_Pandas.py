import numpy as np
import math
from Oscillator_class import Oscillator
from System import System
import pandas as pd

"""
This class is used to run most of the simulations and save all the necessary information about 
the system as pd.DataFrame()
"""


class SavePandas():

    """
    Initialise with the pendulum information
    """
    def __init__(self,m1,m2,l1,l2):
        self.pend1 = Oscillator(m1,l1)
        self.pend2 = Oscillator(m2,l2)
        self.Sys = System(self.pend1,self.pend2)

        self.pend_info = {'m1':m1,'m2':m2,'l1':l1,'l2':l2}


    def simulation(self,steps,timestep,initial_cond = np.array([0,0,0,0],dtype = float)):
        """
        Need to pass all the information defining the simulation - number of step, time step length and Z0
        """
        self.Sys.set_initial(initial_cond)

        
        self.data = [] #to be converted into a DataFrame
        for step in range(steps):
            self.data_time = step*timestep
            self.data_angle1 = self.Sys.Z[0]
            self.data_angle2 = self.Sys.Z[1]
            self.data_mom1 = self.Sys.Z[2]
            self.data_mom2 = self.Sys.Z[3]
            self.data_ham = self.Sys.En_hamiltonian()
            if step ==0: #only include pendulum information on the first entry
                self.data.append([self.data_time,self.data_angle1,self.data_mom1,self.data_angle2,self.data_mom2,self.data_ham,self.pend_info])
            else:
                self.data.append([self.data_time,self.data_angle1,self.data_mom1,self.data_angle2,self.data_mom2,self.data_ham])

            self.Sys.RK(timestep)

        
        self.df = pd.DataFrame(self.data,columns=['TIME','ANGLE 1','MOMENTUM 1', 'ANGLE 2', 'MOMENTUM 2', 'HAMILTONIAN','PENDULUM INFO'])


    """
    User needs to specify the name of the file containing pandas
    """
    def save_as(self,name = 'name'):
        self.df.to_pickle('%s.csv'%name)
