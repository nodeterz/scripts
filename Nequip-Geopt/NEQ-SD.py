import os
import numpy as np
from ase import Atoms
from ase.io import read, write, Trajectory
from nequip.ase import NequIPCalculator
import argparse

str1 = "This script performs geopt with nequip with BFGS"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="input structure")
parser.add_argument('fn_out', action='store' ,type=str, help="output structure")
parser.add_argument('traj', action='store' ,type=str, help="trajectory name")
args=parser.parse_args()

# Set up the OpenKIM calculator
calculator =  NequIPCalculator.from_deployed_model(
        model_path="mymodel.pth",
        device = "cuda",
        species_to_type_name = {
            "Au": "Au",
        }
    )
atom = read(args.fn_inp)
atom.set_calculator(calculator)

e_tol= 1.E-6
E_new=1.E+100
E_old=0.E+0
alpha=1.E-5
SDiter=0
while abs(E_new-E_old) > e_tol :
    E_old=E_new
    atom.set_positions(   np.add( atom.get_positions(),np.multiply(alpha,atom.get_forces()) )   )
    E_new=atom.get_potential_energy()
    if E_new < E_old:
        alpha = min(alpha*1.02,1.E-3)
    else:
        alpha *= 0.5
    print('%07d %.8f %.6f'%(SDiter,alpha,E_new))
    SDiter += 1
    atom.write(args.traj,format='extxyz',append=True)


atom.write(args.fn_out,append=False)
