The main pieces of code which are used for the analysis are the three classes: Oscillator_class, System and SavePandas.
These three files are enough to run any simulation.

Oscillator class is very simple - instantiate a simple pendulum. Two are needed to define a System. (This could have been done in an easier way but it is just a relic of my initial ideas and it works)
System can be used on its own to create a double pendulum system and write an arbitrary simulation.
SystemB is a simple subclass of System which includes the analytical solutions of small angle approximation 
resulting in a phenomenon of beats.

One can also use SavePandas which will use System and perfrom any simulation, saving the pendulum information, displacements
and momenta as well as the energy of the system at each step as a pandas DataFrame.
Most analysis is performed using SavePandas, with some exceptions.

To run a simulation using SavePandas do:
my_sim = SavePandas(mass1,mass2,length1,length2)
my_sim.simulation(how_many_steps,timestep,initial_conditions)
my_sim.save_as('name_of_my_dataset')

abstract_draw is an abstract class making plotting faster. all the files starting with abs_ are subclasses of this class

animate is not used in the report but can animate any run saved with SavePandas. Three examples have been
put up on youtube and links are included in the report 

All programs starting with for_report_ are pieces of analysis performed for the report:
	flip saves an alternative dataset to the one sved with SavePandas
	that data set is drawn using draw_flip
	beats used in Section about beats
	paths used in Section about initial conditions sensitivity
	scan_through_phase_space used in Section about different energy ranges
	shm is simple harmonic motion used as a test

hamiltonian_check_for_flip used to ensure energy is conserved before running for_report_flip

Two folders scans and scans_data can be seen:
	scans contains five subfolders where I have cateorised pictures (png) of paths drawn with 
	for_report_scan_through_phase_space
	scans_data contains ALL the dataframes corresponding to those paths (not categorised)

Hams_cat is a class I created to access runs in scans_data belonging to one category only
so that a hamiltonian histogram can be created for each category, which is done using
save_all_hams

all the files begining with test_ contain pytest checks of code validity 



