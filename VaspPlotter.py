from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSPlotter

import matplotlib.pyplot as plt  # Import matplotlib

# Load vasprun.xml file
vasprun = Vasprun("vasprun.xml")

# Get band structure
band_structure = vasprun.get_band_structure("KPOINTS")

# Plot the band structure
bs_plotter = BSPlotter(band_structure)
fig = bs_plotter.get_plot()
plt.show()  # Show the figure

