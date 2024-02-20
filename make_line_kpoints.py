from pymatgen.io.vasp.inputs import Kpoints
from pymatgen.core import Structure
from pymatgen.symmetry.bandstructure import HighSymmKpath

struct = Structure.from_file("POSCAR")
kpath = HighSymmKpath(struct)
print(kpath)
kpts = Kpoints.automatic_linemode(divisions=40,ibz=kpath)
kpts.write_file("KPOINTS_nsc")
kpt_file=open('KPOINTS_nsc','r')

lines=[]
for line in kpt_file:
    if line != '\n':
        lines.append(line)
lenFile=len(lines)
for i in range(5,lenFile-1,2):
    if lines[i].split()[-1] != lines[i+1].split()[-1]:
        print(lines[i].split()[-1],lines[i+1].split()[-1])
        lines.insert(i+1,lines[i])
        lines.insert(i+2,lines[i+2])
lines.insert(len(lines)-1,lines[-1])
lines.insert(len(lines),lines[4])

lenFile=len(lines)
for i in range(4,lenFile):
    print(lines[i])

outFile=open('KPOINTS','w')
for i in range(4):
    outFile.write(lines[i])
for i in range(4,lenFile,2):
    outFile.write(lines[i])
    outFile.write(lines[i+1])
    outFile.write('\n')
outFile.close()
kpt_file.close()
