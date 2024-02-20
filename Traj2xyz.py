#from ase.calcul ators.eam import EAM
#rom ase.cluster.wulff import wulff_construction
#from ase.cluster.icosahedron import Icosahedron
from ase.io import read
from ase.md.andersen import Andersen
from ase.md import MDLogger
from ase.io import write, Trajectory
from ase.units import fs

def write_vsim():
    structs = Trajectory('md_0000000.traj')
    Traj_len=len(structs)
    for i in range(Traj_len):
        structs[i].write('InputStr%07d.xyz'%i,format='xyz',append=False)    


if __name__ == '__main__':
    write_vsim()
    quit()
