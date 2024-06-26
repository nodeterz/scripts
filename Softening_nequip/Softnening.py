import numpy as np
from ase import Atoms
from ase.vibrations import Vibrations
from ase.io import write,read
from nequip.ase import NequIPCalculator
import sys

calculator =  NequIPCalculator.from_deployed_model(
        model_path="mymodel.pth",
        device = "cuda",
        species_to_type_name = {
            "Au": "Au",
        }
    )

# Define your structure (Example: Lennard-Jones cluster of 13 atoms)
atoms = read(sys.argv[1])
atoms.calc=calculator

# Calculate vibrational modes
vib = Vibrations(atoms)
vib.run()

# Get the softest mode (mode with the lowest frequency)
frequencies = vib.get_frequencies()
modes = vib.get_mode(-1)  # Assuming the softest mode is the last one
print(vib.get_mode(-1))


# Define a function to move the structure in a given direction
def move_in_direction(atoms, direction, step_size, num_steps, prefix):
    positions = atoms.get_positions()
    for step in range(num_steps):
        positions += step_size * direction
        atoms.set_positions(positions)
        write(f'{prefix}_step_{step}.xyz', atoms)

# Move 10 steps in the direction of the soft mode
move_in_direction(atoms, modes, step_size=2.1, num_steps=10, prefix='forward')

# Move 10 steps in the opposite direction of the soft mode
move_in_direction(atoms, -modes, step_size=2.1, num_steps=10, prefix='backward')

# Clean up
vib.clean()

