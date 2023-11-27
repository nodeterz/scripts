from ase.io import read, write
import argparse
import numpy as np
str1 = "scale XYZ"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="input file name in extxyz format")
parser.add_argument('scale', action='store' ,type=float, help="Scale 0.0-1.0")
parser.add_argument('fn_out', action='store' ,type=str, help="output file name in extxyz format")
args=parser.parse_args()

structures = read(args.fn_inp)
structures.set_positions(np.multiply(structures.get_positions(),args.scale))
structures.write(args.fn_out,format='extxyz',append=False)
