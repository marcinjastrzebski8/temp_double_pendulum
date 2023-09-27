from Hams_cat import Hams_cat
import pandas as pd
import matplotlib.pyplot as plt

"""
This program plots historams for the 5 motion categories
"""
chaotic_flip = Hams_cat('chaotic__flip')
chaotic_no_flip = Hams_cat('chaotic_no_flip')
high_en_spinning = Hams_cat('high_en_spinning')
quasiperiodic_high = Hams_cat('quasiperiodic_high')
quasiperiodic_small = Hams_cat('quasiperiodic_small')




d1 = pd.read_pickle('hams_chaotic__flip.csv')
d2 = pd.read_pickle('hams_chaotic_no_flip.csv')
d3 = pd.read_pickle('hams_high_en_spinning.csv')
d4 = pd.read_pickle('hams_quasiperiodic_high.csv')
d5 = pd.read_pickle('hams_quasiperiodic_small.csv')

hams1 = d1['HAMILTONIAN']
hams2 = d2['HAMILTONIAN']
hams3 = d3['HAMILTONIAN']
hams4 = d4['HAMILTONIAN']
hams5 = d5['HAMILTONIAN']

plt.hist(hams1,50)
plt.xlabel('Hamiltonian')
plt.ylabel('Counts')
plt.legend(['Category C'])
plt.show()
plt.hist(hams2,50)
plt.xlabel('Hamiltonian')
plt.ylabel('Counts')
plt.legend(['Category B'])
plt.show()
plt.hist(hams3,50)
plt.xlabel('Hamiltonian')
plt.ylabel('Counts')
plt.legend(['Category D'])
plt.show()
plt.hist(hams4,50)
plt.xlabel('Hamiltonian')
plt.ylabel('Counts')
plt.legend(['Category E'])
plt.show()
plt.hist(hams5,50)
plt.xlabel('Hamiltonian')
plt.ylabel('Counts')
plt.legend(['Category A'])

plt.show()