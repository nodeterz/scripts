from ase.io import read, write
import numpy as np
import argparse

str1 = "This script extxyz2poscar to POSCAR"
parser = argparse.ArgumentParser(description=str1)
parser.add_argument('fn_inp', action='store' ,type=str, help="input extxyz")
parser.add_argument('fn_out', action='store' ,type=str, help="output POSCAR name")
parser.add_argument('vac', action='store' ,type=float, help="Vaccume in each side")
args=parser.parse_args()

def set_str_cell(structure=None,vac=5.0):
    rat=structure.get_positions()
    x=rat[:,0]
    y=rat[:,1]
    z=rat[:,2]
    xmin=min(x)
    ymin=min(y)
    zmin=min(z)
    padX=vac-xmin
    padY=vac-ymin
    padZ=vac-zmin
    x=np.add(x,padX)
    y=np.add(y,padY)
    z=np.add(z,padZ)
    rat2=[]
    for i in range(len(x)):
        rat2.append([x[i],y[i],z[i]])
    #for i in range(len(x)):
    #    print(rat2[i])
    cellX=[max(x)+(vac),0,0]
    cellY=[0,max(y)+(vac),0]
    cellZ=[0,0,max(z)+(vac)]
    structure.set_positions(rat2)
    structure.set_cell([cellX,cellY,cellZ])
    
    return structure
     

structure=read(args.fn_inp)
selStr=set_str_cell(structure,vac=args.vac)
selStr.write(args.fn_out, format='vasp')
