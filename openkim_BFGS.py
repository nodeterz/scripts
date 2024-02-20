import os
import numpy as np
from ase import Atoms
from ase.io import read, write, Trajectory
from ase.optimize import BFGS, FIRE
from ase.calculators.kim import KIM
import argparse

str1 = "This script performs geopt with nequip with BFGS"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="input structure")
parser.add_argument('fn_out', action='store' ,type=str, help="output structure")
parser.add_argument('traj', action='store' ,type=str, help="trajectory name")
args=parser.parse_args()

# Set up the OpenKIM calculator
kim_model = 'EAM_QuinticClampedSpline_Kim_2021_PtAu__MO_463728687265_000'
calculator = KIM(kim_model)
#calculator =  NequIPCalculator.from_deployed_model(
#        model_path="mymodel.pth",
#        device = "cuda",
#        species_to_type_name = {
#            "Au": "Au",
#        }
#    )

atom = read(args.fn_inp)
atom.set_calculator(calculator)
dyn = BFGS(atom,trajectory = args.traj,alpha=1.0)
dyn.run(fmax=0.005)
atom.write(args.fn_out,append=False)
