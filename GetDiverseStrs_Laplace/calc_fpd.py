import os
import argparse
import numpy as np
from tqdm import tqdm
from ase.io import read, write
from FpLaplace import get_laplace_fingerprint
from FpLaplace import get_laplace_fingerprint_distance

str1 = "This script selects diverse structures based on laplace fingerprint"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="input file name in extended xyz format")
args=parser.parse_args()

structures = read(args.fn_inp,index=':')
lenStr=len(structures)
dist_mat = np.zeros((lenStr,lenStr))

for istr in range(lenStr):
    fp_dist_i=get_laplace_fingerprint(input_str=structures[istr], verbose=False, calcDer=False)
    for jstr in range(lenStr):
        fpDist=get_laplace_fingerprint_distance(src_fingerprint=fp_dist_i, trg_struct=structures[jstr], calcDer=False)
        print(istr,jstr,fpDist)
