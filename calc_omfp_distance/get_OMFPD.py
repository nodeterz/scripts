from ase.io import read, write
import numpy as np
import os
import sys


MDStructs=read('OutputStr.extxyz',index=':')
InputStructs=read('InputStr.extxyz')
TargetStructs=read('TargetStr.extxyz')

#get input structure OMFP
nat=InputStructs.get_global_number_of_atoms()
rat=InputStructs.get_positions()
sat=InputStructs.get_chemical_symbols()
posStream=open('posinp.xyz','w')
posStream.write('%d angestroem\nfree\n'%nat)
for iat in range(nat):
    posStream.write('%s %16.10f %16.10f %16.10f\n'%(sat[iat],rat[iat,0],rat[iat,1],rat[iat,2]))
posStream.close()
os.system('rm -f posinp.dat')
os.system('./calcOMFP.x')
initFP=np.loadtxt('fp.dat',dtype=np.float64)
os.system('rm -f fp.dat')

#get target structure OMFP
nat=TargetStructs.get_global_number_of_atoms()
rat=TargetStructs.get_positions()
sat=TargetStructs.get_chemical_symbols()
posStream=open('posinp.xyz','w')
posStream.write('%d angestroem\nfree\n'%nat)
for iat in range(nat):
    posStream.write('%s %16.10f %16.10f %16.10f\n'%(sat[iat],rat[iat,0],rat[iat,1],rat[iat,2]))
posStream.close()
os.system('rm -f posinp.dat')
os.system('./calcOMFP.x')
targetFP=np.loadtxt('fp.dat',dtype=np.float64)
os.system('rm -f fp.dat')

fpdStream=open('FPDist.dat','w')
#get structures OMFP distance
for istruct,struct in enumerate(MDStructs):
    nat=struct.get_global_number_of_atoms()
    rat=struct.get_positions()
    sat=struct.get_chemical_symbols()
    posStream=open('posinp.xyz','w')
    posStream.write('%d angestroem\nfree\n'%nat)
    for iat in range(nat):
        posStream.write('%s %16.10f %16.10f %16.10f\n'%(sat[iat],rat[iat,0],rat[iat,1],rat[iat,2]))
    posStream.close()
    os.system('rm -f posinp.dat')
    os.system('./calcOMFP.x')
    FP=np.loadtxt('fp.dat',dtype=np.float64)
    os.system('rm -f fp.dat')
    initFPD=np.linalg.norm(np.subtract(FP,initFP))
    targetFPD=np.linalg.norm(np.subtract(FP,targetFP))
    fpdStream.write('%07d %24.8e %24.8e\n'%(istruct,initFPD,targetFPD))
fpdStream.close()
