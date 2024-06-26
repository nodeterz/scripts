import sys
from ase.io import read, write, Trajectory

def write_vsim(filename,filename2):
    structs = Trajectory(filename)
    Traj_len=len(structs)
    for i in range(Traj_len):
        if i==0:
            structs[i].write(filename2,format='extxyz',append=False)    
        else:
            structs[i].write(filename2,format='extxyz',append=True)    


if __name__ == '__main__':
    write_vsim(sys.argv[1],sys.argv[2])
    quit()
