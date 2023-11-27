from ase.io import read, write
from operator import itemgetter
import numpy as np

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
     

structures=read('all_minima_no_duplicates.extxyz',index=':')
# Extract energies and corresponding indices
energies_and_indices = [(structure.get_potential_energy(), i) for i, structure in enumerate(structures)]

# Sort structures based on energy
energies_and_indices.sort(key=itemgetter(0))

# Create a list of sorted structures
sorted_structures = [structures[i] for _, i in energies_and_indices]

indList = np.linspace(0, len(sorted_structures)-1, num=50, endpoint=True,dtype=int)
for iidx, idx in enumerate(indList):
    selStr=set_str_cell(sorted_structures[idx])
    sorted_structures[idx].write('posoutSelected.extxyz',format='extxyz',append=True)
    selStr.write('POSCAR%05d'%iidx, format='vasp')
