import numpy as np
import argparse
str1 = "This script is for finding the best fit for large clusters."
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp_ref', action='store' ,type=str, help="reference energies")
parser.add_argument('fn_inp_pre', action='store' ,type=str, help="predicted energies")
args=parser.parse_args()

refFile=open(args.fn_inp_ref,'r')
preFile=open(args.fn_inp_pre,'r')
Ha2Ev=27.2114079527E0

nat=[]
epot_ref=[]
for line in refFile:
    nat.append(int(line.split()[1]))
    epot_ref.append(float(line.split()[2]))
tmp=epot_ref[0]
epot_ref_nat=[]
for iconf in range(len(epot_ref)):
    epot_ref[iconf] -=tmp
    epot_ref[iconf] *= Ha2Ev 
    epot_ref_nat.append(epot_ref[iconf]/nat[iconf])

epot_pre=[]
for line in preFile:
    epot_pre.append(float(line.split()[1]))
tmp=epot_pre[0]
epot_pre_nat=[]
for iconf in range(len(epot_pre)):
    epot_pre[iconf] -= tmp
    epot_pre[iconf] *= Ha2Ev
    epot_pre_nat.append(epot_pre[iconf]/nat[iconf])
    

rmse=np.sqrt(np.mean((np.subtract(epot_pre,epot_ref))**2))
rmsePerNat=np.sqrt(np.mean((np.subtract(epot_pre_nat,epot_ref_nat))**2))

print(args.fn_inp_pre,rmse,'ev',rmsePerNat,'ev/Atom')
