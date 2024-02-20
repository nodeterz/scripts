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
    for i in range(Traj_len):
        if i%1000 == 0 :
            filename = 'mymd'+str(i).zfill(7)+'.xyz'
            write(filename, structs[i])    
        elif i==(Traj_len-1) :
            filename = 'mymd'+str(i).zfill(7)+'.xyz'
            write(filename, structs[i])    


if __name__ == '__main__':
    write_vsim()
    quit()
