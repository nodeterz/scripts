import os
import argparse
import numpy as np
from ase.io import read, write
from FpLaplace import get_laplace_fingerprint
from FpLaplace import get_laplace_fingerprint_distance

str1 = "This script selects diverse structures based on laplace fingerprint"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="input file name in extended xyz format")
parser.add_argument('fn_out', action='store' ,type=str, help="output file name in extended xyz format")
parser.add_argument('fp_tol', action='store' ,type=float, help="minimum fingerprint distance")
args=parser.parse_args()

if(os.path.isfile(args.fn_out)):
    print('Error:',args.fn_out, 'exists.')
    quit()

allStructures = read(args.fn_inp,index=':')
structures=allStructures
selList=[]

def sel_str(strs,addVal,selList,fp_tol):
    lenStr=len(strs)
    dist_mat = np.zeros((lenStr,lenStr))
    for istr in range(lenStr):
        fp_dist_i=get_laplace_fingerprint(input_str=strs[istr], verbose=False, calcDer=False)
        for jstr in range(istr+1,lenStr):
            if(jstr<istr):
                continue
            fpDist=get_laplace_fingerprint_distance(src_fingerprint=fp_dist_i, trg_struct=strs[jstr], calcDer=False)
            dist_mat[istr,jstr]=fpDist
            dist_mat[jstr,istr]=fpDist
    for istr in range(lenStr):
        if np.all(dist_mat[istr,:] == 0):
            continue
        else:
            selList.append(istr+addVal)
            low_index = np.where(dist_mat[istr,:] < fp_tol)
            for row in low_index:
                dist_mat[row,:] = 0
    return selList
h1=False
h2=False
batchsize=16
while True:
    lenAllStr=len(structures)
    print(lenAllStr,batchsize)
    intPart=int(lenAllStr/batchsize)
    remPart=lenAllStr-intPart*batchsize
    selList=[]
    for ipart in range(intPart):
        strs=structures[ipart*batchsize:(ipart+1)*batchsize]
        addVal=ipart*batchsize
        selList=sel_str(strs,addVal,selList,args.fp_tol)

    strs=structures[intPart*batchsize:]
    addVal=intPart*batchsize
    selList=sel_str(strs,addVal,selList,args.fp_tol)
    
    if(lenAllStr==len(selList)):
        if h1:
            h2 = True
        if h2:
            for struct in structures:
                struct.write(args.fn_out,format='extxyz',append=True)
            break
        h1=True
        if batchsize < 128:
            batchsize = 128
    StartStructures=[]
    for istr in selList:
        StartStructures.append(structures[istr])
    structures=StartStructures
    batchsize = min(int(batchsize*1.5),256)
