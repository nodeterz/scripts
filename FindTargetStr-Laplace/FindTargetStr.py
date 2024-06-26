import sys
import argparse
import numpy as np
from ase.io import read
from FpLaplace import get_laplace_fingerprint

def main():
    str1 = "This script calculates laplace fingerprint distance for structures in fn_inp and fn_trg."
    parser = argparse.ArgumentParser(description=str1)
    parser.add_argument('fn_inp', action='store' ,type=str, help="input  structure name in extxtz format")
    parser.add_argument('fn_trg', action='store' ,type=str, help="target structure name in extxyz format")
    args=parser.parse_args()
    inp_structure = read(args.fn_inp,format='extxyz',index=':')
    trg_structure = read(args.fn_trg,format='extxyz')
    FP_target = get_laplace_fingerprint(trg_structure, calcDerivative=False , verbose=False)
    fpDists=[]
    sys.stdout.write('%s\n'%args.fn_inp)
    for istr,strs in enumerate(inp_structure):
        FP_initial = get_laplace_fingerprint(strs, calcDerivative=False , verbose=False)
        FpDist = np.linalg.norm(np.subtract(FP_initial,FP_target))**2
        fpDists.append(FpDist)
        sys.stdout.flush()
    sorted_indices = np.argsort(fpDists)
    lowest_indices = sorted_indices[:5]
    for index in lowest_indices:
        sys.stdout.write('%05d: %.6f\t|\t'%(index,fpDists[index]))
    sys.stdout.write('\n')
    sys.stdout.flush()

if __name__ == '__main__':
    main()
