import numpy as np
from ase.io import read, write
from ase import Atoms
from collections import defaultdict
import sys

def sort_atoms_by_type(atoms):
    atom_types = defaultdict(list)
    for atom in atoms:
        atom_types[atom.symbol].append(atom)
    sorted_atoms = []
    for symbol in ['Mg', 'Ti', 'O']:  # Custom order of elements
        sorted_atoms.extend(atom_types.get(symbol, []))
    return sorted_atoms

# Read the extxyz file
filename=sys.argv[1]
all_atoms = read(filename,index=":")
for iatoms,atoms in enumerate(all_atoms):
    # Sort atoms by atom type
    sorted_atoms = sort_atoms_by_type(atoms)
    satoms = Atoms(sorted_atoms)
    satoms.set_cell(atoms.get_cell())
    
    # Write sorted atoms to POSCAR file
    write('sorted_%04d.poscar'%iatoms, satoms, format='vasp')

