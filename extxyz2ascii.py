import sys
from ase.io import read, write

inpstr=read(sys.argv[1],index=":")

for istr,strs in enumerate(inpstr):
    strs.write('%04d.ascii'%istr,format='v-sim')
