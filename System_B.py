from Oscillator_class import Oscillator
import numpy as np
import math
from System import System

"""
This is a special case of the double pendulum where the small angle approximation makes for an analytical solution
This class can be used to study the phenomenon of beats
For the sake of our analysis both pendulums need to be equal lengths
"""

class SystemB(System):


    def __init__(self,Pendulum1,Pendulum2):
        if Pendulum1.length != Pendulum2.length:
            raise Exception('Both pendulums are required to be equal length. You passed (l1: %s, l2: %s)' %(Pendulum1.length, Pendulum2.length))
        super().__init__(Pendulum1,Pendulum2)
        self.mu = self.second.mass/self.first.mass
        """
        This requires both lengths to be equal
        """
        self.omega1 = np.sqrt(self.g/self.first.length*(1+self.mu+np.sqrt((1+self.mu)*self.mu)))
        self.omega2 = np.sqrt(self.g/self.first.length*(1+self.mu-np.sqrt((1+self.mu)*self.mu)))

    
    def set_initial(self,Z0 = np.array([0,0,0,0],dtype = float)):
        if Z0[0] !=0 or Z0[1] >= 0.2 or Z0[2] !=0 or Z0[3] !=0:
            raise Exception('This system works only for initial conditions of the form [0,SMALL,0,0] where SMALL means <0.2. You passed %s.' %(Z0))
        super().set_initial(Z0)
    
    def angles(self,time,alph_01):
        alpha_1 = (alph_01/2)*np.sqrt(self.mu/(1+self.mu))*(-np.cos(self.omega1*time)+np.cos(self.omega2*time))
        alpha_2 =  alph_01/2*(np.cos(self.omega1*time) + np.cos(self.omega2*time))

        return([alpha_1,alpha_2])
    
    
    
