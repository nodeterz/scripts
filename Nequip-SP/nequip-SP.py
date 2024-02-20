import os
import numpy as np
from nequip.ase import NequIPCalculator
from ase.io import read, write
from ase import Atoms
from ase.optimize import BFGS, FIRE
from ase.calculators.emt import EMT
from ase.io import write, Trajectory
import argparse

str1 = "This script performs SP with nequip"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="input structure")
args=parser.parse_args()

calculator =  NequIPCalculator.from_deployed_model(
        model_path="mymodel.pth",
        device = "cuda",
        species_to_type_name = {
            "Au": "Au",
        }
    )

atom = read(args.fn_inp)
atom.set_calculator(calculator)
print(atom.get_potential_energy(),' (eV)')
