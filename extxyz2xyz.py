from ase.io import read, write
import numpy as np
import argparse
str1 = "This script converts extxyz to xyz "
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="input structure")
args=parser.parse_args()

strs=read(args.fn_inp,index=':')

for istr, struct in enumerate(strs):
    struct.write('posout_%05d.xyz'%istr,format='xyz',append=False)
