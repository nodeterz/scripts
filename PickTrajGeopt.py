#from ase.calcul ators.eam import EAM
#rom ase.cluster.wulff import wulff_construction
#from ase.cluster.icosahedron import Icosahedron
from ase.io import read
from ase.md.andersen import Andersen
from ase.md import MDLogger
from ase.io import write, Trajectory
from ase.units import fs

def write_vsim():
    structs = Trajectory('toto.traj')
    Traj_len=len(structs)
    for i in range(100000):
        if i%50 == 0 :
            structs[i].write('InputStr%07d.extxyz'%i,format='extxyz',append=False)    
        elif i==(Traj_len-1) :
            structs[i].write('InputStr%07d.extxyz'%i,format='extxyz',append=False)    


if __name__ == '__main__':
    write_vsim()
    quit()
