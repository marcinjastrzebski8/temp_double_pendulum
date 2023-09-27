from Oscillator_class import Oscillator
import numpy as np
import math

class System():
    """
    This class takes two pendulums and sets them in motion.
    The equations of motion are those of hamiltonian mechanics;
    Therefore, the system uses generalised coordinates - (angle and generalised momentum in this case)
    User can pick the initial conditions (the angle and momentum for each pendulum)
    """

    def __init__(self,Pendulum1,Pendulum2):
        #an exception will be thrown in some limiting cases for very small pendulums
        if Pendulum1.length <= 10**(-3) or Pendulum1.mass <= 10**(-5) or Pendulum2.mass <=10**(-5) or Pendulum2.length <=10**(-3):
            raise Exception('The parameters of the system you have passed are too small')
        self.first = Pendulum1
        self.second = Pendulum2
        #the parameters of the system - angles and momenta are stored in Z
        self.Z = np.array([0,0,0,0],dtype = float)
        self.g = 10 

    def set_initial(self,Z0 = np.array([0,0,0,0],dtype = float)):
        """
        The format for Z0 is [angle1,angle2,momentum1,momentum2]!
        """
        self.Z = Z0
    
    def motion(self,some_Z = np.array([0,0,0,0],dtype = float)):

        """
        This function describes the evolution of the system in time
        some_Z yields the parameters of the system 
        A1 and A2 are defined just to make the really messy formulae a bit less messy
        f1-f4 correspond to the derivatives of the elements of some_Z wrt time
        The return is a numpy array f made up of those.
        """

        self.A1 = (some_Z[2]*some_Z[3]*np.sin(some_Z[0]-some_Z[1]))* \
                  ((self.first.length*self.second.length)*(self.first.mass+self.second.mass*(np.sin(some_Z[0]-some_Z[1]))**2))**(-1)

        self.A2 = (((some_Z[2]**2)*self.second.mass*(self.second.length**2)-2*some_Z[2]*some_Z[3]*self.second.mass*self.first.length*self.second.length*np.cos(some_Z[0]-some_Z[1])+(some_Z[3]**2)*(self.first.mass+self.second.mass)*(self.first.length**2))*np.sin(2*(some_Z[0]-some_Z[1])))* \
                  (2*(self.first.length**2)*(self.second.length**2)*(self.first.mass+self.second.mass*((np.sin(some_Z[0]-some_Z[1]))**2))**2)**(-1)

        self.f1 = (some_Z[2]*self.second.length - some_Z[3]*self.first.length*np.cos(some_Z[0]-some_Z[1]))* \
                  ((self.first.length**2)*self.second.length*(self.first.mass + self.second.mass*(np.sin(some_Z[0]-some_Z[1]))**2))**(-1)

        self.f2 = (some_Z[3]*(self.first.mass+self.second.mass)*self.first.length - some_Z[2]*self.second.mass*self.second.length*np.cos(some_Z[0]-some_Z[1]))* \
                  (self.second.mass*self.first.length*(self.second.length**2)*(self.first.mass+self.second.mass*((np.sin(some_Z[0]-some_Z[1]))**2)))**(-1)

        self.f3 = -(self.first.mass+self.second.mass)*self.g*self.first.length*np.sin(some_Z[0]) - self.A1 + self.A2

        self.f4 = -self.second.mass*self.g*self.second.length*np.sin(some_Z[1])+self.A1-self.A2

        self.f = [self.f1,self.f2,self.f3,self.f4]
        return np.array(self.f)
    

    def RK(self,deltaT):

        """
        The Runge-Kutta(4) method of numerical integration
        """

        self.Y1 = np.multiply(deltaT,self.motion(self.Z))
        self.Y2 = np.multiply(deltaT,self.motion(self.Z+np.multiply(0.5,self.Y1)))
        self.Y3 = np.multiply(deltaT,self.motion(self.Z+np.multiply(0.5,self.Y2)))
        self.Y4 = np.multiply(deltaT,self.motion(self.Z+self.Y3))

        self.Z = self.Z + (self.Y1+ np.multiply(2,self.Y2)+np.multiply(2,self.Y3)+self.Y4)/6

    def En_hamiltonian(self):
        """
        The user can calculate the hamiltonian of the system
        """
        num1 = self.second.mass*((self.second.length)**2)*((self.Z[2])**2)
        num2 = (self.first.mass + self.second.mass)*((self.first.length)**2)*((self.Z[3])**2)
        num3 = 2*self.second.mass*self.first.length*self.second.length*self.Z[2]*self.Z[3]*np.cos((self.Z[0])-(self.Z[1]))
        den1 = 2*self.second.mass*((self.first.length)**2)*((self.second.length)**2)
        den2 = self.first.mass + self.second.mass*(np.sin((self.Z[0])-(self.Z[1]))**2)
        component1 = (self.first.mass + self.second.mass)*self.g*self.first.length*np.cos(self.Z[0])
        component2 = self.second.mass*self.g*self.second.length*np.cos(self.Z[1]) 

        self.hamiltonian = (num1+num2-num3)/(den1*den2) - component1 -component2
        return(self.hamiltonian)
        
    

