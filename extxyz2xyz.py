from ase.io import read, write
import numpy as np

strs=read('posoutSelected.extxyz',index=':')

for istr,struct in enumerate(strs):
    outStream=open('posinp_%05d.xyz'%istr,'w')
    pos=struct.get_positions()
    elems=struct.get_chemical_symbols()
    outStream.write('%d angstroem\nfree'%struct)
    for i in range(len(elems)):
        outStream.write('%2s %.8f %.8f %.8f\n'%(elems[i],pos[i][0],pos[i][1],pos[i][2]))
    outStream.close()
